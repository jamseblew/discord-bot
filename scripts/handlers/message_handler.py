import asyncio
from command_pattern import CommandPattern

class MessageHandler:
    def __init__(self):
        self.handlers = []

    def create_handler(pattern):
        # return a decorator function which takes their
        # function and adds it to the handlers as tuple
        # (pattern, handleFunction)

    async def run_handlers(arguments):

        


"""
I want to be able to do:

self.handler = MessageHandler()

...

@client.createHandler('word <variable> something <other_variable>')
async def function_name(message, variable, other_variable):
    await do_something()

