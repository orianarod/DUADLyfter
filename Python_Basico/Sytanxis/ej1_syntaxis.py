my_text1 = "Hello"
my_text2 = "World"
my_integer1 = 10
my_integer2 = 20
my_float1 = 3.14
my_float2 = 2.71
my_boolean1 = True
my_boolean2 = False
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

my_combined_text = my_text1 + my_text2  
my_integer_sum = my_integer1 + my_integer2
my_float_sum = my_float1 + my_float2
my_boolean_sum = my_boolean1 + my_boolean2
my_boolean_multiplication = my_boolean1 * my_boolean2
my_list_combined = my_list1 + my_list2

# integer_text_sum = my_text1 + my_integer1
# ERROR: TypeError: can only concatenate str (not "int") to str
# Solution: Convert the integer to a string before concatenation or get the length of the string and add it to the integer
integer_text_sum1 = my_text1 + str(my_integer1)
integer_text_sum2 = len(my_text1) + my_integer1
integer_float_sum = my_integer1 + my_float1
boolean_integer_sum = my_boolean1 + my_integer1
boolean_or = my_boolean1 or my_boolean2
boolean_and = my_boolean1 and my_boolean2

# list_text_sum = my_list1 + my_text1
# ERROR: TypeError: can only concatenate list (not "str") to list
# Solution: Convert the string to a list before concatenation
list_text_sum = my_list1 + [my_text1]

print("Combined Text:", my_combined_text) # concatenation of two strings (results in a string)
print("Integer Sum:", my_integer_sum)  #addition of two integers (results in an integer)
print("Float Sum:", my_float_sum)   # addition of two floats (results in a float)
print("Boolean Sum:", my_boolean_sum) # addition of two booleans (results in an integer were true is treated as 1 and false as 0)
print("Boolean Multiplication:", my_boolean_multiplication) # multiplication of two booleans (results in a integer were true is treated as 1 and false as 0)
print("Boolean OR:", boolean_or) # logical OR of two booleans (results in a boolean)
print("Boolean AND:", boolean_and) # logical AND of two booleans (results in a boolean)
print("List Combined:", my_list_combined) # concatenation of two lists (results in a list that combines both lists)
print("Integer + Text (Method 1):", integer_text_sum1) # concatenation of an integer and a string (results in a string)
print("Integer + Text (Method 2):", integer_text_sum2) # addition of the length of a string and an integer (results in an integer)
print("Integer + Float:", integer_float_sum) # addition of an integer and a float (results in a float)
print("Boolean + Integer:", boolean_integer_sum) # addition of a boolean and an integer (results in an integer) | true is treated as 1 and false as 0
print("List + Text:", list_text_sum) # concatenation of a list and a string (results in a list that combines the list and the string as a single element of the new list) 
