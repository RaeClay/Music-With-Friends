integer = input('Type an integer')
try:
    if int(integer) % 2 == 0:
        print('Even')
    else:
        print('Odd')
except:
    print("That's not an integer")