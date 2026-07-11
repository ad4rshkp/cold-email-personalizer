import sqlite3


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


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
