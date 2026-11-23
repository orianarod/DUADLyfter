#Reads the file and creates a list where each element is a line of the file
#returns the list
def read_file(original_file):
    with open(original_file, 'r') as file:
        data=file.readlines()
    return data


#reads the a list and add each element as new line
def create_new_file(new_file, data):
    #creates a new file with the given name or overwrites an existing homonym file with the new data
    with open(new_file, 'w', newline='\n') as file:
        for line in data:
            #it removes the \n and adds a new one to guarantee each element is in a new line and there's no more than 1 break
            file.write(line.rstrip('\n')+'\n')


def main():
    #defines variable for the file paths to make the code more readable
    #using relative paths the files
    original_file='songs.txt' 
    new_file='ordered_songs.txt'

    #calls the read_file function and assigns its return value to the variable data
    data=read_file(original_file)
    #sorts the values in the list data alphabetically
    data.sort()
    #passes the ordered data to the create_new_file function to create the new file.
    create_new_file(new_file,data)

if __name__=='__main__':
    main()


