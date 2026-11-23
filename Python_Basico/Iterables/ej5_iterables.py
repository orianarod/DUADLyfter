number_list = []

for index in range(10) :
    number_list.append(int(input('Enter a number: ')))

    if index==0:
        highest = number_list [index]
        
    if number_list[index] > highest:
        highest = number_list [index]

print(f'{number_list}. The highest number was: {highest}')
