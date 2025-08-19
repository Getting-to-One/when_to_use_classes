class Database():
    def __init__(self, path):
        self.connection = sqlite3.connect(path, check_same_thread=False)
        self.cursor = self.connection.cursor

    def fetch_database(self):
        """retrieves all song objects from the database"""
        self.cursor.execute("SELECT * FROM tunes")
        self.connection.commit()
        return self.cursor.fetchall()

    def insert_song(self, song: Song):
        """inserts a song into the tunes database"""
        self.cursor.execute(
            "INSERT OR IGNORE INTO tunes (title, artist) VALUES (?, ?)",
            song.get_data(),
        )
        self.connection.commit()

    def delete_song(self, title=None, id=None):
        """deletes a song by id or title from the database"""
        if id is not None and title is not None:
            self.cursor.execute(
                "DELETE FROM tunes WHERE ROWID = ? AND title = ?",
                (id, title)
            )
        elif id is not None:
            self.cursor.execute(
                "DELETE FROM tunes WHERE ROWID = ?", (id,)
            )
        elif title is not None:
            self.cursor.execute(
                "DELETE FROM tunes WHERE title = ?", (title,)
            )
        else:
            return
        self.connection.commit()

song_database = Database("db/tunes.db")