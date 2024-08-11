HEADER = """
<!doctype html>
<html>
<head>
    <title>Pire Agenda</title>
    <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
    <link href="/src/style/style.css" media="screen" rel="stylesheet" type="text/css"/>
    <link href="https://fonts.googleapis.com/css2?family=Titillium+Web:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="header">
        <div class="header-left" onclick="window.open('/today', '_self')">
            <div class="header-title">
                Pire Agenda
            </div>
        </div>
        <nav class="header-nav">
            <label for="toggle">☰</label>
            <input type="checkbox" id="toggle">
            <div class="main_pages">
                <a href="/filter/date">Par date</a>
                <a href="/filter/categorie">Par catégorie</a>
            </div>
        </nav>
    </div>"""

# TODO : add by-title filter

FOOTER = """
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

CARDS_CONTAINER = """
<div class="cards-container {}">
    <div class="cards-container-left">
        <div class="cards-container-label">
            <p>{}</p>
        </div>
    </div>
    <div class="cards">{}</div>
</div>"""

CARD = """
<div class="card" onclick="onclick="window.open('/events/{}', '_self')">
    <div class="card-header">
        <div class="card-title">{}</div>
        <div class="card-header-right">
            <img class="card-image" src="/src/img/{}.png">
            <div class="card-date">
                <p>{}</p>
            </div>
        </div>
    </div>
    <div class="card-text">
        <p>{}</p>
    </div>
</div>"""

SINGLE_CARD = """
<div class="card single-card" style="cursor: default;">
    <div class="card-header">
        <div class="card-title">{}</div>
        <div class="card-header-right">
            <img class="card-image" src="/src/img/{}.png">
            <div class="card-date">
                <p>{}</p>
            </div>
        </div>
    </div>
    <div class="card-text">
        <p>{}</p>
    </div>
</div>"""

NO_CARD = """
<div class="card" style="cursor: default;">
    <div class="card-header">
        <div class="card-title">Pas d'événement ce jour là</div>
        <div class="card-header-right">
            <img class="card-image" src="/src/img/tmp.png">
            <div class="card-date">
                <p>{}</p>
            </div>
        </div>
    </div>
    <div class="card-text">
        <p>Il n'y a pas d'événement enregistré pour cette date.</p>
    </div>
</div>"""

FILTER_DATE = """
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
        <script src="/src/script/selector.js"></script>
    </div>
    <div class="filter-item">
        <label for="search"></label>
        <button class="filter-item-child" id="search" onclick="window.open('/date/01/01', '_self')">Chercher</button>
    </div>
</div>"""

FILTER_CATEGORY = """
<div class="filter">
    <div class="filter-item">
        <div class="filter-item-child category" onclick="window.open('/categorie/angledroit', '_self')">
            <p>AngleDroit</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/art', '_self')">
            <p>Art</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/cinema', '_self')">
            <p>Cinema</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/divers', '_self')">
            <p>Divers</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/geographie', '_self')">
            <p>Geographie</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/histoire', '_self')">
            <p>Histoire</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/jeux', '_self')">
            <p>Jeux</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/Langues', '_self')">
            <p>Langues</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/musique', '_self')">
            <p>Musique</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/sciences', '_self')">
            <p>Sciences</p>
        </div>
        <div class="filter-item-child category" onclick="window.open('/categorie/sports', '_self')">
            <p>Sports</p>
        </div>
    </div>
</div>"""
