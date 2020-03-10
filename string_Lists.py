user_string = input('Please type the word: ')

if user_string[len(user_string)::-1] == user_string:
    print('This is palindrome')
else:
    print(user_string)