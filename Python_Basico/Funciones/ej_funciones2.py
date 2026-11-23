my_global_var = "I am global"

def change_global_without_global():
    my_global_var = "I've been changed"


def change_global_with_global():
    global my_global_var 
    my_global_var = "I've been changed using global"


def my_scope_function():
    my_local_var="I am local"
    print(f"Inside my function, global variable is {my_global_var} and function local variable is {my_local_var}")
    #works perfectly fine because a global variable is defined for the whole code


def main():
    print(f'Original global variable value is: {my_global_var}')
    change_global_without_global()
    print(f"After calling change_global_without_global, global variable is: {my_global_var}")
    #The value doesn't change because is taken by the function as local variable since it "global" isn't indicated
    change_global_with_global()
    print(f"After calling change_global_without_global, global variable is: {my_global_var}")
    my_scope_function()
    #The value of the global variable changes because it is addressed as so in the scope of the function
    print(f"Output my function, global variable is: {my_global_var} and the function local variable is: {my_local_var}")
    #it generates a NameError because the local variable is not defined for the global scope

if __name__ == '__main__':
    main()

    #The output only prints what is inside the function. The second print fails and crashes the program