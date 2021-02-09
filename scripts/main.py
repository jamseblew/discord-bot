# imports
from settings import TOKEN, PREFIX, OBJECTIVES
from handlers.message_handler import MessageHandler
from misc_func import primes, factors
import discord

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

@list_command_handler.create_handler('member-count')
async def member_count_handler(user_msg):
    guild: discord.Guild = user_msg.channel.guild # There are some strange issues with accessing certain properties of guild
    # I couldn't list all members in the guild, got something to do with the accessor being a Coroutine
    # Can't be fucked, good luck to whoever tries to solve this
    
    await user_msg.channel.send('Probably more than 1')

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
