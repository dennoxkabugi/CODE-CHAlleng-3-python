# database.py

import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('concerts.db')
connection.row_factory = sqlite3.Row  # This will allow us to get dict-like row objects
cursor = connection.cursor()

# Function to initialize the database schema
def initialize_db():
    with open('schema.sql', 'r') as schema_file:
        schema = schema_file.read()
    cursor.executescript(schema)
    connection.commit()

# Concert Methods
def get_band_for_concert(concert_id):
    query = """
    SELECT bands.* FROM bands
    JOIN concerts ON concerts.band_id = bands.id
    WHERE concerts.id = ?
    """
    cursor.execute(query, (concert_id,))
    return cursor.fetchone()

def get_venue_for_concert(concert_id):
    query = """
    SELECT venues.* FROM venues
    JOIN concerts ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """
    cursor.execute(query, (concert_id,))