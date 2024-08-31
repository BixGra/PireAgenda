import datetime
import sqlite3 as sl

from src.tools.html_base import *

LABELS = ["id", "day", "title", "description", "category1", "category2", "category3", "link", "link_title"]

MONTHS = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]


def to_str(number: int) -> str:
    return str(number).rjust(2, '0')


def date_to_str(date: datetime.date) -> str:
    return f"{to_str(date.day)}/{to_str(date.month)}"


def n_to_br(text: str) -> str:
    return text.replace("\n", "<br>")


def parity(number: [int, str]) -> str:
    return "odd" if int(number) % 2 else "even"


def get_all_events() -> list[dict]:
    with sl.connect(f"./src/data/pireagenda.db") as con:
        cur = con.cursor()
        cur.execute(f"""
            SELECT * FROM AGENDA;
        """)
        events = cur.fetchall()
        return list(map(lambda x: dict(zip(LABELS, x)), events))


def get_events_by_date(date: str) -> list[dict]:
    with sl.connect(f"./src/data/pireagenda.db") as con:
        cur = con.cursor()
        cur.execute(f"""
            SELECT * FROM AGENDA WHERE date = '{date}';
        """)
        events = cur.fetchall()
        return list(map(lambda x: dict(zip(LABELS, x)), events))


def get_events_by_category(category: str) -> list[dict]:
    with sl.connect(f"./src/data/pireagenda.db") as con:
        cur = con.cursor()
        cur.execute(f"""
            SELECT * FROM AGENDA WHERE (
                category1 = '{category}'
                OR category2 = '{category}'
                OR category3 = '{category}'
            ) ORDER BY date DESC;
        """)
        events = cur.fetchall()
        return list(map(lambda x: dict(zip(LABELS, x)), events))


def get_event_by_id(event_id: int) -> dict:
    with sl.connect(f"./src/data/pireagenda.db") as con:
        cur = con.cursor()
        cur.execute(f"""
            SELECT * FROM AGENDA WHERE id = '{event_id}' LIMIT 1;
        """)
        event = cur.fetchall()
        return dict(zip(LABELS, event.pop()))


def event_to_all_item(event: dict) -> str:
    return ALL_ITEM.format(event["title"], event["id"], f'{event["day"]} - {event["title"]}')


def event_to_text(event: dict) -> str:
    description = n_to_br(event["description"])
    title = event["link_title"] if not event["link_title"] == "none" else "Pour aller plus loin"
    link = CARD_LINK.format(title, event["link"], title) if not event["link"] == "none" else ""
    return description + link


def category_to_tag(category: str) -> str:
    return TAG.format(category, category, get_category(category))


def event_to_tags(event: dict) -> str:
    tags = [category_to_tag(event[category]) for category in ["category1", "category2", "category3"] if not event[category] == "none"]
    return TAGS_CONTAINER.format("\n".join(tags))


def event_to_card(event: dict) -> str:
    page_tags = event_to_tags(event)
    return CARD.format(event["title"], event["id"], event["title"], event["category1"], event["day"], event_to_text(event), page_tags)


def event_to_single_card(event: dict) -> str:
    page_tags = event_to_tags(event)
    return SINGLE_CARD.format(event["title"], event["category1"], event["day"], event_to_text(event), page_tags)


def no_event_card(date) -> str:
    return NO_CARD.format(date)


def render_index(date: str = None) -> str:
    is_today = not bool(date)
    if is_today:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date + "/2024", "%d/%m/%Y").date()

    today = date_to_str(date)
    events_today = get_events_by_date(today)
    if events_today:
        cards_today = list(map(lambda x: event_to_card(x), events_today))
    else:
        cards_today = [no_event_card(today)]

    tomorrow = date_to_str(date + datetime.timedelta(days=1))
    events_tomorrow = get_events_by_date(tomorrow)
    if events_tomorrow:
        cards_tomorrow = list(map(lambda x: event_to_card(x), events_tomorrow))
    else:
        cards_tomorrow = [no_event_card(tomorrow)]

    yesterday = date_to_str(date - datetime.timedelta(days=1))
    events_yesterday = get_events_by_date(yesterday)
    if events_yesterday:
        cards_yesterday = list(map(lambda x: event_to_card(x), events_yesterday))
    else:
        cards_yesterday = [no_event_card(yesterday)]

    if is_today:
        page_today = CARDS_CONTAINER.format("even", f"Aujourd'hui {today}", "\n".join(cards_today))
        page_tomorrow = CARDS_CONTAINER.format("odd", f"Demain {tomorrow}", "\n".join(cards_tomorrow))
        page_yesterday = CARDS_CONTAINER.format("even", f"Hier {yesterday}", "\n".join(cards_yesterday))
    else:
        page_today = CARDS_CONTAINER.format("even", f"Journée du {today}", "\n".join(cards_today))
        page_tomorrow = CARDS_CONTAINER.format("odd", f"Le lendemain {tomorrow}", "\n".join(cards_tomorrow))
        page_yesterday = CARDS_CONTAINER.format("even", f"La veille {yesterday}", "\n".join(cards_yesterday))

    return HEADER + page_today + page_tomorrow + page_yesterday + FOOTER


def render_all_events() -> str:
    all_events = get_all_events()
    months = {f"{to_str(i)}": [] for i in range(1, 13)}
    list(map(lambda x: months[x["day"].split("/")[1]].append(x), all_events))
    page_events = ""
    for month, events in map(lambda y: (int(y[0])-1, y[1]), sorted(months.items(), key=lambda x: int(x[0]))):
        if events:
            page_event = list(map(lambda x: event_to_all_item(x), sorted(events, key=lambda x: int(x["day"].split("/")[0]))))
            amount_events = len(page_event)
        else:
            page_event = [no_event_card(f"{MONTHS[month]}")]
            amount_events = 0
        page_events += ALL_CONTAINER.format(parity(month), f"{MONTHS[month]} - {amount_events} événements", "\n".join(page_event))
    return HEADER + page_events + FOOTER


def render_category(category: str) -> str:
    events_category = get_events_by_category(category)
    cards_category = list(map(lambda x: event_to_card(x), events_category))
    page_category = CARDS_CONTAINER.format("even", f"{get_category(category)}", "\n".join(cards_category))
    return HEADER + page_category + FOOTER


def render_category_by_month(category: str) -> str:
    events_category = get_events_by_category(category)
    months = {f"{to_str(i)}": [] for i in range(1, 13)}
    list(map(lambda x: months[x["day"].split("/")[1]].append(x), events_category))
    page_category = ""
    for month, events in map(lambda y: (int(y[0])-1, y[1]), sorted(months.items(), key=lambda x: int(x[0]))):
        if events:
            cards_category = list(map(lambda x: event_to_card(x), sorted(events, key=lambda x: int(x["day"].split("/")[0]), reverse=True)))
        else:
            cards_category = [no_event_card(f"{MONTHS[month]}")]
        page_category += CARDS_CONTAINER.format(parity(month), f"{MONTHS[month]} - {get_category(category)}", "\n".join(cards_category))
    return HEADER + page_category + FOOTER


def render_event(event_id: int) -> str:
    event = get_event_by_id(event_id)
    card_event = event_to_single_card(event)
    page_event = CARDS_CONTAINER.format("even", event["title"], card_event)
    return HEADER + page_event + FOOTER


def render_filter_date() -> str:
    return HEADER + FILTER_DATE + FOOTER


def render_filter_category() -> str:
    return HEADER + FILTER_CATEGORY + FOOTER
