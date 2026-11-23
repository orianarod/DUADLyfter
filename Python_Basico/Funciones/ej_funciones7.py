#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
#Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

def is_prime(number):
    prime_number= True

    for divisor in range(2,number):
        if number%divisor==0:
            prime_number= False
            break
    
    return prime_number


def prime_numbers(numbers_list):
    prime_numbers_list=[]
    
    for number in numbers_list:
        if number>=2 and is_prime(number):
            prime_numbers_list.append(number)
    
    return prime_numbers_list


def main():
    numbers_list=[67,48,91,50,3,107,37,1,0]
    print(prime_numbers(numbers_list))
    

if __name__=='__main__':
    main()
