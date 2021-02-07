# adjusting the path
import sys
from pathlib import Path
sys.path.append(str(Path('.') / 'handlers'))

# imports
from settings import TOKEN, PREFIX
from message_handler import MessageHandler
import discord

main_message_handler = MessageHandler()

@main_message_handler.create_handler('say <string:msg>')
async def talk(user_message, msg):
    await user_message.delete()
    await user_message.channel.send(msg)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if not message.content.startswith(PREFIX):
            return

        arguments = message.content[len(PREFIX) + 1:].split()
        await main_message_handler.run_handlers(message, arguments)


client = MyClient()
client.run(TOKEN)
