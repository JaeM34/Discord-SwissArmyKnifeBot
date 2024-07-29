#   ESTABLISH CONNECTION TO DISCORD
#   ESTABLISH CONNECTION WITH MONGODB
#   INITIALIZE ANY INTERNALIZED CLOCKS
#   BEGIN LOGIC LOOP
#   CREATE LOG
import pymongo
import dotenv
import discord

token = dotenv.get_key("discord_token")
client = discord.client(token)

class bot: 
    def run():
        print("hello")
        
