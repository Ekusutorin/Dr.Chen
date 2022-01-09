import discord
from discord.ext import commands
import requests
import json
from keep_alive.py import keep_alive

bot = commands.Bot(command_prefix=';')
client = commands.Bot(command_prefix=';')



# Cursed
def get_cursed():
    response = requests.get('https://cursedimg.herokuapp.com/api')
    json_data = json.loads(response.content)
    cursed = json_data['image']
    return (cursed)
# NSFW Waifu
def get_waifu():
    response = requests.get('https://api.waifu.pics/nsfw/waifu')
    json_data = json.loads(response.content)
    waifu = json_data['url']
    return (waifu)
# NSFW Neko
def get_neko():
    response = requests.get('https://api.waifu.pics/nsfw/neko')
    json_data = json.loads(response.content)
    neko = json_data['url']
    return (neko)
# NSFW Trap
def get_trap():
    response = requests.get('https://api.waifu.pics/nsfw/trap')
    json_data = json.loads(response.content)
    trap = json_data['url']
    return (trap)
# NSFW BJ
def get_bj():
    response = requests.get('https://api.waifu.pics/nsfw/blowjob')
    json_data = json.loads(response.content)
    bj = json_data['url']
    return (bj)
# Sfw Waifu 
def get_wife():
    response = requests.get('https://api.waifu.pics/sfw/waifu')
    json_data = json.loads(response.content)
    wife = json_data['url']
    return (wife)
# Start Up
@bot.event
async def on_ready():
    print('We have logged in and have access to {0.user}'.format(bot))
    print('---------------------------------------------------------')
    print('Welcome Eku,')
    print('Welcome Drake Roblox...')
    print('--------------------')
    print('System analysis completed')
    print('--------------------------')
    print('Everything is in check')
    print('---------------------')
    print('Black coffee is on the table if you need it :)')
    print('----------------------------------------------')

#Zhaddy Chen Music Section
@bot.command()
async def join(ctx: commands.Context):
    print("Audio Section Working")
    for vc in bot.voice_clients:
        await vc.disconnect(force=True)
    await ctx.author.voice.channel.connect()
    await ctx.send("Mann Im Connected")

@bot.command(pass_context=True)
async def yt(ctx, url):
      author = ctx.message.author
      voice_channel = author.voice_channel
      vc = await ctx.author.voice.channel.connect()
      player = await vc.create_ytdl_player(url)
      player.start()


@bot.command()
async def leave(ctx: commands.Context):
    print("Sup")
    for vc in bot.voice_clients:
        await vc.leave(force = True)
    await ctx.author.voice.channel.disconnect()
    await ctx.send('Im out that Bitch')
# Clear Command
@bot.command()
async def clear(ctx, amount=5):
				await ctx.message.delete()
				await ctx.channel.purge(limit=amount)
#Spam Command 
@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): 
        await ctx.send(message) 

# Commands
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

#Fuck you
    if message.content.startswith(';fuck you'):
        await message.channel.send('fuck you too')

#this is an inside joke within a friend group, i spams a word 25 times
# Man Man Man Man Man
    elif message.content.startswith(';austin'):
        for i in range(5):
            await message.channel.send("""

MAN                      MAN                    NMANMA                    MAN M            MAN
MAN MANMAN MAN              MAN        MAN                  MAN MAN      MAN            
MAN      MAN      MAN             MAN           MAN                MAN   MAN    MAN
MAN          M         MAN           MAN   MAN   MAN             MAN       MAN MAN
MAN                      MAN          MANMANMANMAN          MAN           MANMA
MAN                      MAN        MAN                         MAN       MAN               MANA
MAN                      MAN      MAN                             MAN     MAN                  MAN
            
            """)
            await message.channel.send('᲼᲼')

    elif message.content.startswith('man'):
        await message.channel.send("""
      
      MAN                      MAN                    NMANMA                    MAN M            MAN
MAN MANMAN MAN              MAN        MAN                  MAN MAN      MAN            
MAN      MAN      MAN             MAN           MAN                MAN   MAN    MAN
MAN          M         MAN           MAN   MAN   MAN             MAN       MAN MAN
MAN                      MAN          MANMANMANMAN          MAN           MANMA
MAN                      MAN        MAN                         MAN       MAN               MANA
MAN                      MAN      MAN                             MAN     MAN                  MAN
            
      """)
# Zaddy Chen
    elif message.content.startswith(';drchen'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/870496185432014868/904866132320723035/REAL.mp4'
        )
    elif message.content.startswith(';god'):
        await message.channel.send(
            'https://media.discordapp.net/attachments/878082497508946020/905273517300400198/unknown.png'
        )
# I hate You
    elif message.content.startswith(';i hate you'):
        await message.channel.send('Cry about it little bitch')

# Test
    elif message.content.startswith(';test'):
        await message.channel.send('Bot is Up and Running')

# Genshin ad ?
    elif message.content.startswith(';genshin'):
        await message.channel.send(
            'Genshin Impact is an open-world action role-playing game that allows the player to control one of four interchangeable characters in a party. Switching between characters can be done quickly during combat, allowing the player to use several different combinations of skills and attacks. Download Here: https://genshin.mihoyo.com/en/ '
        )

# Cultured
    elif message.content.startswith(';cultured'):
        await message.channel.send(
            'https://media.discordapp.net/attachments/904876881810165831/904912371758297128/unknown.png'
        )
        await message.channel.send('Random Hentai: https://nhentai.to/random/ '
                                   )

#   elif message.content.startswith(''):

# await message.channel.send('')

    elif message.content.startswith(';veteran'):
        await message.channel.send(
            '''What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in Guerrilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo'''
        )

# Cursed
    elif message.content.startswith(';cursed'):
        cursed = get_cursed()
        await message.channel.send(cursed)
# Waifu
    elif message.content.startswith(';waifu'):
        waifu = get_waifu()
        await message.channel.send(waifu)
        await client.delete_message(message)
# Neko
    elif message.content.startswith(';neko'):
        neko = get_neko()
        await message.channel.send(neko)
        await client.delete_message(message)
# Trap
    elif message.content.startswith(';trap'):
        trap = get_trap()
        await message.channel.send(trap)
        await client.delete_message(message)
# BJ
    elif message.content.startswith(';bj'):
        bj = get_bj()
        await message.channel.send(bj)
        await client.delete_message(message)
# SFW Waifu
    elif message.content.startswith(';wife'):
        wife = get_wife()
        await message.channel.send(wife)
        await client.delete_message(message)
# Help
    elif message.content.startswith(';help'):
        await message.channel.send("""   **Daddy Chen Commands**
        `fuck you`, `austin`, `drchen`, `i hate you`, `genshin`, `cultured`, `veteran`, `cursed` , `god`, `trap`, `waifu`, `bj`, `neko`"""
                                   )

    await bot.process_commands(message)


# Uptime Robot Connection
keep_alive()
#Bot Token
bot.run(token)
