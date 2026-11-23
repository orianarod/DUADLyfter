#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def order_words_alphabetically(word_list_string):
    word_list = word_list_string.rsplit("-")
    word_list.sort()
    ordered_word_list_string = "-".join(word_list)
    
    return ordered_word_list_string
    
    
def main():
    word_list_string = 'Charlie-Alpha-Delta-Bravo'
    ordered_word_list_string = order_words_alphabetically(word_list_string)
    print(f'Unordered list: {word_list_string}')
    print(f'Ordered list: {ordered_word_list_string}')
    
    
if __name__=='__main__':
    main()
        
   
    