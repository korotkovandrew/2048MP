import re

def checkPassword(password) -> str:
    '''
        Returns empty string if password is valid
        or error message if password is invalid
    '''
    if len(password) < 6:
        return "Password is too short"
    elif not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter"
    elif not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter"
    elif not re.search("[0-9]", password):
        return "Password must contain at least one number"
    elif re.search("\s", password):
        return "Password must contain no whitespaces"
    else:
        return ""

def checkNickname(nickname):
    '''
        Returns empty string if nickname is valid
        or error message if nickname is invalid
    '''
    if len(nickname) < 4:
        return "Nickname is too short"
    elif not re.search("[a-zA-Z0-9]", nickname):
        return "Nickname must contain only letters and numbers"
    elif re.search("\s", nickname):
        return "Nickname must contain no whitespaces"
    else:
        return ""