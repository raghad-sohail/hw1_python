name = input('Add your name: \n')
if not name.isalpha() and name == '':
    print('you should enter a valid name')

age = input('Add your age: \n')
if not age.isdigit() and age == '':
    print('you should enter an age')

address = input('Add your address: \n')
if address == '':
    print('You should enter a valid address')

print(f'Hello Mr/Ms {name} age {age} located in {address}.\n Thanks for beening one of our community, \n Enjoy ...')
