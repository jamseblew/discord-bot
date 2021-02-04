# TO ASSERT THE PATTERN IS VALID BEFORE INSTANTIATING
# CommandPattern

# set of the valid variable name characters
VALID_CHAR_SET = set(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
)

def is_valid_char(c):
    assert type(var) == str
    return c in VALID_CHAR_SET

def is_valid_var(var):
    assert type(var) == str
    return all(map(is_valid_char, var))

def is_variable_argument(argument):
    return argument and argument[0] == '<' and argument[-1] == '>'

def is_valid_pattern(pattern):
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
        elif not is_valid_var(argument):
            return False

    return True

