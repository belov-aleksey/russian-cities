import sqlite3
import json


# 1. Reading JSON
with open("russian-cities.json", "r", encoding="utf-8") as f:
    cities_data = json.load(f)

# 2. Connecting to SQLite
conn = sqlite3.connect("russian_cities.db")
cursor = conn.cursor()

# 3. Creating table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject TEXT,
        district TEXT,
        population INTEGER,
        lat REAL NOT NULL,
        lon REAL NOT NULL
    )
""")

# 4. Inserting data
for city in cities_data:
    cursor.execute(
        "INSERT INTO cities (name, subject, district, population, lat, lon) VALUES (?, ?, ?, ?, ?, ?)",
        (
            city["name"],
            city["subject"],
            city["district"],
            city["population"],
            float(city["coords"]["lat"]),
            float(city["coords"]["lon"]),
        ),
    )

# 5. Saving changes and closing connection
conn.commit()
conn.close()

print("Database has created")