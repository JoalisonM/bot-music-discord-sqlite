from database.models.Playlist import Playlist
from database.db import db

class PlaylistRepo:

    @staticmethod
    def save(name):
        playlist = Playlist(name)
        db.session.add(playlist)
        db.session.commit()
        return playlist.toJson()

    @staticmethod
    def findPlaylistByName(playlistName):
        playlists = db.session.query(Playlist).filter(Playlist.name==playlistName).all()
        jsonplaylists = []
        for i in range(len(playlists)):
            jsonplaylists.append(playlists[i].toJson())
        return playlists

    @staticmethod
    def findAll():
        playlists = db.session.query(Playlist).all()
        jsonplaylists = []
        for i in range(len(playlists)):
            jsonplaylists.append(playlists[i].toJson())
        return jsonplaylists
