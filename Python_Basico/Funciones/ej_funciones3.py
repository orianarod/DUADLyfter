def list_sum(list_parameter):
    number_sum = 0
    
    for number in list_parameter:
        number_sum += number

    return number_sum


def main():
    list_parameter = [20, 6, 8, 4]
    print(f'The sum of : {list_parameter} is {list_sum(list_parameter)}')


if __name__ == '__main__':
    main()

