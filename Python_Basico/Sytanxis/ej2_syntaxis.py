surname = input("Enter your surname: ")
lastname = input("Enter your last name: ")
age = input("Enter your age: ") # TypeError: '<' not supported between instances of 'str' and 'int'
age = int(age) #must be turned to int to avoid TypeError

if age < 2 :
    print("You are a baby.")
elif age < 10 :
    print("You are a child.")
elif age < 13 :
    print("You are a preteen.")
elif age < 18 :
    print("You are a teenager.")
elif age < 30 : 
    print("You are a young adult.")
elif age < 60 :
    print("You are an adult.")
else :
    print("You are a senior citizen.")
