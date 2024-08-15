import os
from enum import Enum

root = "/pireagenda" if "PIREAGENDAPROD" in os.environ else ""


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


HEADER = f"""
<!doctype html>
<html>
<head>
    <title>Pire Agenda</title>
    <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/x-icon" href="{root}/src/img/education.png">
    <link href="{root}/src/style/style.css" media="screen" rel="stylesheet" type="text/css"/>
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
            <p>Le site est encore en <a class="footer-link" href="https://github.com/BixGra/PireAgenda" target="_blank">plein développement (repo GitHub)</a> et je ne suis pas dev' web donc il y a pas mal de soucis à régler. Tout retour ou aide sont les bienvenus <a class="footer-link" href="https://twitter.com/babiilabilux">par message</a> !</p>
        </div>
        <div class="footer-content">
            <p>Images via <a class="footer-link" href="https://www.flaticon.com/free-icons/art" title="art icons">Freepik - Flaticon</a>.</p>
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
</div>"""

NO_CARD = f"""
<div class="card single-card no-event" style="cursor: default;">
    <div class="card-header">
        <div class="card-title">Pas d'événement à cette date</div>
        <div class="card-header-right">
            <img class="card-image" src="{root}/src/img/tmp.png">
            <div class="card-date">
                <p>{{}}</p>
            </div>
        </div>
    </div>
    <div class="card-text">
        <p>Il n'y a pas d'événement enregistré pour cette date.</p>
    </div>
</div>"""

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
<div class="filter-item-child category" onclick="window.open('{root}/categorie/{{}}', '_self')">
    <div class="category-text">
        <p>{{}}</p>
    </div>
    <div>
        <img class="category-image" src="{root}/src/img/{{}}.png">
    </div>
</div>"""

FILTER_CATEGORY = f"""
<div class="filter">
    <div class="filter-item">
        {"".join([SINGLE_CATEGORY.format(c.name, c.value, c.name) for c in CATEGORIES])}
    </div>
</div>"""
