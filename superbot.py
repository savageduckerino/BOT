import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import re

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print ("Bot is ready.")
    print ("User: " + bot.user.name)
    print ("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Quiz-Dog | !help"))

@bot.event
async def on_message(message):
    if message.content.startswith("!help"):
        embed = discord.Embed(title="Quiz-Dog", description="<@%s>: Commands" % message.author.id, color=0x7289DA, icon='https://i.imgur.com/K7rEGgK.jpg')
        embed.set_thumbnail(url="https://i.imgur.com/K7rEGgK.jpg")
        embed.add_field(name='**!help**', value="shows this command with bad gui :stuck_out_tongue:\n`Syntax: !help`\n")
        embed.add_field(name='**!life**', value="send a life through the Quiz-Dog!\n`Syntax: !life <phone>`\n")
        embed.add_field(name='**!confirm**', value="confirm a life through the Quiz-Dog bot.\n`Syntax: !confirm <code> <referral>`\n")
        embed.set_footer(text="Quiz-Dog | !help", icon_url='https://i.imgur.com/K7rEGgK.jpg')
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith("!life"):
        args = message.content.split(" ")
        phone = re.sub(r"[()-/\s/]", "", (" ".join(args[1:])))
        if phone == "":
            await bot.send_message(message.channel, "<@%s>: Invalid arguments. Use `!life <phone>` to be my human and actually send a life." % message.author.id)
        else:
            if not phone[:2] == "+1":
                phone = "+1" + phone
            await bot.send_message(discord.Object(id='450114331661697028'), ".cancel")
            await bot.send_message(discord.Object(id='450114331661697028'), f".life {phone}")
            await bot.send_message(message.channel, f"<@%s>: Verification code sent to `{phone}`, please use `!confirm <code> <referral>` to queue the life and bark." % message.author.id)

    if message.content.startswith("!confirm"):
        args = message.content.split(" ")
        secondargs = (" ".join(args[1:]))
        if secondargs == "" or not len(args[1]) == 4:
            await bot.send_message(message.channel, "<@%s>: Invalid arguments. Use `!life <phone>` and then `!confirm <code> <referral>` to queue the life, you don't know what to do hooman." % message.author.id)
        else:
            code = args[1]
            referral = args[2]
            await bot.send_message(discord.Object(id='450114331661697028'), f".confirm {code} {referral}")
            await bot.send_message(discord.Object(id='450135109757173770'), f"Quiz-Dog has barked at {referral}'s mom and queued a life to `{referral}`.")
            await bot.send_message(message.channel, f"<@%s>: Account created. Life has been applied to the account `{referral}` with Quiz-Dog" % message.author.id)

bot.run("NDQ4MTExODgwMDQ5Nzg2ODkw.DevB8w.2sc0eNDVdjCnC4gAq7mbLhixF_g")
