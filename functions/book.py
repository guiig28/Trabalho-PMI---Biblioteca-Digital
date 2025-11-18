#Imports
from .user import user_data, logged_in_user, update_user

book_data = ("title", "quantity")
library = [{book_data[0]: "titulo 1", book_data[1]: 3}, {book_data[0]: "titulo 2", book_data[1]: 8}]

def add_book_to_lib(title: str, qt: int):
    found_book = False

    for i in range(len(library)):
        if library[i][book_data[0]] == title:
            library[i][book_data[1]] += qt
            found_book = True
            break

    if not found_book: 
        library.append({book_data[0]: title, book_data[1]: qt})

    print("\nLivro adicionado à biblioteca.")

def rmv_book_from_lib(title: str, qt: int):
    found_book = False

    for i in range(len(library)):
        if library[i][book_data[0]] == title:
            library[i][book_data[1]] -= qt
            found_book = True

            if library[i][book_data[1]] <= 0:
                library.pop(i)

            break

    if found_book: 
        print("\nLivro removido com sucesso.")
    else:
        print("\nLivro não encontrado.")

def rent_book(title):
    for i in range(len(library)):
        if title in logged_in_user[user_data[2]]:
            print("\nLivro ja alugado pelo usuário.")
        else:
            if library[i][book_data[0]] == title:
                library[i][book_data[1]] -= 1

                if library[i][book_data[1]] == 0:
                    library.pop(i)     

                logged_in_user[user_data[2]].append(title)    
                update_user() 
            else:
                print("\nLivro não disponível na biblioteca.")