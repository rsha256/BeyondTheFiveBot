import discord
import env.token 

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('!members'):
        x = message.guild.members
        m = ''
        for member in x:
            m = m + '\n' +member.name 
        await message.channel.send('```'+m+'```')
        

client.run(token)
