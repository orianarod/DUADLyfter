#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
#“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
def count_cases(my_string):
    upper_cases=0
    lower_cases=0
    
    for letter in my_string:
        
        if letter.isupper():
            upper_cases += 1
        elif letter.islower():
            lower_cases += 1
    
    print(f'There is {upper_cases} upper case(s) and {lower_cases} lower case(s)')


def main():
    count_cases('Ana Perez')


if __name__ == '__main__':
    main()
    
        
            