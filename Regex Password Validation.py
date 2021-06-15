# https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python

# You need to write regex that will validate a password to make sure it meets the following criteria:

#     At least six characters long
#     contains a lowercase letter
#     contains an uppercase letter
#     contains a number

# Valid passwords will only be alphanumeric characters.
def check (string):
    import re
    if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$', string):
        return True
    else:
        return False

print(check('fjd3IR9'))
print(check('ghdfj32'))
print(check('DSJKHD23'))
print(check('dsF43'))
print(check('4fdg5Fj3'))





