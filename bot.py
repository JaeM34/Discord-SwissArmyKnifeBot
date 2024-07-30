#   ESTABLISH CONNECTION TO DISCORD
#   ESTABLISH CONNECTION WITH MONGODB
#   INITIALIZE ANY INTERNALIZED CLOCKS
#   BEGIN LOGIC LOOP
#   CREATE LOG
import pymongo
import dotenv
import discord
from discord import app_commands
import os

dotenv.load_dotenv()

class bot:
    token = os.environ.get("discord_token")
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    commands = discord.app_commands.CommandTree(client)

    #   Functions to run on first initialization of bot
    def run(self):
        self.client.run(token=self.token)
        print("Connection established")

    #   Functions to run on member join guild
    async def on_member_join(self, member):
        guild_id = member.guild.id
        self.grant_role(member=member)

    @commands.command(
            name="default role"
            description="Sets default role of new members in a guild"
            help="Sets the default role to be given to new users. Default is None."
    )
    async def default_role(interaction):
        #   Sets default role_id within the database
        print("Hi")

    # Autorole Bot Functions
    async def grant_role(self, member):
        #   Get role ID from database
        role_id = ""
        member.add_roles(role_id, "Autorole granted. Reason: joined server.")
        print("Added role_id " + role_id + " to user_id " + member.id + " with guild_id " + member.guild.id)