from pathlib import Path
import csv

#ask the user how many games will be added to the file
def def_games_qty():

    not_acceptable_qty=True
    
    while not_acceptable_qty:
        try:
            games_qty=int(input('How many games will your file contain? '))
        
            if games_qty<1:
                raise ValueError('The list must contain at least 1 record.')
            else:
                not_acceptable_qty=False

            return games_qty

        except ValueError as error:
            print(f'{error}\n Provide a valid integer.') 


#returns a list with the games asking the user about the info of each game.
def create_games_list(games_qty):
    games_list=[]

    for game_number in range(games_qty):
        game={}
        print(f'Fill in data for game number {game_number+1}...')

        game['name']=input(f'NAME: ')
        game['genre']=input(f'GENRE: ')
        game['developer']=input(f'DEVELOPER: ')
        game['esrb_classification']=validate_esrb_classification()
        games_list.append(game)
            
    return games_list


#validates that the user is entering an existing ESRB classification
def validate_esrb_classification():
    esrb_classification_values=['EC','E','E10+','T','M','AO','RP']
    esrb_needed=True


    while esrb_needed:
        try:
            esrb_classification=input(f'ESRB Classification: ').strip().upper()
                
            if esrb_classification not in esrb_classification_values:
                raise ValueError(f"{esrb_classification}' doesn't match an ESRB Classification, please select a value in {esrb_classification_values}")

            esrb_needed=False
        
        except ValueError as error:
                print(error)

    return(esrb_classification)


#validates if the user is creating a new file and prompts him if he wants to 
#overwrite an existing one.
def validate_file_name():
    file_name_needed=True

    while file_name_needed:

        try:
            file_name=input('Please provide a name for your file: ').strip()

            if not file_name:
                raise ValueError('No file name provided. Please provide a name.')

            file_name=file_name+'.csv'

            if Path(file_name).exists():
                file_action_needed=True
                raise FileExistsError('Another file has the same name.')

            file_name_needed=False

        except ValueError as error:
            file_name_needed=True
            print(error)

        except FileExistsError as error:
            while file_action_needed:
                try:
                    user_overwrite_select=input(f"{error} Would you like to overwrite it? (Y/N): ").upper().lstrip().rstrip()
                    
                    if user_overwrite_select == 'Y':
                        file_action_needed=False
                        file_name_needed=False
                    elif user_overwrite_select == 'N':
                        file_action_needed=False
                    else:
                        raise ValueError('Not a valid answer. Y for Yes and N for No')

                except ValueError as error:
                    print(error)

    return file_name

#save the file in csv format
def save_csv_file(file_name, games_list):

    with open(file_name, 'w', encoding='utf-8', newline='') as csv_file:
        headers=games_list[0].keys()
        writer=csv.DictWriter(csv_file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(games_list)

    print(file_name + " has been saved!")
    

def main():
    try:
        games_qty=def_games_qty()
        games_list=create_games_list(games_qty)
        file_name=validate_file_name()
        save_csv_file(file_name,games_list)
    except Exception as error:
        print(f'An error has occurred: {error}')

if __name__=='__main__':
    main()