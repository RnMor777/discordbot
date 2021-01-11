# bot.py
import os
import discord
import random

f = open("token.txt", "r")
TOKEN = f.readline()

LEADER = "~"
intents = discord.Intents.all()
client = discord.Client(intents=intents)

def main():
    client.run(TOKEN)

@client.event
async def on_ready():
    print ("Connection established")

@client.event
async def on_message(message):
    print (message.author)
    if message.author == client.user:
        return

    if message.content[0] == LEADER:
        msg = message.content.split(' ')
        command = msg[0][1:]
        filename = "{}.sf".format(message.author)

        if (command == "Add" or command == "add"):
            if (os.path.isfile(filename)):
                f = open (filename, "a+")
                f.write(msg[1]+'\n')
                f.close()
            else:
                f = open (filename, "w")
                f.write(msg[1]+'\n')
                f.close()

        if (command == "Show" or command == "show"):
            if (os.path.isfile(filename)):
                f = open (filename, "r")
                tmp = [x.replace('\n','') for x in f.readlines()]
                user = await client.fetch_user(message.author.id)
                await user.send(' '.join(tmp))
                f.close()



if __name__ == "__main__":
    main()
