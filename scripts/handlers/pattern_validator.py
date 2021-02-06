# TO ASSERT THE PATTERN IS VALID BEFORE INSTANTIATING
# CommandPattern

# set of the valid variable name characters
VALID_CHAR_SET = set(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
)

def is_valid_char(c: str):
    return c in VALID_CHAR_SET

def is_valid_var(var: str):
    """
    test if the variable name is valid
    """
    var = var.split(':')
    if len(var) > 2:
        return False
    for part in var:
        if not all(map(is_valid_char, part)):
            return False
    return True

def is_variable_argument(argument: str):
    return argument and argument[0] == '<' and argument[-1] == '>'

def is_valid_pattern(pattern: str):
    """
    determines whether the string `pattern` matches list
    `arguments` where pattern contains space seperated
    words in either the format:

    1. a plain word
        pattern = 'word'
    2. a dynamic variable
        pattern = '<variable_name>'
    3. a static variable
        pattern = '<typename:variable_name>'

    var_name is vlaid iff valid_var_char(x) for all x
    in var_name.
    """
    pattern = pattern.split()

    for argument in pattern:
        if is_variable_argument(argument): 
            if not is_valid_var(argument[1:-1]):
                return False

    return True
