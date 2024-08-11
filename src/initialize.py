import re
import sqlite3 as sl

import pandas as pd


con = sl.connect(f"./src/data/pireagenda.db")

# Journees
with con:
    con.execute("""
            DROP TABLE AGENDA;
        """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS AGENDA (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            title TEXT,
            description TEXT,
            category TEXT
        );
    """)

sql_agenda = """INSERT INTO AGENDA (id, date, title, description, category) values(?, ?, ?, ?, ?)"""


def convert_google_sheet_url(url):
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'
    return re.sub(pattern, lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv', url)


url = convert_google_sheet_url("https://docs.google.com/spreadsheets/d/161ygk8Gyjn4JXMcP_fSjTJB776P0uZUsG7K8TTCYYV4/edit#gid=0")
# url = convert_google_sheet_url("https://docs.google.com/spreadsheets/d/161ygk8Gyjn4JXMcP_fSjTJB776P0uZUsG7K8TTCYYV4/edit#gid=885544863")

df = pd.read_csv(url)

agenda = [(int(row[0]), row[1], row[2], row[3], row[4]) for row in df.iloc]
with con:
    con.executemany(sql_agenda, agenda)
