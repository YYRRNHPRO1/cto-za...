import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
       for attachment in ctx.message.attachments:
           file_name = attachment.filename
           file_url = attachment.url
           await attachment.save(f'{attachment.filename}')
           result = get_class(model="keras_model.h5", labels="labels.txt", image=f'{attachment.filename}')
           await ctx.send(result)
           if result[0] == 'Голубь':
               print('+')
           else:
               print('-')
    else:
        await ctx.send('Вы забыли загрузить картинку')
        
bot.run("MTIxMzc4MDY3NTk3NTU3NzczMQ.GgVxYe.CR6nJXUk_JyjIjMvSLpGxrGzrg8D0qPLmSJ5GE")