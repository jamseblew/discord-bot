# adjusting the path
import sys
from pathlib import Path
sys.path.append(str(Path('.') / 'handlers'))
sys.path.append(str(Path('.') / 'misc_func'))

# imports
from settings import TOKEN, PREFIX, OBJECTIVES
from message_handler import MessageHandler
import discord
import primes, factors

list_command_handler = MessageHandler()

@list_command_handler.create_handler('list factors <int:number>')
async def prime_handler(user_msg, number):
    await user_msg.channel.send(' '.join(map(str, factors.get_factors(number))))


@list_command_handler.create_handler('list primes <int:number>')
async def prime_handler(user_msg, number):
    await user_msg.channel.send(' '.join(map(str, primes.get_primes(number))))


@list_command_handler.create_handler('list objectives')
async def list_objectives_handler(user_msg):
    await user_msg.channel.send('\n'.join(OBJECTIVES))


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if not message.content.startswith(PREFIX):
            return

        arguments = message.content[len(PREFIX):].split()
        await list_command_handler.run_handlers(message, arguments)


client = MyClient()
client.run(TOKEN)
