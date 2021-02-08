# adjusting the path
import sys
from settings import ROOT_PATH
sys.path.append(str(ROOT_PATH / 'scripts'))
sys.path.append(str(ROOT_PATH / 'scripts' / 'misc_func'))
sys.path.append(str(ROOT_PATH / 'scripts' / 'handlers'))

# imports
from settings import TOKEN, PREFIX, OBJECTIVES
from handlers.message_handler import MessageHandler
import discord
from misc_func import primes, factors

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
