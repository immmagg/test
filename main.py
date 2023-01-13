import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Works")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send(message.content)

client.run('TOKEN')
