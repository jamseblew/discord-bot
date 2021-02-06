from pattern_validator import is_valid_pattern, is_variable_argument

# mapping of variable typenames to their class
PATTERN_TYPES = {
    'string':   str,
    'int':      int,
    'float':    float
}

class CommandPattern:
    def __init__(self, pattern: str):
        assert is_valid_pattern(pattern)
        self.pattern = pattern.split()

    # STATIC METHODS


    @staticmethod
    def strip_p_arg(p_arg: str):
        if is_variable_argument(p_arg):
            return p_arg[1:-1]
        return p_arg


    #staticmethod
    def is_static(p_arg: str):
        return ':' in p_arg


    @staticmethod
    def get_arg_typename(p_arg: str):
        """
        takes in pattern argument `p_arg` and returns
        the typename of the argument.

        >>> CommandPattern.get_arg_typename('<string:var_name>')
        'string'
        """
        # strip <>
        p_arg = CommandPattern.strip_p_arg(p_arg)

        # default type string
        if not CommandPattern.is_static(p_arg):
            return 'string'

        return p_arg.split(':')[0]


    @staticmethod
    def get_arg_type(p_arg: str):
        """
        gets and returns the class of the argument type from
        variable argument:
            '<typename:variable_name>'

        or throws an assertion error if no match
        """
        typename = CommandPattern.get_arg_typename(p_arg)
        assert typename in PATTERN_TYPES
        return PATTERN_TYPES[typename]


    @staticmethod
    def translate_var(p_arg: str, arg: str):
        """
        returns the variable argument translated into the
        required static type/class
        """
        argtype = CommandPattern.get_arg_type(p_arg)
        return argtype(arg)


    @staticmethod
    def get_p_arg_name(p_arg: str):
        p_arg = CommandPattern.strip_p_arg(p_arg)
        if CommandPattern.is_static(p_arg):
            return p_arg.split(':')[1]
        return p_arg


    # PRIVATE METHODS 
    def _can_translate_args(self, arguments: list[str]):
        """
        returns True if the arguments have input strings
        which can be translated into the specified typename.
        """
        # p_arg is the pattern argument
        for p_arg, arg in zip(self.pattern, arguments):
            if is_variable_argument(p_arg) and CommandPattern.is_static(p_arg):
                try:
                    CommandPattern.translate_var(p_arg, arg)
                except:
                    return False

        return True


    def _is_match(self, arguments: list[str]):
        """
        returns True if the arguments match self.pattern
        """
        if not len(arguments) == len(self.pattern):
            return False

        if not self._can_translate_args(arguments):
            return False


        # p_arg represents the pattern argument
        for p_arg, arg in zip(self.pattern, arguments):
            if not is_variable_argument(p_arg) and arg != p_arg:
                return False
            
        return True


    # PUBLIC METHODS
    def gen_object(self, arguments: list[str]):
        """
        returns None if the arguments do not match the
        pattern.

        otherwise returns an object containing the variable name as
        keys and the input values as values (translated to
        the correct type).

        for:
        self.pattern: CommandPattern('list <int:something>').pattern
        arguments: ['list', '1']

        output:
        {
            'something': 1
        }
        """
        if not self._is_match(arguments):
            return None

        output_obj = {}
        for p_arg, arg in zip(self.pattern, arguments):
            if not is_variable_argument(p_arg):
                continue

            p_arg_name = CommandPattern.get_p_arg_name(p_arg)
            arg_val = CommandPattern.translate_var(p_arg, arg)

            output_obj[p_arg_name] = arg_val

        return output_obj


# testing
if __name__ == '__main__':
    test_pattern = CommandPattern('print <string:message> <int:times>')
    input_args = 'print something 10'.split()
    print(test_pattern.gen_object(input_args))
