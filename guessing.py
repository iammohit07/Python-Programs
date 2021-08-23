print('*' * 10 + ' Welcome to Program ' + '*' * 10)
secret_number = 7
guess_count = 0
guess_limit = int(input('Enter guessing limit :'))
while guess_count < guess_limit :
    guess = int(input('Guess the secret number between 1 to 10 : '))
    guess_count += 1
    if guess == secret_number:
        print('YOU WON !!')
        break
    else:
        print('TRY AGAIN ')
else:
    print('GUESS LIMIT REACHED ')