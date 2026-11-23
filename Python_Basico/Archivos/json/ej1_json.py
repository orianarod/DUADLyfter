import json

#imports the data from the json file into a data variable
def import_json_data(file_name):

    try:
        with open(file_name, 'r',encoding='utf-8') as json_file:
            file_data=json.load(json_file)
            pokemons=file_data['pokemons']
            dict_keys,type_list_keys,type_dict_keys,type_bool_keys=get_dict_keys(pokemons)
        return pokemons,dict_keys,type_list_keys,type_dict_keys,type_bool_keys
    except json.JSONDecodeError as error:
        print(f"Unexpected error while reading '{file_name}'.")
        print(error)
        print("Please address the background error and try again")
        exit()
        
#obtains the dictionary keys 
def get_dict_keys(pokemons):
    dict_keys=pokemons[0].keys()
    type_list_keys=[]
    type_dict_keys={}
    type_bool_keys=[]

    #save the data types of each key and storage them so they can be handled later
    for key in pokemons[0]:

        if isinstance(pokemons[0][key], bool ):
            type_bool_keys.append(key)

        if isinstance(pokemons[0][key], list):
            type_list_keys.append(key)

        if isinstance(pokemons[0][key], dict):
            type_dict_keys[key]=[]
            
            for sub_key in pokemons[0][key]:
                type_dict_keys[key].append(sub_key)

    return dict_keys,type_list_keys,type_dict_keys,type_bool_keys

#displays the stored pokemons
def display_pokemons(pokemons):
    print('These are the current pokemons in file: ')
    for pokemon in pokemons:
        print(f'{pokemon}:...')


def add_new_element(pokemons,dict_keys,type_list_keys,type_dict_keys,type_bool_keys):

    while add_new_element_request(pokemons):
        new_pokemon=create_new_pokemon(dict_keys,type_list_keys,type_dict_keys,type_bool_keys)
        pokemons.append(new_pokemon)
    return pokemons


#determines if the users wants to add a new pokemon to the file
def add_new_element_request(pokemons):

    display_pokemons(pokemons)

    while True:
        try:
            add_new=input('Do you want to add a new pokemon to the file? (Y/N)').upper().strip()
                    
            if add_new == 'Y':
                return True
            elif add_new == 'N':
                return False
            else:
                raise ValueError('Not a valid answer. Y for Yes and N for No')

        except ValueError as error:
                    print(error)


#creates a new element for the pokemon
def create_new_pokemon(dict_keys,type_list_keys,type_dict_keys,type_bool_keys):
    new_pokemon={}

    for key in dict_keys:
    
        if key in type_bool_keys:
            need_value=True
            while need_value:
                try:
                    is_true=input(f'{key} (Y/N)').upper().strip()
                    if is_true == 'Y':
                        new_pokemon[key]=True
                        need_value=False
                    elif is_true == 'N':
                        new_pokemon[key]=False
                        need_value=False
                    else:
                        raise ValueError('Not a valid answer. Y for Yes and N for No')
                except ValueError as error:
                    print(error)
        
        elif key in type_list_keys: 
            for value in type_list_keys:
                new_pokemon[key]=input(f'{key} (Separate skills by comma ","): ').rsplit(',')
        elif key in type_dict_keys.keys():
            new_pokemon[key]={}
            print(f'{key}:')

            for sub_key in type_dict_keys[key]:                
                new_pokemon[key][sub_key]=input(f'\t {sub_key}: ')                
        else:
            new_pokemon[key]=input(f'{key}: ')
        
    return new_pokemon


def export_to_json(new_pokemons, file_name):

    with open(file_name, 'w', encoding='utf-8') as json_file:
        file_data={"pokemons": new_pokemons}
        json_string=json.dumps(file_data,indent=4)
        json_file.write(json_string)


def main():    

    file_name='pokemons.json'
    pokemons,dict_keys,type_list_keys,type_dict_keys,type_bool_keys=import_json_data(file_name) 
    original_file_length=len(pokemons)
    new_pokemons=add_new_element(pokemons,dict_keys,type_list_keys,type_dict_keys,type_bool_keys)
    
    if len(new_pokemons) != original_file_length:
        export_to_json(new_pokemons, file_name)
    else:
        print("You didn't add any new pokemons to the file.")

    print('BYE!')
    


if __name__=='__main__':
    main()


