connection = sqlite3.connect("db/tunes.db", check_same_thread=False)
cursor = connection.cursor()

class Database():
    def fetch_all_songs():
        """retrieves all song objects from the database"""
        cursor.execute("SELECT * FROM tunes")
        connection.commit()
        return cursor.fetchall()

    def insert_song(song: Song):
        """inserts a song into the tunes database"""
        cursor.execute(
            "INSERT OR IGNORE INTO tunes (title, artist) VALUES (?, ?)",
            song.get_song_data(),
        )
        connection.commit()

    def delete_song(title=None, id=None):
        """deletes a song by id or title from the database"""
        if id is not None and title is not None:
            cursor.execute(
                "DELETE FROM tunes WHERE ROWID = ? AND title = ?",
                (id, title)
            )
        elif id is not None:
            cursor.execute("DELETE FROM tunes WHERE ROWID = ?", (id,))
        elif title is not None:
            cursor.execute(
                "DELETE FROM tunes WHERE song_title = ?",
                (title,)
            )
        else:
            return
        connection.commit()