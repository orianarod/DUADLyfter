keys_list = ['first_name', 'last_name', 'role'] 
values_list = ['Oriana', 'Rodriguez', 'Developer']
my_dictionary = {}

for index in range(0, len(keys_list)):
    my_dictionary[keys_list[index]] = values_list[index]

print(my_dictionary)

