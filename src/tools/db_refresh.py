import re
import sqlite3 as sl

import pandas as pd
from loguru import logger


def convert_google_sheet_url(url):
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'
    return re.sub(pattern, lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (
        f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv', url)


def check_cat1(cat) -> str:
    return cat if isinstance(cat, str) else "sans_categorie"


def check_cat(cat) -> str:
    return cat if isinstance(cat, str) else "none"


def db_refresh():
    logger.info("Refreshing DB")
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

    url = convert_google_sheet_url("https://docs.google.com/spreadsheets/d/161ygk8Gyjn4JXMcP_fSjTJB776P0uZUsG7K8TTCYYV4/edit#gid=0")
    logger.info("Downloading DB")
    df = pd.read_csv(url).dropna(subset=["id", "date", "nom", "description"])
    logger.info("Populating DB")
    agenda = [(int(row["id"]), row["date"], row["nom"], row["description"], check_cat1(row["categorie1"]), check_cat(row["categorie2"]), check_cat(row["categorie3"]), check_cat(row["lien"]), check_cat(row["titre_lien"])) for row in df.iloc]
    with con:
        con.executemany(sql_agenda, agenda)
    logger.info("DB refreshed")
