import os

from dotenv import load_dotenv

load_dotenv()

# Application
MAXIMUM_CONFIRMATION_CHECKS = 20

# thenewboston
BANK_IP = '54.183.16.194'
BANK_PROTOCOL = 'http'
BOT_ACCOUNT_NUMBER = '598428d3a9df5423aab3e593b5d1b5f056b9fa353607fccb1aa76385cf233851'

# Discord
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Mongo
MONGO_DB_NAME = 'discord-db'
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
