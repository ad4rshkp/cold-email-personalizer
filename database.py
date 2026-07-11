import sqlite3
import pandas as pd


def get_all_leads_as_dataframe():
    conn = sqlite3.connect("data/leads.db")
    df = pd.read_sql_query("SELECT * FROM leads", conn)
    conn.close()
    return df


def init_db():
    conn = sqlite3.connect("data/leads.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            company TEXT,
            title TEXT,
            website TEXT,
            email_opener TEXT,
            lead_score TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_lead(lead):
    conn = sqlite3.connect("data/leads.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO leads (name, company, title, website, email_opener, lead_score)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        lead["name"],
        lead["company"],
        lead["title"],
        lead["website"],
        lead["email_opener"],
        lead["lead_score"]
    ))

    conn.commit()
    conn.close()


def view_all_leads():
    conn = sqlite3.connect("data/leads.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leads")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    view_all_leads()
