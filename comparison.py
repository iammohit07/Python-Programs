# temp = int(input('enter the temperature in celcius : '))
# if temp  >= 50 :
#     print('Its too hot ')
# elif temp <= 10:
#     print('freezing cold ')
# else:
#     print('normal day')
name = str(input('enter the name : '))
if len(name)  <= 3 :
    print(' name must be more than 3 charcaters ')
elif len(name) >= 50 :
    print(' max charcter limit reached ')
else:
    print('good name ')