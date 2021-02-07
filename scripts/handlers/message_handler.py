import asyncio
from command_pattern import CommandPattern


"""
message handler has three main functions

1. create a handler to a pattern (decorator)
2. run all handlers asynchronously if they match
3. run a single handler if it matches
"""

class MessageHandler:
    def __init__(self):
        self.handlers = []

    def create_handler(self, pattern: str):
        # return a decorator function which takes their
        # function and adds it to the handlers as tuple
        # (pattern : CommandPattern, handleFunction : function)

        # translate the pattern
        command_pattern = CommandPattern(pattern)

        def decorated_handler(pattern_handler):
            self.handlers.append((command_pattern, pattern_handler))
            return pattern_handler

        return decorated_handler

    async def run_handlers(self, message, arguments: list[str]):
        for command_pattern, pattern_handler in self.handlers:
            pattern_object = command_pattern.gen_object(arguments)

            if pattern_object is not None:
                await pattern_handler(message, **pattern_object)


"""
I want to be able to do:

message_handler = MessageHandler()

...

@client.createHandler('word <variable> something <other_variable>')
async def function_name(message, variable, other_variable):
    await do_something()
"""

if __name__ == '__main__':
    message_handler = MessageHandler()

    @message_handler.create_handler('list something')
    async def poop(message):
        await message.channel.send('hi')
