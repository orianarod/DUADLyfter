def reverse_string(my_string):
    reversed_string =''

    for index in range(len(my_string)-1,-1,-1):
        reversed_string = reversed_string + my_string[index]

    return reversed_string

    
def main():
    my_string = "I'm going in reverse!"
    print(reverse_string(my_string))


if __name__ == '__main__':
    main()

