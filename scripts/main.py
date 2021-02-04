from constants import TOKEN, PREFIX
import discord

async def handle_request(message, arguments):
    await message.channel.send('testing')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # test for prefix
        content = message.content
        if not content.startswith(PREFIX):
            return

        arguments = content[len(PREFIX) + 1:].split()
        await handle_request(message, arguments)

client = MyClient()
client.run(TOKEN)
