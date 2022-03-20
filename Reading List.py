def main():

    prompt = input("Do you want to add or delete a title? a = add, d = delete ")
    
    if prompt == 'a':
        addToList()
    elif prompt == 'd':
        deleteItem()
    with open(r"reading list.txt", 'r+') as reading_list:
        print(reading_list)
def addToList():

    reading_list = []

    file = open("reading list.txt", 'a')
    
    again = 'y'

    while again == 'y':

        book_name = input("Title: ")

        reading_list.append(book_name)

        again = input("Continue? y = yes, anything else = no. ")

    for book in reading_list:
        
        file.write(book + '\n')

    file.close()

def deleteItem():
    
    reading_list = open(r"reading list.txt", 'r')

    lines = reading_list.readlines()

    reading_list.close()

    book_name = input("Title: ")

    new_rl = open(r"reading list.txt", 'w+')

    for line in lines:

        if line.strip('\n') != book_name:

            new_rl.write(line)

    new_rl.close()
    
      
    
            
                
    
    
if __name__ == '__main__':
    main()
