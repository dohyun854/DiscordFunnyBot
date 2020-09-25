import discord
import configparser
import asyncio
import os


client = discord.Client()


@client.event
async def on_ready():
    a = configparser.ConfigParser()
    print(client.user.id)
    print("ready")
    game = discord.Game("p!help")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("p!help"):
        embed = discord.Embed(title="Funny Discord Bot", description="made by Codeman#0001", color=0xadfffe)
        embed.set_author(name="Bot Commands")
        embed.set_thumbnail(
            url="https://theme.zdassets.com/theme_assets/678183/af1a442f9a25a27837f17805b1c0cfa4d1725f90.png")
        embed.add_field(name="p!help", value="Get help (you're using it lol)", inline=False)
        embed.add_field(name="p!info", value="Show bot's information", inline=False)
        embed.add_field(name="p!invite", value="Invite me!", inline=False)
        embed.add_field(name="p!support", value="Get support", inline=False)
        embed.add_field(name="p!donate", value="Donate to bot developer.", inline=False)
        embed.add_field(name="p!ban [@Member] [Reason(optional)]", value="Bans user (Fake)", inline=False)
        embed.add_field(name="p!kick [@Member] [Reason(optional)]", value="Kick user (Fake)", inline=False)
        embed.add_field(name="p!mute [@Member] [Reason(optional)]", value="Mute user (Fake)", inline=False)
        embed.add_field(name="p!warn [@Member] [Reason(optional)]", value="Warn user (Fake)", inline=False)
        embed.add_field(name="p!hack [@Member]", value="Hack user's Discord account (Fake)", inline=False)
        embed.add_field(name="p!kill [@Member]", value="Kill user (Fake)", inline=False)
        embed.add_field(name="p!get-nitro", value="Get Discord Nitro! (Maybe real)", inline=False)
        embed.add_field(name="p!get-real-nitro", value="Get REAL Discord Nitro!", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("p!info"):
        embed = discord.Embed(title="Funny Bot#3396", color=0x99ffe6)
        embed.set_author(name="Information")
        embed.add_field(name="Developer", value="Codeman#0001", inline=True)
        embed.add_field(name="Logo Creator", value="Codeman#0001", inline=True)
        embed.add_field(name="Creation Date", value="August 28 2020", inline=True)
        embed.add_field(name="Prefix", value="`p!`", inline=True)
        embed.add_field(name="Bot Commands", value="`p!help` for bot commands.", inline=True)
        embed.add_field(name="Donate", value="`p!donate` to donate", inline=True)
        embed.add_field(name="Invite", value="`p!invite` to invite me!", inline=True)
        embed.add_field(name="Image Source", value="Codeman#0001, Google, Pixabay, and Discord", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("p!invite"):
        embed = discord.Embed(title="Invite Me!",
                              url="https://discord.com/oauth2/authorize?client_id=748731937081786459&scope=bot&permissions=201812992",
                              color=0xffe66b)
        embed.set_author(name="Funny Discord Bot Invite")
        embed.set_footer(text="Be careful! I can ban you anytime! LOL")
        await message.channel.send(embed=embed)

    if message.content.startswith("p!support"):
        embed = discord.Embed(title="DM Codeman#0001 to get support", color=0x8095ff)
        embed.set_author(name="Get Bot Support")
        embed.set_thumbnail(url="https://blogfiles.pstatic.net/MjAyMDA4MjhfMjM4/MDAxNTk4NTg1MTcwNDU3.tw9dy7KDcWJ02-g50DeSeGN57JCS5zoxmVhuxT2bWSkg.ibbzJQ2xtgOQ3_EuUGI3gP3poeDHbFHzbNIVF_Td6Mog.JPEG.dohyun854/8biticon_512.jpg?type=w1")
        embed.set_footer(text="No spam DMing!!")
        await message.channel.send(embed=embed)

    if message.content.startswith("p!donate"):
        embed = discord.Embed(title="Donate to Bot Developer", url="https://www.patreon.com/Codeman_IT", color=0xceff85)
        embed.set_author(name="Donate")
        embed.set_thumbnail(
            url="https://blogfiles.pstatic.net/MjAyMDA4MjhfMjM4/MDAxNTk4NTg1MTcwNDU3.tw9dy7KDcWJ02-g50DeSeGN57JCS5zoxmVhuxT2bWSkg.ibbzJQ2xtgOQ3_EuUGI3gP3poeDHbFHzbNIVF_Td6Mog.JPEG.dohyun854/8biticon_512.jpg?type=w1")
        embed.set_footer(text="Join developer's fan server too! Link: https://discord.gg/xbn8hzM")
        await message.channel.send(embed=embed)

    if message.content.startswith("p!ban"):
        if message.content[28:] == "":
            author = message.guild.get_member(int(message.content[9:27]))
            embed = discord.Embed(title="Your punishment has been updated.", color=0xff0000)
            embed.set_author(name="Moderation")
            embed.add_field(name="Action", value="Ban", inline=True)
            embed.add_field(name="Reason", value="No Reason", inline=True)
            embed.add_field(name="Duration", value="Permanent", inline=True)
            await author.send(embed=embed)
            embed = discord.Embed(title="**Banned**", color=0xff0000)
            embed.set_author(name="Moderation Log")
            embed.add_field(name="User", value=author, inline=True)
            embed.add_field(name="Action by", value="YOU", inline=True)
            embed.add_field(name="Reason", value="No Reason", inline=True)
            embed.add_field(name="Duration", value="Permanent", inline=True)
            await message.channel.send(embed=embed)
        else:
            author = message.guild.get_member(int(message.content[9:27]))
            reason = message.content[28:]
            embed = discord.Embed(title="Your punishment has been updated.", color=0xff0000)
            embed.set_author(name="Moderation")
            embed.add_field(name="Action", value="Ban", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Duration", value="Permanent", inline=True)
            await author.send(embed=embed)
            embed = discord.Embed(title="**Banned**", color=0xff0000)
            embed.set_author(name="Moderation Log")
            embed.add_field(name="User", value=author, inline=True)
            embed.add_field(name="Action by", value="YOU", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Duration", value="Permanent", inline=True)
            await message.channel.send(embed=embed)

    if message.content.startswith("p!kick"):
        if message.content[29:] == "":
            author = message.guild.get_member(int(message.content[10:28]))
            embed = discord.Embed(title="Your punishment has been updated.", color=0xffa500)
            embed.set_author(name="Moderation")
            embed.add_field(name="Action", value="Kick", inline=True)
            embed.add_field(name="Reason", value="No Reason", inline=True)
            await author.send(embed=embed)
            embed = discord.Embed(title="**Kicked**", color=0xffa500)
            embed.set_author(name="Moderation Log")
            embed.add_field(name="User", value=author, inline=True)
            embed.add_field(name="Action by", value="YOU", inline=True)
            embed.add_field(name="Reason", value="No Reason", inline=True)
            await message.channel.send(embed=embed)
        else:
            author = message.guild.get_member(int(message.content[10:28]))
            reason = message.content[29:]
            embed = discord.Embed(title="Your punishment has been updated.", color=0xffa500)
            embed.set_author(name="Moderation")
            embed.add_field(name="Action", value="Kick", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            await author.send(embed=embed)
            embed = discord.Embed(title="**Kicked**", color=0xffa500)
            embed.set_author(name="Moderation Log")
            embed.add_field(name="User", value=author, inline=True)
            embed.add_field(name="Action by", value="YOU", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            await message.channel.send(embed=embed)

    if message.content.startswith("p!mute"):
        if message.content[29:] == "":
            author = message.guild.get_member(int(message.content[10:28]))
            embed = discord.Embed(title="Your punishment has been updated.", color=0xff0000)
            embed.set_author(name="Moderation")
            embed.add_field(name="Action", value="Mute", inline=True)
            embed.add_field(name="Reason", value="No Reason", inline=True)
            embed.add_field(name="Duration", value="Permanent", inline=True)
            await author.send(embed=embed)
            embed = discord.Embed(title="**Muted**", color=0xff0000)
            embed.set_author(name="Moderation Log")
            embed.add_field(name="User", value=author, inline=True)
            embed.add_field(name="Action by", value="YOU", inline=True)
            embed.add_field(name="Reason", value="No Reason", inline=True)
            embed.add_field(name="Muted until", value="Permanent", inline=True)
            await message.channel.send(embed=embed)
        else:
            author = message.guild.get_member(int(message.content[10:28]))
            reason = message.content[29:]
            embed = discord.Embed(title="Your punishment has been updated.", color=0xff0000)
            embed.set_author(name="Moderation")
            embed.add_field(name="Action", value="Mute", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Duration", value="Permanent", inline=True)
            await author.send(embed=embed)
            embed = discord.Embed(title="**Muted**", color=0xff0000)
            embed.set_author(name="Moderation Log")
            embed.add_field(name="User", value=author, inline=True)
            embed.add_field(name="Action by", value="YOU", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Muted until", value="Permanent", inline=True)
            await message.channel.send(embed=embed)

    if message.content.startswith("p!warn"):
        if message.content[29:] == "":
            author = message.guild.get_member(int(message.content[10:28]))
            embed = discord.Embed(title="Your punishment has been updated.", color=0xffee00)
            embed.set_author(name="Moderation")
            embed.add_field(name="Action", value="Warn", inline=True)
            embed.add_field(name="Reason", value="No Reason", inline=True)
            await author.send(embed=embed)
            embed = discord.Embed(title="**Warned**", color=0xffee00)
            embed.set_author(name="Moderation Log")
            embed.add_field(name="User", value=author, inline=True)
            embed.add_field(name="Action by", value="YOU", inline=True)
            embed.add_field(name="Reason", value="No Reason", inline=True)
            await message.channel.send(embed=embed)
        else:
            author = message.guild.get_member(int(message.content[10:28]))
            reason = message.content[29:]
            embed = discord.Embed(title="Your punishment has been updated.", color=0xffee00)
            embed.set_author(name="Moderation")
            embed.add_field(name="Action", value="Warn", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            await author.send(embed=embed)
            embed = discord.Embed(title="**Warned**", color=0xffee00)
            embed.set_author(name="Moderation Log")
            embed.add_field(name="User", value=author, inline=True)
            embed.add_field(name="Action by", value="YOU", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            await message.channel.send(embed=embed)

    if message.content.startswith("p!hack"):
        author = message.guild.get_member(int(message.content[10:28]))
        embed = discord.Embed(title="Finding out IP address......", color=0xffee00)
        embed.set_author(name="Hacking......")
        msg = await message.channel.send(embed=embed)
        await asyncio.sleep(3,0)
        embed = discord.Embed(title="Finding out email address......", color=0xffee00)
        embed.set_author(name="Hacking......")
        await msg.edit(embed=embed)
        await asyncio.sleep(3,0)
        embed = discord.Embed(title="Finding out password......", color=0xffee00)
        embed.set_author(name="Hacking......")
        await msg.edit(embed=embed)
        await asyncio.sleep(3,0)
        embed = discord.Embed(title="Logging in......", color=0xffee00)
        embed.set_author(name="Hacking......")
        await msg.edit(embed=embed)
        await asyncio.sleep(3,0)
        embed = discord.Embed(title="Stealing private information......", color=0xffee00)
        embed.set_author(name="Hacking......")
        await msg.edit(embed=embed)
        await asyncio.sleep(3,0)
        embed = discord.Embed(title="Selling information to a government......", color=0xffee00)
        embed.set_author(name="Hacking......")
        await msg.edit(embed=embed)
        await asyncio.sleep(3,0)
        embed = discord.Embed(title="Virus injecting......", color=0xffee00)
        embed.set_author(name="Hacking......")
        await msg.edit(embed=embed)
        await asyncio.sleep(3,0)
        embed = discord.Embed(title="Hacking complete! Bot earned $98.99", color=0xffee00)
        embed.set_author(name="Hacking Complete")
        await msg.edit(embed=embed)
        embed = discord.Embed(title="You lost $99.98", color=0x00a313)
        embed.set_author(name="Account Hacked!!")
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/10/24/07/12/hacker-2883632_1280.jpg")
        embed.add_field(name="Hacker", value="Funny Bot#3396", inline=True)
        embed.add_field(name="Hack Requester", value="[Private]", inline=True)
        embed.add_field(name="Damages",
                        value="- Private information(includes IP address and password) leaked\n- $99.98 stolen\n- Virus injected to your devices.",
                        inline=True)
        embed.set_footer(text="Automatically called for police.")
        await author.send(embed=embed)

    if message.content.startswith("p!kill"):
        author = message.guild.get_member(int(message.content[10:28]))
        embed = discord.Embed(title="How dare you murder our member!!", color=0x9694ff)
        embed.set_author(name="Killed!!")
        embed.set_thumbnail(url="https://c0.wallpaperflare.com/preview/82/63/732/shooting-killing-murder-crime.jpg")
        embed.add_field(name="Killer", value="YOU", inline=True)
        embed.add_field(name="Killed Member", value=author, inline=True)
        embed.add_field(name="Weapon Used", value="Gun", inline=True)
        embed.set_footer(text="Called Police Automatically")
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="🤪 • • • • • 🔫", color=0x9694ff)
        embed.set_author(name="You are MURDERED!")
        embed.set_thumbnail(url="https://c0.wallpaperflare.com/preview/82/63/732/shooting-killing-murder-crime.jpg")
        embed.add_field(name="Body Condition", value="DEAD", inline=True)
        embed.add_field(name="Murderer", value="[Private]", inline=True)
        embed.add_field(name="Target", value="YOU", inline=True)
        embed.add_field(name="Weapon Used", value="Gun", inline=True)
        embed.set_footer(text="Bot called for police automatically.")
        await author.send(embed=embed)

    if message.content.startswith("p!get-nitro"):
        await message.channel.send("https://discord.gift/KEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEKEK")
        embed = discord.Embed(title="KEKEKEKEK", color=0xffb433)
        embed.set_author(name="NO Discord Nitro For You!!")
        embed.set_thumbnail(url="https://i.redd.it/mvoen8wq3w831.png")
        embed.add_field(name="Why are you not giving me Discord Nitro?", value="Because, you're too DUM.", inline=True)
        embed.add_field(name="Can I have Discord Nitro for free?", value="No, never. kkkk", inline=True)
        embed.add_field(name="I want Discord Nitro, how can I get it?", value="Buy it, you stupid.", inline=True)
        embed.set_footer(text="Bruh, get Discord Nitro legitimately!!")
        await message.channel.send(embed=embed)

    if message.content.startswith("p!get-real-nitro"):
        embed = discord.Embed(title="Get Discord Nitro for FREE!!", url="https://discord.gift/fVAfX9NzdtKVZmgQ",
                              description="Legitimately Gifting", color=0x8d5cff)
        embed.set_author(name="Discord Nitro Gift Here!!")
        embed.set_thumbnail(url="https://discord.com/assets/b941bc1dfe379db6cc1f2acc5a612f41.png")
        embed.set_footer(text="Yo, this time real Nitro")
        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
