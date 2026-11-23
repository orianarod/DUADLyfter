my_list =  [ 1, 2, 3, 4, 5, 6]
my_even_list = []

for index in range(0, len(my_list)) :

    if my_list[index]%2 == 0 :
        my_even_list.append(my_list[index])
    
print(my_even_list)
    
