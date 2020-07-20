import sqlite3 as sql


class DBCharacter:

    def __init__(self, pinyin: str, character: str, german: str):
        self.pinyin = pinyin
        self.character = character
        self.german = german


DB_PATH = '/database/database.db'


def init_database() -> None:
    with sql.connect(DB_PATH) as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS "characters" (
            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "pinyin"	TEXT NOT NULL,
            "character"	TEXT NOT NULL UNIQUE,
            "german"	TEXT NOT NULL)
        """)


def add_character(entry: DBCharacter) -> None:
    with sql.connect(DB_PATH) as db:
        cursor = db.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO characters(pinyin, character, german)  VALUES(?, ?, ?)
        """, (entry.pinyin, entry.character, entry.german))
        db.commit()


def get_all_characters() -> list:
    with sql.connect(DB_PATH) as db:
        cursor = db.cursor()
        cursor.execute("""
            SELECT * FROM characters 
        """)
        all_characters = cursor.fetchall()
        db.commit()
        return all_characters
