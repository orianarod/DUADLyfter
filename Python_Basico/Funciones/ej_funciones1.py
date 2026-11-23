def first_printing_function():
    second_printing_function()
    print("This is my first printed message")


def second_printing_function():
    print('This is my second printed message')


def main():
    first_printing_function()

if __name__ == '__main__':
    main()
