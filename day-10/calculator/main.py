from art import logo
import calculator as calc

def calculator():
    print(logo)

    first_value = float(input('First number: '))

    for operation in calc.operations:
        print(operation)
    
    should_continue = True

    while should_continue:

        operation = input('Pick an operation from the line above: ')
        second_value = float(input('Next value: '))

        function = calc.operations[operation]
        answer = function(first_value, second_value)

        print(f'{first_value} {operation} {second_value} = {answer} ')
        aswr = input(f'Type \'y\' to continue calculating with {answer} or \'n\' to start a new calculation or \'exit\' to close the application: ').lower()

        if aswr == 'y':
            first_value = answer
        elif aswr == 'n':
            calculator()
        elif aswr == 'exit':
            should_continue = False
