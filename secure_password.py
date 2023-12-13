import random

# Fuction to shuffle characters in password string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90)) # Generate a random Uppercase letter from ASCII A-Z (65-90)
uppercaseLetter2=chr(random.randint(65,90)) # Generate a random Uppercase letter from ASCII A-Z (65-90)
uppercaseLetter3=chr(random.randint(65,90)) # Generate a random Uppercase letter from ASCII A-Z (65-90)
uppercaseLetter4=chr(random.randint(65,90)) # Generate a random Uppercase letter from ASCII A-Z (65-90)

lowercaseLetter1=chr(random.randint(97,122)) # Generate a random Lowercase letter from ASCII a-z (97-122)
lowercaseLetter2=chr(random.randint(97,122)) # Generate a random Lowercase letter from ASCII a-z (97-122)
lowercaseLetter3=chr(random.randint(97,122)) # Generate a random Lowercase letter from ASCII a-z (97-122)
lowercaseLetter4=chr(random.randint(97,122)) # Generate a random Lowercase letter from ASCII a-z (97-122)

digit1=chr(random.randint(48,57)) # Generate a random number from ASCII 0-9 (48-57)
digit2=chr(random.randint(48,57)) # Generate a random number from ASCII 0-9 (48-57)
digit3=chr(random.randint(48,57)) # Generate a random number from ASCII 0-9 (48-57)
digit4=chr(random.randint(48,57)) # Generate a random number from ASCII 0-9 (48-57)

specialChar1=chr(random.randint(33,47)) # Generate a random number from ASCII 0-9 (33-47)
specialChar2=chr(random.randint(33,47)) # Generate a random number from ASCII 0-9 (33-47)
specialChar3=chr(random.randint(33,47)) # Generate a random number from ASCII 0-9 (33-47)
specialChar4=chr(random.randint(33,47)) # Generate a random number from ASCII 0-9 (33-47)

# Piece together password from generated characters
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + digit1 + digit2 + digit3 + digit4 + specialChar1 + specialChar2 + specialChar3 + specialChar4
secPassword = shuffle(password)

# Output
print(f"Password: {secPassword}")
