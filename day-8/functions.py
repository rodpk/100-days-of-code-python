def greet():
    print('Hello')
    print('how do you do?')
    print('isnt the wather nice today?')


greet()


def greet_with_name(name):
    print(f'Hello {name}')

greet_with_name('Rodrigo')


def greet_with(name, location):
    print(f'Hello {name}')
    print(f'You are in {location}')

greet_with('Rodrigo', 'Campinas')
greet_with(location='Campinas_2', name='Rodrigo_2')