import sqlite3

connection = sqlite3.connect(
    "orqora.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS traces (
    trace_id TEXT PRIMARY KEY,
    agent TEXT,
    task TEXT,
    start_time TEXT,
    end_time TEXT,
    duration_seconds REAL,
    output TEXT
)
""")

connection.commit()
