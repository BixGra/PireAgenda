import re
import sqlite3 as sl

import numpy as np
import pandas as pd
from matplotlib import colormaps

from tools.html_base import CATEGORIES, root

con = sl.connect(f"./src/data/pireagenda.db")

# Journees
with con:
    con.execute("""
            DROP TABLE IF EXISTS AGENDA;
        """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS AGENDA (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            title TEXT,
            description TEXT,
            category1 TEXT DEFAULT 'sans_categorie',
            category2 TEXT DEFAULT 'none',
            category3 TEXT DEFAULT 'none',
            link TEXT DEFAULT 'none',
            link_title TEXT DEFAULT 'none'
        );
    """)

sql_agenda = """INSERT INTO AGENDA (id, date, title, description, category1, category2, category3, link, link_title) values(?, ?, ?, ?, ?, ?, ?, ?, ?)"""


def convert_google_sheet_url(url):
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'
    return re.sub(pattern, lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv', url)


url = convert_google_sheet_url("https://docs.google.com/spreadsheets/d/161ygk8Gyjn4JXMcP_fSjTJB776P0uZUsG7K8TTCYYV4/edit#gid=0")

df = pd.read_csv(url)

def check_cat1(cat) -> str:
    return cat if isinstance(cat, str) else "sans_categorie"


def check_cat(cat) -> str:
    return cat if isinstance(cat, str) else "none"


agenda = [(int(row["id"]), row["date"], row["nom"], row["description"], check_cat1(row["categorie1"]), check_cat(row["categorie2"]), check_cat(row["categorie3"]), check_cat(row["lien"]), check_cat(row["titre_lien"])) for row in df.iloc]
with con:
    con.executemany(sql_agenda, agenda)


cmap = colormaps["hsv"]
gradient = np.linspace(0, 1, len(CATEGORIES))


def to_256(value: float) -> int:
    return int(value*255)


def to_256_tint_1(value: float) -> int:
    return int((value + (1-value)/2)*255)


def to_256_tint_2(value: float) -> int:
    return int((value + 3*(1-value)/4)*255)


with open("./src/style/categories.css", "w") as f:
    f.write(f"""body {{
    background-image: url("{root}/src/img/background.png");
    background-size: 128px;
}}
""")
    for g, category in zip(cmap(gradient), CATEGORIES):
        if category.name == "angledroit":
            pass
        else:
            f.write(f"""
.{category.name} {{
    background: {("#%02x%02x%02x" % (to_256_tint_1(g[0]), to_256_tint_1(g[1]), to_256_tint_1(g[2]))).replace("-", "")};
}}

.{category.name}:hover {{
    background: {("#%02x%02x%02x" % (to_256_tint_2(g[0]), to_256_tint_2(g[1]), to_256_tint_2(g[2]))).replace("-", "")};
}}""")
