# bot.py
import os
import discord
import random

f = open("token.txt", "r")
TOKEN = f.readline()

LEADER = "!"
copy = []
mainserver = ""
intents = discord.Intents.all()
client = discord.Client(intents=intents)

def main():
    global copy
    f = open("copypasta.txt", "r")
    copy = list(map(str, f.readlines()))
    f.close()

    for i in range(len(copy)):
        copy[i] = copy[i].replace("{}", '\n')

    client.run(TOKEN)

@client.event
async def on_ready():
    global mainserver
    for i in client.guilds:
        if (i.id == 592488893484630016):
            mainserver = i
    print ("Connection established")

@client.event
async def on_member_update(before, after):
    # "serverID":"592488893484630016", "userID":"577682679307173888"
    if (before.id == 577682679307173888):
        # if (after.nick != "Spankenheimer"):
            # await after.edit(nick = "Spankenheimer")
        if (mainserver.get_role(746854796501188649) not in after.roles):
            await after.add_roles(mainserver.get_role(746854796501188649))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "!" in message.content and message.content[0] == LEADER:
        msg = message.content.split(' ')
        command = msg[0][1:]

        who = message.raw_mentions
        for i in message.role_mentions:
            who.extend([j.id for j in i.members])
        who = list(set(who))

        if (command == "spank"):
            print (spank)

        if (command == "gnome"):
            if (len(who) > 0):
                for j in who:
                    user = await client.fetch_user(j)
                    await user.send("You've been gnomed!")
            else:
                await message.channel.send("You've been gnomed!")

        if (command == "copy"):
            copysend = random.choice(copy)
            if (len(who) > 0):
                for j in who:
                    user = await client.fetch_user(j)
                    await user.send(copysend)
                    copysend = random.choice(copy)
            else:
                await message.channel.send(copysend)

        if (command == "spy" or command == "spied"):
            spy = "https://cdn.discordapp.com/attachments/703092458208100394/764307449808683028/unknown.png"
            channel = client.get_channel(703092458208100394)

            if (len(who) > 0):
                for j in who:
                    user = await client.fetch_user(j)
                    await user.send(spy)
                    copysend = random.choice(spy)
            else:
                # await channel.send(spy)
                await message.channel.send(spy)

if __name__ == "__main__":
    main()
