from database.db import db

class Song(db.Model):

    __tablename__ = "song"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String)
    playlistName = db.Column("playlist_name" , db.ForeignKey("playlist.name"))

    def __init__(self, name, playlistName):
        self.name = name
        self.playlistName = playlistName

    def toJson(self):
        return {
            "id":self.id,
            "name":self.name,
            "playlistName":self.playlistName
        }