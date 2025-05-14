import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "honestybox.db"
SCHEMA_PATH = Path(__file__).parent.parent / "database" / "schema.sql"
SEED_PATH = Path(__file__).parent.parent / "database" / "seed_data.sql"

def reset_db():
    if DB_PATH.exists():
        DB_PATH.unlink()  # delete old DB

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Run schema
    with open(SCHEMA_PATH, "r") as f:
        cursor.executescript(f.read())

    # Seed initial data
    with open(SEED_PATH, "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database reset and seeded.")

if __name__ == "__main__":
    reset_db()

