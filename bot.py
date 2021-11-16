import discord
import discord.ext import commands

#sets bots prefix which commands the bot
client  = commands.Bot(command_prefix = '!')

#prepares bot and if ready prints message
@client.event
async def on_ready():
    print('Bot is ready to start!')
    
#When a member joins prints statement 
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')
    
# When a members leaves for any reason, prints message
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')
    
#Bot responds with message when using comand !hello
@client.command()
async def hello(ctx):
    await ctx.send("Hey, hope you're well!")


#runs the discord bot
client.run('YOUR DISCORD BOT TOKEN HERE') #Token is necessary for bot control
