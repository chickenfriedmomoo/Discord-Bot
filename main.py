import discord 
import os
intents = discord.Intents.default()
clint = discord.Client(intents=intents)


@clint.event
async def on_ready():
  print('We have logged in as {0.user}'.format(clint))

@clint.event
async def on_message(message):
  if message.author == clint.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

clint.run('MTE5NjA5MDg1ODkyODM1NzUyNg.GJK3bM.C1xxIh-0-HZQLdW68h8iYgaQFwmboWKl3YBvAk')

