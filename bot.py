import discord
import requests
from bs4 import BeautifulSoup
import time 
from discord.ext import commands
from discord.ext.commands import Bot
from random import randint
from random import choice

masiv = ['You bring light to my life                                         \n jk because im bot :D','A smile becomes you','I could talk to you all night long','Sry, but u will die soon ','Hmmm, i smell you have good mood :D','You are beautiful','Artur will fuck you','You are pretty' , 'You are gay', 'You are like a shit', 'U will get gf(bf) as soon as posible','You are peach ', 'You are looking so lovely', 'You make me feel happy ','I will help you , you so good','Sry, but you are dumb :(']



CORONA_WORLD = 'https://www.worldometers.info/coronavirus/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
def cheack_currency():
   full_page = requests.get(CORONA_WORLD,headers = headers)
   soup = BeautifulSoup(full_page.content, 'html.parser')
   
   convert = soup.findAll("span", {"data-precision": "data-value"})
   a = convert[0].text

Bot = commands.Bot(command_prefix= "^")

@Bot.event
async def on_ready():
    print("Im online")


@Bot.command()
async def Swed(ctx):
    await ctx.send(f"<@{273844890608336896}> is Cops Top1 player :?")

@Bot.command()
async def howlesbian(ctx):
    author = ctx.message.author
    await ctx.send(f"<@{author.id}> is {randint(0,101)}% lesbian")


@Bot.command()
@commands.has_permissions(administrator = True)
async def mute (ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name = "Muted")
    await member.add_roles(mute_role)
    await ctx.send("Muted")


@Bot.command()
async def howgay(ctx):
    author = ctx.message.author
    await ctx.send(f"<@{author.id}> is {randint(0,101)}% gay")


@Bot.command()
async def allabout(ctx):
    author = ctx.message.author
    await ctx.send(f"<@{author.id}> is {randint(0,101)}% gay")
    await ctx.send(f"<@{author.id}> накурений на  {randint(0,101)}% ")
    await ctx.send(f"<@{author.id}> your penis is  {randint(-5,30)} cm ")
    await ctx.send(f"<@{author.id}> is {randint(0,101)}%lesbian")
    await ctx.send(f"<@{author.id}>, {choice(masiv)}")

@Bot.command()
async def mems(ctx):
    await ctx.send("I dont have mems you gay smd")


@Bot.command()
async def howhigh(ctx):
    author = ctx.message.author
    await ctx.send(f"<@{author.id}> накурений на  {randint(0,101)}% ")


@Bot.command()
async def random(ctx):
    await ctx.send("Danylo pidor!!")

@Bot.command()
async def aboutme(ctx):
    author = ctx.message.author
    await ctx.send(f"<@{author.id}>, {choice(masiv)}")

@Bot.command()
async def sizeofpenis(ctx):
    author = ctx.message.author
    await ctx.send(f"<@{author.id}> your penis is  {randint(-5,30)} cm ")


@Bot.command()
async def coronaworld(ctx):
   full_page = requests.get(CORONA_WORLD,headers = headers)
   soup = BeautifulSoup(full_page.content, 'html.parser')
   
   convert = soup.findAll("span", {"style": "color:#aaa"})
   a = convert[0].text
   await ctx.send(f"Covid 19 cases (in world) at the moment - {a}")


@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Hello <@{author.id}> , i was made by Nazarko :D ")


Bot.run('NzAyMDkwNDg3MTA3OTQ0NDg5.Xp6-uA.pDN40mvOZzHe27LXQCooDsHFQCE')
