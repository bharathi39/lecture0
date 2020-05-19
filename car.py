onned = False
while True:
    command = input("cmd = ").lower()
    if command == "on":
        if onned:
            print("is already on !")
        else:
            onned = Trueon
            print("is on")
    elif command == "off":
        if not onned:
            print("is already off !")
        else:
            onned = False
            print("is off")
    elif command == "help":
        print('''
on - switches on
off - switches off
qui - breaks        
        ''')
    elif command == "qui":
        break
    else:
        print("Sorry, i don't understand")



