import datetime
import sqlite3 as sl
from enum import Enum

from src.tools.html_base import *

LABELS = ["id", "day", "title", "description", "category"]


class CATEGORIES(Enum):
    angledroit = "AngleDroit"
    art = "Art"
    cinema = "Cinéma"
    divers = "Divers"
    education = "Education"
    environnement = "Environnement"
    feminisme = "Féminisme"
    gastronomie = "Gastronomie"
    geographie = "Géographie"
    histoire = "Histoire"
    internet = "Internet"
    jeux = "Jeux"
    langues = "Langues"
    litterature = "Littérature"
    media = "Média"
    musique = "Musique"
    nature = "Nature"
    sante = "Santé"
    sciences = "Sciences"
    societe = "Société"
    sports = "Sports"


def to_str(number: int) -> str:
    return str(number).rjust(2, '0')


def date_to_str(date: datetime.date) -> str:
    return f"{to_str(date.day)}/{to_str(date.month)}"


def n_to_br(text: str) -> str:
    return text.replace("\n", "<br>")


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
            SELECT * FROM AGENDA WHERE category = '{category}' ORDER BY date DESC;
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


def event_to_card(event: dict) -> str:
    return CARD.format(event["id"], event["title"], "tmp", event["day"], n_to_br(event["description"]))


def event_to_single_card(event: dict) -> str:
    return SINGLE_CARD.format(event["title"], "tmp", event["day"], n_to_br(event["description"]))


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


def render_category(category: str) -> str:
    events_category = get_events_by_category(category)
    cards_category = list(map(lambda x: event_to_card(x), events_category))
    page_category = CARDS_CONTAINER.format("even", f"{CATEGORIES[category].value}", "\n".join(cards_category))
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
