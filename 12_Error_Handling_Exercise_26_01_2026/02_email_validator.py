class NameTooShortError(Exception):
    """
    Raise it when the name in the email is less than or equal to 4
    ("peter" will be the name in the email "peter@gmail.com").
    Message will be: "Name must be more than 4 characters"
    """
    pass

class MustContainAtSymbolError(Exception):
    """
    Raise it when there is no "@" in the email.
    Message will be: "Email must contain @"
    """
    pass

class InvalidDomainError(Exception):
    """
    Raise it when the domain of the email is invalid
    (valid domains are: .com, .bg, .net, .org).
    Message will be: "Domain must be one of the following: .com, .bg, .org, .net"
    """
    pass

EMAIL_MIN_LEN = 5
VALID_DOMAINS = ["com", "bg", "org", "net"]

while True:
    line = input()
    if line == "End":
        break

    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")

    if len(line.split("@")[0]) < EMAIL_MIN_LEN:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = line.split(".")[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")