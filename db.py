import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (Id INTEGER PRIMARY KEY, Item text, Quality INTEGER, Quantity INTEGER, Price FLOAT)" )
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, Item, Quality, Quanity, Price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)", (Item, Quality, Quanity, Price))
        self.conn.commit()

    def remove(self, Id):
        self.cur.execute("DELETE FROM parts WHERE Id=?", (Id,))
        self.conn.commit()

    def update(self, Id, Item, Quality, Quanity, Price):
        self.cur.execute("UPDATE parts SET part = ?, Item = ?, Quality = ?, Quantiy = ?, Price= ? WHERE Id = ?", (Item, Quality, Quanity, Price, Id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#db = Database('store.db')
#db.insert("Brown Rice", "1","2","180")
#db.insert("Apple", "1","2","180")
#db.insert("Orange", "1","2","180")
#db.insert("Mango", "1","2","180")


             