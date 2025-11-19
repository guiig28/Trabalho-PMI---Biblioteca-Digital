#Imports
from .user import user_data, user_list, logged_in_user, update_user

book_data = ("title", "quantity")
library = [{book_data[0]: "titulo 1", book_data[1]: 3}, {book_data[0]: "titulo 2", book_data[1]: 8}, {book_data[0]: "titulo 3", book_data[1]: 1}]

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
    if title in logged_in_user[user_data[2]]:
            print(f"\nLivro {title} ja alugado pelo usuário.")
    else:
        avaible_book = False
        for i in range(len(library)):
            if library[i][book_data[0]] == title:
                if library[i][book_data[1]] > 0:
                    library[i][book_data[1]] -= 1

                    logged_in_user[user_data[2]].append(title)

                    update_user() 
                    avaible_book = True
                    print(f"\nLivro {title} alugado com sucesso.")

                break                
            
        if not avaible_book:
            print(f"\nLivro {title} não disponível na biblioteca.")

def return_book(title):
    if title in logged_in_user[user_data[2]]:
        logged_in_user[user_data[2]].remove(title)

        found_book = False
        for i in range(len(library)):
            if library[i][book_data[0]] == title:
                library[i][book_data[1]] += 1
                found_book = True
                break

        if not found_book:
            library.append({book_data[0]: title, book_data[1]: 1})

        print(f"\nLivro {title} devolvido com sucesso.")
    else:
        print(f"\nLivro {title} não encontrado.")

def find_book_by_title(title):
    books_in_library = 0
    books_with_user = 0

    for b in library:
        if b[book_data[0]] == title:
            books_in_library += b[book_data[1]]
            break

    print(f"\nTítulo: {title} \n\nEm estoque na biblioteca: {books_in_library}\n")

    for u in user_list:
        if title in u[user_data[2]]:
            print(f"Usuário: {u[user_data[0]]} | Alugado: 1")
            books_with_user += 1

    print(f"\nTotal: {books_in_library + books_with_user}")

def lib_stats():
    books_avaible = 0
    total_books = 0

    for b in library:
        title = b[book_data[0]]
        avaible = b[book_data[1]]
        total = b[book_data[1]]
        

        for u in user_list:
            if title in u[user_data[2]]:
                total += 1

        books_avaible += avaible
        total_books += total

        print(f"\n\nTítulo: {title}")
        print(f"\nDispovíveis para alugar: {avaible}")
        print(f"\nTotal de cópias: {total}")

    print(f"\n\nLivros disponíveis para alugar: {books_avaible}")
    print(f"\n\nTotal: {total_books}")
