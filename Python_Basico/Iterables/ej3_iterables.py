my_list =  [ 1, 2, 3, 4, 5]

if len(my_list) > 1 :
    first_element = my_list.pop(0)
    last_element = my_list.pop(len(my_list)-1)
    my_list.insert(0,last_element)
    my_list.append(first_element)

print(my_list)
