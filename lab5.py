'''
lab5
if statement
'''

#3.1
alien_color = 'red'

if alien_color == 'green':
    print('you get 5 points')
    
#3.2
alien_color = 'red'

if alien_color == 'green':
    print('you get 5 points')
else:
    print('you get 10 points')

#3.3
favorite_fruits = ['apple', 'banana', 'peach']
if 'apple' in favorite_fruits:
    print('you really like apples')
if 'banana' in favorite_fruits:
    print('you really like bananas')
if 'peach' in favorite_fruits:
    print('you really like peaches')
    
#3.4
age = 45

if age<10:
    print('person is a kid')
elif age<20:
    print('person is a teenager')
else:
    print('person is an adult')
if 65<age:
    print('person is an elder')
