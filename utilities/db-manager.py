# Run from root directory: python -i utilities/db-manager.py
import sqlite3
import os

# Define the path to the database file in the data directory relative to this script
DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
DB_PATH = os.path.join(DB_DIR, 'database.db')

def get_connection():
    """Returns a connection to the SQLite database."""
    # Ensure the data directory exists just in case
    os.makedirs(DB_DIR, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def test_database():
    """Tests the SQLite database."""
    print(f"Connecting to database at {DB_PATH}...")
    conn = get_connection()
    cursor = conn.cursor()
    conn.commit()
    conn.close()
    print("Database connection successful.")

if __name__ == '__main__':
    print("db-manager loaded.")
    print("Run test_database() to test the database.")
