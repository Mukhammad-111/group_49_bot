import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            connection.execute("""
            CREATE TABLE IF NOT EXISTS reviews(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(200),
            date DATA,
            phone_number VARCHAR(200),
            rate INTEGER,
            extra_comments TEXT
            )
            """)


            connection.execute("""
            CREATE TABLE IF NOT EXISTS dishes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(200),
            price INTEGER,
            description TEXT,
            category TEXT,
            photo TEXT
            )
            """)


    def save_reviews(self, data: dict):
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                """ 
                        INSERT INTO reviews(name, date, phone_number, rate, extra_comments)
                        VALUES (?, ?, ?, ?, ?)
                    """,
              (data["name"], (data["date"]), data["phone_number"], data["rate"],
               data["extra_comments"])
                    )



    def save_dishes(self, data: dict):
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                """
                        INSERT INTO dishes(name, price, description, category, photo)
                        VALUES (?, ?, ?, ?, ?)
                    """,
              (data["name"], data["price"], data["description"], data["category"],
               data["photo"])
            )


    def get_dishes(self):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            result = connection.execute("SELECT * FROM dishes")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(row) for row in data]