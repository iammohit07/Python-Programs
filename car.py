print('*' * 10 + ' Welcome to Program ' + '*' * 10)
print("""COMMANDS :  
help 
start
stop
quit
""")
started = False
stopped = False
while True :
    command = input('Enter the command : ').lower()
    if command == "help":
        print("""
help ~ for help
start ~ to stop the car
stop ~ to stop the car
quit ~ to quit 
        """)
    elif command == "start":
        if started:
            print('car is already started ')
        else:
            started = True
            print('car started !! ')
    elif command == "stop":
        if stopped:
            print('car is already stopped ')
        else:
            stopped = True
            print('car stopped !! ')
    elif command == "quit":
        break
    else:
        print('enter valid command ')