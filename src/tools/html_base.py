import os
from enum import Enum

root = "/pireagenda" if "PIREAGENDAPROD" in os.environ else ""


class CATEGORIES(Enum):
    angledroit = "AngleDroit"
    animaux = "Animaux"
    art = "Art"
    cinema_series = "Cinéma/Séries"
    conflit = "Conflit"
    culture = "Culture"
    divers = "Divers"
    droit_justice = "Droit/Justice"
    ecologie_environnement = "Écologie/Environnement"
    economie = "Économie"
    education = "Éducation"
    feminisme = "Féminisme"
    gaming = "Gaming"
    gastronomie = "Gastronomie"
    geographie = "Géographie"
    histoire = "Histoire"
    humour = "Humour"
    information = "Information"
    innovation = "Innovation"
    internet = "Internet"
    jeunesse = "Jeunesse"
    jeux = "Jeux"
    langues = "Langues"
    lgbt = "LGBTQIA+"
    litterature = "Littérature"
    loisirs = "Loisirs"
    medias = "Médias"
    musique = "Musique"
    pire_commu = "Pire Commu"
    politique = "Politique"
    religions = "Religions"
    sante = "Santé"
    sciences = "Sciences"
    sciences_sociales = "Sciences sociales"
    societe = "Société"
    solidarite = "Solidarité"
    sports = "Sports"
    technologies = "Technologies"
    television = "Télévision"
    travail = "Travail"
    twitch = "Twitch"
    vegetaux = "Végétaux"

    sans_categorie = "Sans catégorie"


def get_category(category: str) -> str:
    try:
        return CATEGORIES[category].value
    except KeyError:
        return "none"

HEADER = f"""
<!doctype html>
<html>
<head>
    <title>Pire Agenda</title>
    <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/x-icon" href="{root}/src/img/divers.png">
    <link href="{root}/src/style/style.css" media="screen" rel="stylesheet" type="text/css"/>
    <link href="{root}/src/style/categories.css" media="screen" rel="stylesheet" type="text/css"/>
    <link href="https://fonts.googleapis.com/css2?family=Titillium+Web:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="header">
        <div class="header-left" onclick="window.open('{root}/today', '_self')">
            <div class="header-title">
                Pire Agenda
            </div>
        </div>
        <nav class="header-nav">
            <label for="toggle">☰</label>
            <input type="checkbox" id="toggle">
            <div class="main_pages">
                <a href="{root}/filter/date">Par date</a>
                <a href="{root}/filter/categorie">Par catégorie</a>
                <a href="{root}/all">Liste entière</a>
            </div>
        </nav>
    </div>"""

# TODO : add by-title filter

FOOTER = f"""
    <div class="footer">
        <div class="footer-content">
            <p>Agenda des journées mondiales, internationales et bien d'autres. Le calendrier comprend aussi quelques dates et événements liés au stream francophone.</p>
        </div>
        <div class="footer-content">
            <p>Le site est encore en <a class="footer-link" href="https://github.com/BixGra/PireAgenda" target="_blank">plein développement (repo GitHub)</a> et je ne suis pas dev' web donc il y a pas mal de soucis à régler. Tout retour ou aide sont les bienvenus <a class="footer-link" href="https://twitter.com/babiilabilux" target="_blank">par message</a> !</p>
        </div>
        <div class="footer-content">
            <p>Images via <a class="footer-link" href="https://www.flaticon.com/" title="Flaticon" target="_blank">Freepik - Flaticon</a>.</p>
        </div>
    </div>
</body>
</html>"""

CARDS_CONTAINER = f"""
<div class="cards-container {{}}">
    <div class="cards-container-left">
        <div class="cards-container-label">
            <p>{{}}</p>
        </div>
    </div>
    <div class="cards">{{}}</div>
</div>"""

CARD = f"""
<div class="card" title="{{}}" onclick="window.open('{root}/events/{{}}', '_self')">
    <div class="card-header">
        <div class="card-title">{{}}</div>
        <div class="card-header-right">
            <img class="card-image" src="{root}/src/img/{{}}.png">
            <div class="card-date">
                <p>{{}}</p>
            </div>
        </div>
    </div>
    <div class="card-text">
        <p>{{}}</p>
    </div>
    <div class="card-bottom">
        {{}}
    </div>
</div>"""

SINGLE_CARD = f"""
<div class="card single-card" style="cursor: default;">
    <div class="card-header">
        <div class="card-title">{{}}</div>
        <div class="card-header-right">
            <img class="card-image" src="{root}/src/img/{{}}.png">
            <div class="card-date">
                <p>{{}}</p>
            </div>
        </div>
    </div>
    <div class="card-text">
        <p>{{}}</p>
    </div>
    <div class="card-bottom">
        {{}}
    </div>
</div>"""

NO_CARD = f"""
<div class="card single-card no-event" style="cursor: default;">
    <div class="card-header">
        <div class="card-title">Pas d'événement à cette date</div>
        <div class="card-header-right">
            <img class="card-image" src="{root}/src/img/divers.png">
            <div class="card-date">
                <p>{{}}</p>
            </div>
        </div>
    </div>
    <div class="card-text">
        <p>Il n'y a pas d'événement enregistré pour cette date.</p>
    </div>
</div>"""

TAGS_CONTAINER = f"""
<div class="card-tags">
    {{}}
</div>
"""

TAG = f"""
<div class="card-tag {{}}" title="" onclick="window.open('{root}/categorie/{{}}', '_self'); event.stopPropagation();">{{}}</div>
"""

ALL_CONTAINER = f"""
<div class="cards-container {{}}">
    <div class="cards-container-left">
        <div class="cards-container-label">
            <p>{{}}</p>
        </div>
    </div>
    <div class="cards">
        <div class="card single-card all-container">
            {{}}
        </div>
    </div>
</div>"""

ALL_ITEM = f"""
<div class="all-item">
    <a class="all-link" title="{{}}" href="{root}/events/{{}}">{{}}</a>
</div>
"""

FILTER_DATE = f"""
<div class="filter">
    <div class="filter-item">
        <div class="filter-item-child" id="title">
            <p>Rechercher des journées en filtrant par date</p>
        </div>
    </div>
    <div class="filter-item">
        <label for="month"></label>
        <select class="filter-item-child" id="month">
            <option value="1">Janvier</option>
            <option value="2">Février</option>
            <option value="3">Mars</option>
            <option value="4">Avril</option>
            <option value="5">Mai</option>
            <option value="6">Juin</option>
            <option value="7">Juillet</option>
            <option value="8">Août</option>
            <option value="9">Septembre</option>
            <option value="10">Octobre</option>
            <option value="11">Novembre</option>
            <option value="12">Decembre</option>
        </select>
        <label for="day"></label>
        <select class="filter-item-child" id="day">
        </select>
    </div>
    <div class="filter-item">
        <label for="search"></label>
        <button class="filter-item-child" id="search" root="{root}" onclick="window.open('{root}/date/01/01', '_self')">Chercher</button>
    </div>
    <script src="{root}/src/script/selector.js"></script>
</div>"""

SINGLE_CATEGORY = f"""
<div class="filter-item-child category {{}}" onclick="window.open('{root}/categorie/{{}}', '_self')">
    <div class="category-text">
        <p>{{}}</p>
    </div>
    <div class="category-right">
        <img class="category-image" src="{root}/src/img/{{}}.png">
    </div>
</div>"""

FILTER_CATEGORY = f"""
<div class="filter">
    <div class="filter-item categories">
        {"".join([SINGLE_CATEGORY.format(c.name, c.name, c.value, c.name) for c in CATEGORIES])}
    </div>
</div>"""
