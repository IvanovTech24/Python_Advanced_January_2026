class PasswordTooShortError(Exception):
    """
    Message: "Password must contain at least 8 characters"
    """
    pass

class PasswordTooCommonError(Exception):
    """
    Message: "Password must be a combination of digits, letters, and special characters"
    """
    pass

class PasswordNoSpecialCharactersError(Exception):
    """
    Message: "Password must contain at least 1 special character"
    """
    pass

class PasswordContainsSpacesError(Exception):
    """
    Message: "Password must not contain empty spaces"
    """
    pass

PASSWORD_LENGTH = 8
SPECIAL_CHARACTER = {"@", "*", "&", "%"}

def password_too_common(pwd, special):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_specials = all(ch in special for ch in pwd)
    return only_digits or only_letters or only_specials

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < PASSWORD_LENGTH:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(password, SPECIAL_CHARACTER):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIAL_CHARACTER for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")