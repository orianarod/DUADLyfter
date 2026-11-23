

for iteration in range(3) :
    number = int(input ("Please enter a number: "))

    if iteration == 0:
        highest = number
    
    if number > highest :
        highest = number

print(f"The highest number is: {highest}")