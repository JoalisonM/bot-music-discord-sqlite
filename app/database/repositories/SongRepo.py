from database.models.Song import Song
from database.db import db

class SongRepo:

    @staticmethod
    def save(name, playlistName):
        song = Song(name, playlistName)
        db.session.add(song)
        db.session.commit()
        return song.toJson()

    @staticmethod
    def findByPlaylist(playlistName):
        songs = db.session.query(Song).filter(Song.playlistName==playlistName).all()
        jsonsongs = []
        for i in range(len(songs)):
            jsonsongs.append(songs[i].toJson())
        return jsonsongs

    @staticmethod
    def findAll():
        songs = db.session.query(Song).all()
        jsonsongs = []
        for i in range(len(songs)):
            jsonsongs.append(songs[i].toJson())
        return jsonsongs
