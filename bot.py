import discord
import discord.ext import commands
import random

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
    await ctx.send(f"Hey, hope you're well {ctx.author.mention}")
    

#joke command tells joke to user from array    
@client.command(name="joke", aliases=["getjoke" , 'jokes'])
async def joke(ctx):
    jokes = ['What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.', 'Did you hear about the first restaurant to open on the moon? It had great food, but no atmosphere.', 'Do you want to hear a construction joke? Sorry, I’m still working on it.', 'What does a nosey pepper do? It gets jalapeño business. ']
    await ctx.send(f'{random.choice(jokes)}')


#runs the discord bot
client.run('YOUR DISCORD BOT TOKEN HERE') #Token is necessary for bot control
