import discord
from discord.ext import commands
import time
import asyncio
from discord.ext.commands.bot import Bot
import os
import datetime
bot = commands.Bot(command_prefix='s ', help_command=None)
#client = discord.Client()

#ban

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(name = "help command: s help"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)-1}個伺服器"))
        await asyncio.sleep(60)
@bot.event
async def on_ready():
    print("=========================")
    print(">>>>>bot is online!<<<<<")
    bot.loop.create_task(status_task())
    time.sleep(1)
    print(bot.user.name)
    time.sleep(1)
    print(bot.user.id)
    time.sleep(1)
    print(f'{round(bot.latency*1000)} (ms)')
    print("=========================")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if not message.author.id == (1):
        if message.channel.id == (3):
            if not message.author.display_name == message.author.name:
                print("1")
                embed=discord.Embed(title="from: "+message.guild.name, description="by: "+message.author.display_name+"#"+message.author.discriminator, color=0x00ffff)
                embed.add_field(name=message.content, value="by: "+message.author.name+"#"+message.author.discriminator, inline=False)
                channel = bot.get_channel(2)
                await channel.send(embed=embed)
            if message.author.display_name == message.author.name:
                print("2")
                embed=discord.Embed(title="from: "+message.guild.name, description="by: "+message.author.display_name+"#"+message.author.discriminator, color=0x00ffff)
                embed.add_field(name=message.content, value=".", inline=False)
                channel = bot.get_channel(2)
                await channel.send(embed=embed)
            print("跨服聊天:")
            print(message.guild.name)
            print(message.author.name)
            print(message.content)
            t = datetime.datetime.now()
            now_time = t.strftime("%d/%m(%H:%M)")
            print(now_time)
            print("=========================")
    if not message.author.id == (1):
        if message.channel.id == (2):
            if not message.author.display_name == message.author.name:
                print("1")
                embed=discord.Embed(title="from: "+message.guild.name, description="by: "+message.author.display_name+"#"+message.author.discriminator, color=0x00ffff)
                embed.add_field(name=message.content, value="by: "+message.author.name+"#"+message.author.discriminator, inline=False)
                channel = bot.get_channel(3)
                await channel.send(embed=embed)
            if message.author.display_name == message.author.name:
                print("2")
                embed=discord.Embed(title="from: "+message.guild.name, description="by: "+message.author.display_name+"#"+message.author.discriminator, color=0x00ffff)
                embed.add_field(name=message.content, value=".", inline=False)
                channel = bot.get_channel(3)
                await channel.send(embed=embed)
            print("跨服聊天:")
            print(message.guild.name)
            print(message.author.name)
            print(message.content)
            t = datetime.datetime.now()
            now_time = t.strftime("%d/%m(%H:%M)")
            print(now_time)
            print("=========================")
    if message.content == "淦":
        await message.channel.send('你知道嗎 淦是水流進船裡的意思 所以如果當年鐵達尼號上有中國人 他們就會説 淦淦淦淦淦！')
    if message.content == ('hi'):
        await message.channel.send('hi你好我是~~智障機器人~~')
        
for Filename in os.listdir('./cog'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cog.{Filename[:-3]}')
if '__main__' == __name__:
    bot.run('tokennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')