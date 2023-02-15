import re

def validateEmail(email:str) -> bool:
    """
    Verify is the given :attr:`email`  in the argument is  valid or not.\n
    Return True if valid and False if not.
    """
    validRegex = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(validRegex,email):
        return True
    return False



