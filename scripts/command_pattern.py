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

    @staticmethod
    def get_arg_type(typename):
        """
        gets and returns the class of the argument type from
        variable argument:
            '<typename:variable_name>'

        or throws an assertion error if no match
        """
        assert typename in PATTERN_TYPES
        return PATTERN_TYPES[typename]

    def is_match(arguments):
        """
        returns True if the arguments match self.pattern
        """
        for pattern_arg, arg in zip(pattern, arguments):
            if is_variable_argument(pattern):
                #CONTINUE
            
        return False

            
    def get_pattern_object(arguments):
        """
        returns an object containing the variable name as
        keys and the input values as values (translated to
        the correct type.

        'list <something>'
        """
        

