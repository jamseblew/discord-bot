import asyncio

class MessageHandler:
    def __init__(self):
        self.handlers = []

    def valid_pattern(pattern):
        for argument in pattern:
            if pattern[0] == '<' and pattern[1] == '>':


    def pattern_matcher(pattern, arguments):
        """
        determines whether the string `pattern` matches list
        `arguments` where pattern contains space seperated
        words in either the format:

        1. a plain word
            pattern = 'word'
        2. a dynamic variable
            pattern = '<variable_name>'
        3. a static variable
            pattern = '<string:variable_name>'

        and returns an object containing the variable name as
        keys and the input values as values (translated to
        the correct type.
        """
        pattern = pattern.split()

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

