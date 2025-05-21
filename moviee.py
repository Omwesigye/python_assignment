age = int(input('enter your age'))
if age >= 18:
    print('you are an adult')
    hastocket = input('any ticket? (yes/no)')
    if hastocket.lower() == "yes":
        print('u can watch')
    else:
        print("u cant with out ticket")
else:
    print(" u are below 18 u  cant watch")
               
    