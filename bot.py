import discord
from discord import app_commands
import random

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"we have logged in as {self.user}.")
        
client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "test", description = "testing")
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Hello {name}! I was made with discrod.py", ephemeral = False)
    
@tree.command(name = "losuj", description = "losowanie")
async def self(interaction: discord.Interaction, ilość: int):
    a = 0
    help = []
    while a!=ilość:
        help.append(random.randint(1, 31)) 
        a = a + 1
    await interaction.response.send_message(f"Liczba to {help}", ephemeral = False)
    
client.run('ODM0ODE4OTM1NjkzMTE1NDEy.GGscZB.uwmrs_VZ3k1J_inIQmScOKv_y2TLuTHcwYpoWw')