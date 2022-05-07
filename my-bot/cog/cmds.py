import discord
import time
from discord.ext import commands
import datetime
from datetime import time
import time
class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def now_time(self,ctx):
        t = datetime.datetime.now()
        now_time = t.strftime("%H:%M:%S")
        embed=discord.Embed(title="現在的時間是：", color=0x00ffff)
        embed.add_field(name=now_time, value="now_time", inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def today(self,ctx):
        t = datetime.datetime.now()
        now_time = t.strftime("%d/%m/%Y")
        embed=discord.Embed(title="今天是：", color=0x00ffff)
        embed.add_field(name=now_time, value="today", inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!'+'\n'+f'**{round(self.bot.latency*1000)}**ms')
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("ERROR1[沒有此指令]")
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("ERROR2[遺失參數]")
    @commands.command()
    async def nitro(self, ctx):
        await ctx.send('https://discordgift.site/qOmE5ajYL6mjkob')
        time.sleep(2)
        await ctx.send('||~~絕對不是rick roll~~||')
        time.sleep(5)
        await ctx.send('||rick rolled||')
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="小瓶的機器人指令幫助", color=0x00ffff)
        embed.add_field(name="say", value="說出東西", inline=False)
        embed.add_field(name="clean", value="清理訊息", inline=False)
        embed.add_field(name="kick", value="踢出別人", inline=False)
        embed.add_field(name="ban", value="封禁別人", inline=False)
        embed.add_field(name="ping", value="顯示我的延遲", inline=False)
        embed.add_field(name="info", value="顯示我的資訊", inline=False)
        embed.add_field(name="invite", value="顯示我的邀請連結", inline=False)
        #embed.add_field(name="music_help", value="音樂指令幫助", inline=False)
        embed.add_field(name="now_time", value="顯示現在的時間", inline=False)
        embed.add_field(name="today", value="顯示現在的日期", inline=False)
        embed.add_field(name="send_dm [@member] [msg]", value="發送私人訊息", inline=False)
        embed.set_footer(text="help")
        await ctx.send(embed=embed)
        print("help:")
        print(ctx.author.name)
        print("=========================")
#    @commands.command()
#    async def music_help(self, ctx):
#        embed=discord.Embed(title="小瓶的機器人音樂指令幫助", color=0x00ffff)
#        embed.add_field(name="play [連結]/名字", value="播放音樂", inline=False)
#        embed.add_field(name="stop/st", value="暫停播放", inline=False)
#        embed.add_field(name="resume", value="繼續播放", inline=False)
#        embed.add_field(name="join/j", value="加入語音頻道", inline=False)
#        embed.add_field(name="leave/dc", value="離開語音頻道", inline=False)
#        embed.add_field(name="clear/c", value="清除播放清單裏的歌曲", inline=False)
#        embed.add_field(name="list/l", value="顯示播放清單", inline=False)
#        embed.add_field(name="skip/s", value="跳過目前播放的歌曲", inline=False)
#        await ctx.send(embed=embed)
    @commands.command()
    async def say(self, ctx, * ,msg):
        embed=discord.Embed(title=msg, color=0x00ffff)
        await ctx.send(embed=embed)
        time.sleep(1)
        await ctx.message.delete()
        print("say:")
        print(msg)
        print(ctx.author.neme)
        print("=========================")
    @commands.command()
    async def invite(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        time.sleep(1)
        await ctx.channel.purge(limit=1)
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=841267762316050462&permissions=8&scope=bot")
        print("invite:")
        print(ctx.author.name)
        print("=========================")
    @commands.command()
    async def send_dm(self, ctx, member: discord.Member, *, content):
        await ctx.send("<a:loading:966882297464897578> Loading...")
        channel = await member.create_dm()
        embed=discord.Embed(title="by"+ctx.author.display_name+"("+ctx.author.name+")", color=0x00ffff)
        embed.add_field(name=content, value="send_dm", inline=False)
        await channel.send(embed=embed)
        time.sleep(0.5)
        await ctx.channel.purge(limit=1)
        time.sleep(0.5)
        print("send dm")
        print(ctx.author.name)
        print(content)
        print("=========================")
        await ctx.send("<a:done:843856167658586112> done!")
        time.sleep(5)
        await ctx.channel.purge(limit=2)
    @commands.command()
    async def info(self, ctx):
        embed=discord.Embed(title="small bottle bot 資訊", url="http://discord.gg/wQG2cwSDYs", description="製作者:0123#9817", color=0x00ffff)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/fb/Glass_Bottle_JE2_BE2.png/revision/latest/scale-to-width-down/160?cb=20200523234146")
        embed.add_field(name="我的ID", value="841267762316050462", inline=False)
        embed.add_field(name="0123#9817的ID", value="733616286734745650", inline=True)
        embed.add_field(name="my web", value="http://jp-tyo-iij-1.natfrp.cloud:49515/", inline=False)
        embed.set_footer(text="info")
        await ctx.send(embed=embed)
        print("info:")
        print(ctx.author.name)
        print("=========================")
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, num: int):
        if num == ('0'):
            await ctx.send("error2")
        else:
            await ctx.channel.purge(limit=1)
            time.sleep(1)
            await ctx.channel.purge(limit=num)
            print("clean:")
            print(ctx.author.name)
            print(num)
            print("=========================")
    @clean.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("你沒有刪除訊息的權限")
            print("clean error:")
            print(ctx.author.name)
            print("=========================")
    
    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        print(member)
        time.sleep(2)
        await member.ban(reason=reason)
        time.sleep(2)
        await ctx.send(member.display_name + " 已被封鎖!")
        time.sleep(5)
        await ctx.channel.purge(limit=1)
        print("ban:")
        print(ctx.author.name)
        print(member)
        print("=========================")
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member):
        print(member)
        time.sleep(2)
        await member.kick()
        time.sleep(2)
        await ctx.send(member.display_name + " 已被踢出!")
        time.sleep(5)
        await ctx.channel.purge(limit=1)
        print("kick:")
        print(ctx.author.name)
        print(member)
        print("=========================")
    @commands.command()
    async def set_web_on(self, ctx,):
        if ctx.author.id == 733616286734745650:
            await ctx.channel.purge(limit=1)
            embed=discord.Embed(title="網頁伺服器狀態",color=0x00ffff)
            embed.add_field(name="狀態", value="on", inline=False)
            embed.add_field(name="link", value="link", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("you can't do it!")
    @commands.command()
    async def set_web_off(self, ctx,):
        if ctx.author.id == 733616286734745650:
            await ctx.channel.purge(limit=1)
            embed=discord.Embed(title="網頁伺服器狀態",color=0x00ffff)
            embed.add_field(name="狀態", value="off", inline=False)
            embed.add_field(name="link", value="link", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("you can't do it!")
    @commands.command()
    async def set_mc_on(self, ctx,):
        if ctx.author.id == 733616286734745650:
            await ctx.channel.purge(limit=1)
            embed=discord.Embed(title="minecraft伺服器狀態",color=0x00ffff)
            embed.add_field(name="狀態", value="on", inline=False)
            embed.add_field(name="伺服器位址", value="link", inline=False)
            embed.add_field(name="埠", value="17475", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("you can't do it!")
    @commands.command()
    async def set_mc_off(self, ctx,):
        if ctx.author.id == 733616286734745650:
            await ctx.channel.purge(limit=1)
            embed=discord.Embed(title="minecraft伺服器狀態",color=0x00ffff)
            embed.add_field(name="狀態", value="off", inline=False)
            embed.add_field(name="伺服器位址", value="link", inline=False)
            embed.add_field(name="埠", value="17475", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("you can't do it!")



def setup(bot):
    bot.add_cog(Main(bot))