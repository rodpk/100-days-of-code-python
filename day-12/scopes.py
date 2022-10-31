enemies = 1

def increase_enemies():
    enemies = 2
    print(f'enemies inside function: {enemies}')

increase_enemies()
print(f'enemies outside function: {enemies}')





# Local Scope
# existing within functions


def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()


#global scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)



def outer_funct():
    outer_var = 'outer_var'

    def inner_funct():
        print(outer_var)
    
    inner_funct()

outer_funct()


## the is no block scope (if, while, for, etc)

level = 3
enemies = ['skeleton', 'zombie', 'alien']

if level < 5:
    new_enemy = enemies[0]

print(new_enemy)


print('----------------------------------')

# modifying global scope

enemies = 1

def increase_enemies():
    #enemies = 2 # create a new variable in local scope - it is not recommended name
    # should explicit say its referencing the global variable:
    global enemies
    enemies += 1
    print(f'enemies inside function: {enemies}')

increase_enemies()
print(f'enemies outside function: {enemies}')



# Global constants

PI = 3.14159
URL = "https://www.google.com.br"

def calc():
    print(URL)


calc()