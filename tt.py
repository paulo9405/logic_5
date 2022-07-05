valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

name = 'Pasu'


for letter in name: # This will loop through the input word
    if letter not in valid_characters:
        check = True
        print(check)
    else:
        check = False
        print(check)

