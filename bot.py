#   ESTABLISH CONNECTION TO DISCORD
#   ESTABLISH CONNECTION WITH MONGODB
#   INITIALIZE ANY INTERNALIZED CLOCKS
#   BEGIN LOGIC LOOP
#   CREATE LOG
import pymongo
import dotenv
import discord
import os

dotenv.load_dotenv()

class bot:
    token = os.environ.get("discord_token")
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    def run(self):
        self.client.run(token=self.token)
        print("Connection established")
        
