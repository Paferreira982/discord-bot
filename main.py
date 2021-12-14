import bot
client = bot.getClient()

@client.event
async def on_ready():
  bot.ready(client)
  
@client.event
async def on_message(message):
  command = bot.getCommand(message)

  if message.author == client.user:
    return

  if message.content.startswith("$convert"):
    return await bot.convert(command)

  if message.content.startswith("$price"):
    return await bot.price(command)

  if message.content.startswith("$rank"):
    return await bot.rank(command)

  if message.content.startswith("$help"):
    return await bot.help(command)

  if message.content.startswith("$tokens"):
    return await bot.tokens(command)

bot.run()