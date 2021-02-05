from pattern_validator import is_valid_pattern, is_variable_argument

# mapping of variable typenames to their class
PATTERN_TYPES = {
    'string':   str,
    'int':      int,
    'float':    float
}

class CommandPattern:
    def __init__(self, pattern):
        assert is_valid_pattern(pattern)
        self.pattern = pattern.split()

    #staticmethod
    def is_static(p_arg):
        return ':' in p_arg

    @staticmethod
    def get_arg_typename(p_arg):
        # if they forgot to strip it of the <>
        if is_variable_argument(p_arg):
            p_arg = p_arg[1:-1]

        assert is_static(p_arg)
        return p_arg.split(':')[0]


    @staticmethod
    def get_arg_type(p_arg):
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
    def translate_var(p_arg, arg):
        """
        returns the variable argument translated into the
        required static type/class
        """
        argtype = CommandPattern.get_arg_type(p_arg)
        return argtype(arg)

    def can_translate_args(arguments):
        """
        returns True if the arguments have input strings
        which can be translated into the specified typename.
        """
        # p_arg is the pattern argument
        for p_arg, arg in zip(self.pattern, arguments):
            if is_variable_argument(p_arg) and is_static(p_arg):
                try:
                    translate_var(p_arg, arg)
                except:
                    return False

        return True

    def is_match(arguments):
        """
        returns True if the arguments match self.pattern
        """
        if not len(arguments) == len(self.pattern):
            return False

        if not can_translate_args(arguments):
            return False

        # p_arg represents the pattern argument
        for p_arg, arg in zip(self.pattern, arguments):
            if not is_variable_argument(p_arg) and arg != p_arg:
                return False
            
        return True

            
    def get_pattern_object(arguments):
        """
        returns an object containing the variable name as
        keys and the input values as values (translated to
        the correct type.

        'list <something>'
        """
        output_obj = {}
