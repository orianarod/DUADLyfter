keys_list = ['experience', 'role',] 
employee = {
    'first_name': 'Oriana', 
    'last_name':'Rodriguez', 
    'experience': 2,
    'role': 'Developer'}

print(f'Original employee data: {employee}' )
for key in keys_list:
    employee.pop(key)

print(f'Modified employee data: {employee}')

