num = int(input('Enter number tilll which you wanna check Fizz and Buzz :'))
for i in range(1, num + 1):
    if (i % 3 == 0):
        if (i % 3 == 0 and i % 5 == 0):
            print(str(i) + ' : Fizzbuzz')
        else:
            print(str(i) + ' : Fizz')
    elif (i % 5 == 0):
        if (i % 3 == 0 and i % 5 == 0):
            print(str(i) + ' : Fizzbuzz')
        else:
            print(str(i) + ' : Buzz')
    else:
        print(i)
