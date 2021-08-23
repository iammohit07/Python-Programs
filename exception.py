try:
    num1,num2 = input('enter values to divide '),input('enter values to divide ')
    print(int(num1)//int(num2))
except ZeroDivisionError:
    print('cannot divide with zero ')
except TypeError:
    print('invalid value')
except ValueError:
    print('invalid value')