from database.db import db

class Playlist(db.Model):

    __tablename__ = "playlist"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String)

    def __init__(self, name):
        self.name = name

    def toJson(self):
        return {
            "id":self.id,
            "name":self.name
        }