from constants import TOKEN, PREFIX
import discord

async def handle_(message, arguments):
    await message.channel.send('testing')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'{message.author}: {message.content}')

        # test for prefix
        if not message.content.startswith(PREFIX):
            return

        content = message.content
        arguments = content[len(PREFIX) + 1:].split()
        await handle_request(message, arguments)

client = MyClient()



client.run(TOKEN)
