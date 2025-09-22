class Song():
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist

    def fetch_all_songs():
        """retrieves all song objects from the database"""
        cursor.execute("SELECT * FROM tunes")
        connection.commit()
        return cursor.fetchall()

    def insert_song(self):
        """inserts this song object into the tunes database"""
        cursor.execute(
            "INSERT OR IGNORE INTO tunes (title, artist, duration) VALUES (?, ?, ?)",
            (self.title, self.artist)
        )
        connection.commit()

    def delete_song(self, id=None):	
        """deletes a song by id or title from the database"""
        if id is not None and self.title is not None:
            cursor.execute(
                "DELETE FROM tunes WHERE ROWID = ? AND title = ?",
                (id, self.title)
            )
        elif id is not None:
            cursor.execute("DELETE FROM tunes WHERE ROWID = ?", (id,))
        elif title is not None:
            cursor.execute(
                "DELETE FROM tunes WHERE song_title = ?",
                (self.title,)
            )
        else:
            return
        connection.commit()