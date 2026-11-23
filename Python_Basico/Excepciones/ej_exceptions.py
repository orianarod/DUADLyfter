def display_menu(result):
    print('(1) Addition + ')
    print('(2) Subtraction -')
    print('(3) Multiplication *')
    print('(4) Division / ' )
    print('(5) Delete ')
    print('(6) Exit')
    print(f'* RESULT: ********')
    print(f'*      {result}         *')
    print('******************')


def select_operation():
    while True:
        try:
            operation=int(input('Select an operation (Choose a number between 1 and 6): '))
            
            if operation<1 or operation>6:
                raise ValueError(f"-- ERROR:  {operation} isn't a valid option")

            return operation
    
        except ValueError as error:
            print(error,'Please try again')



def validate_number():
    while True:
        try:
            number=float(input('Provide a real number: '))
            break
        except ValueError as error:
            print(f'-- ERROR: {error} -- Please provide numerical value!')  
    return number


def addition(result, number):
    result += number
    return result


def subtraction(result, number):
    result -= number
    return result

def multiplication(result, number):
    result=result * number
    return result

def division(result, number):
    try:
        result = result / number
    except ZeroDivisionError:
        print("-- ERROR: Zero division is not possible \n")
    return result


def calculator():
    result = 0

    while True:

        display_menu(result)

        try:
            operation=select_operation()

            if operation==5: #delete
                result=0
                continue

            elif operation==6:
                break

            number=validate_number()
            
            match operation:

                case 1: #addition
                    result=addition(result, number)
                case 2: #subtraction
                    result=subtraction(result, number)
                case 3: #multiplication
                    result=multiplication(result, number)
                case 4: #division
                    result=division(result, number)

        except ValueError:
            continue

    print("BYE!")

def main():
    try:     
        calculator()    
    except Exception as error:
        print("An error has been found: ")
        print(error)


if __name__ == '__main__':
    main()

