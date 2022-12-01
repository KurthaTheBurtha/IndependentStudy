#Create your menu here
menu = ['burger', 'fries','shake','soda','lemonade']
reservation_times = ['12:00','1:00','2:00','3:00']

# print_options should print options available to users
# see exercise description for more details
def print_options():
    print('1. Take a look at the menu')
    print('2. Ask about daily specials')
    print('3. Make a reservation')
    print('4. order take out')
    print('5. exit')

def print_menu():
    print()
    num = 1
    for x in menu:
        print(str(num), end=". ")
        print(x)
        num = num + 1
    print()

def reservations():
    print()
    print('Here are the available times')
    num = 1
    for x in reservation_times:
        print(str(num), end=". ")
        print(x)
        num = num + 1
    print()
    choice = input('which time would you like?')
    while choice not in reservation_times:
        choice = input('Please enter a valid reservation time')
    print('You are set to go for ' + choice)
    reservation_times.remove(choice)

def make_order():
    print()
    num = 1
    order = []
    for x in menu:
        print(str(num), end=". ")
        print(x)
        num = num + 1
    print()
    choice = input('which one would you like?')
    while choice not in menu:
        choice = input('Please enter a valid menu item')
    order.append(choice)
    another = input('would you like anything else?: yes or no')
    while(another!='no'):
        choice = input('which one would you like?')
        while choice not in menu:
            choice = input('Please enter a valid menu item')
        order.append(choice)
        another = input('would you like anything else?: yes or no')
    print('Here is your order:')
    num = 1
    for x in order:
        print(str(num), end=". ")
        print(x)
        num = num + 1


print_options()
options = ['1','2','3','4','5']
user = input('make a choice: ')
while user not in options:
    user = input('Please enter a valid menu item')
if user == '5':
    print('Thank you for orderingQ')
else:
    while user!= '5':
        if user == '1':
            print_menu()
            user = input('would you like to do anything else?: ')
            while user not in options:
                user = input('Please enter a valid menu item')
        if user == '2':
            print()
            print('The special for today is the ShakeStack burger')
            print()
            user = input('would you like to do anything else?: ')
            while user not in options:
                user = input('Please enter a valid menu item')
        if user == '3':
            reservations()
            user = input('would you like to do anything else?: ')
            while user not in options:
                user = input('Please enter a valid menu item')
        if user == '4':
            make_order()
            user = input('would you like to do anything else?: ')
            while user not in options:
                user = input('Please enter a valid menu item')
        if user == '5':
            print('thank you for ordering')
            break
