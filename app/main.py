import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from config.loadYML import botPrefix
from services.botService import BotMusic
from flask import Flask
from database.models.Playlist import Playlist
from database.models.Song import Song
from database.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
app.app_context().push()

with app.app_context():
    db.create_all()
    
load_dotenv()

tokenDiscord = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(botPrefix, intents=intents)

bot.add_cog(BotMusic(bot))

print("INDO")
bot.run(tokenDiscord)