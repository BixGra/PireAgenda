import os

root = "/pireagenda" if "PIREAGENDAPROD" in os.environ else ""

HEADER = f"""
<!doctype html>
<html>
<head>
    <title>Pire Agenda</title>
    <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
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
            <p>Créé par <a class="footer-link" href="https://twitter.com/babiilabilux">Babi'</a> avec la Pire Commu.</p>
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
<div class="card" onclick="onclick="window.open('{root}/events/{{}}', '_self')">
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
<div class="card" style="cursor: default;">
    <div class="card-header">
        <div class="card-title">Pas d'événement ce jour là</div>
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
        <script src="{root}/src/script/selector.js"></script>
    </div>
    <div class="filter-item">
        <label for="search"></label>
        <button class="filter-item-child" id="search" root="{root}" onclick="window.open('{root}/date/01/01', '_self')">Chercher</button>
    </div>
</div>"""

FILTER_CATEGORY = f"""
<div class="filter">
    <div class="filter-item">
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/angledroit', '_self')">
            <p>AngleDroit</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/art', '_self')">
            <p>Art</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/cinema', '_self')">
            <p>Cinéma</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/divers', '_self')">
            <p>Divers</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/education', '_self')">
            <p>Education</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/environnement', '_self')">
            <p>Environnement</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/feminisme', '_self')">
            <p>Féminisme</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/gastronomie', '_self')">
            <p>Gastronomie</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/geographie', '_self')">
            <p>Géographie</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/histoire', '_self')">
            <p>Histoire</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/internet', '_self')">
            <p>Internet</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/jeux', '_self')">
            <p>Jeux</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/langues', '_self')">
            <p>Langues</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/litterature', '_self')">
            <p>Littérature</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/media', '_self')">
            <p>Média</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/musique', '_self')">
            <p>Musique</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/nature', '_self')">
            <p>Nature</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/sante', '_self')">
            <p>Santé</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/sciences', '_self')">
            <p>Sciences</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/societe', '_self')">
            <p>Société</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('{root}/categorie/sports', '_self')">
            <p>Sports</p>
        </div>
    </div>
</div>"""
