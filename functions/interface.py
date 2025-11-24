#Imports
from .user import login, logoff, register, register_adm, logged_in_user, user_data
from .book import show_user_books, show_library, rent_book, return_book, add_book_to_lib, rmv_book_from_lib, find_book_by_title, lib_stats

def menu_logged_off():
    print("\nEscolha uma opção:\n")
    print("1 - Login")
    print("2 - Registrar usuário")
    print("3 - Registrar admin")
    print("0 - Encerrar programa")
        
    opc = input("\nOPC: ")

    match opc:
        case "1":
            login()
            return [True, True] #[logged_in, app_is_on]
        case "2":
            register()
            return [False, True]
        case "3":
            register_adm()
            return [False, True]
        case "0":
            return [False, False]
        case _:
            print("Opção inválida.")
            return [False, True]
               
def menu_logged_in():
    print("\nEscolha uma opção:\n")
    print("1 - Mostrar livros alugados")
    print("2 - Mostrar biblioteca")
    print("3 - Alugar livro")
    print("4 - Devolver livro")
    if logged_in_user[0][user_data[3]] == "adm":
        print("5 - Adicionar livros à biblioteca")
        print("6 - Remover livros da biblioteca")
        print("7 - Procurar livro por nome")
        print("8 - Estatísticas")
    print("9 - Logout")
    print("0 - Encerrar programa")

    opc = input("\nOPC: ")

    match opc:
        case "1":
            show_user_books()
            return [True, True]
        case "2":
            show_library()
            return [True, True]
        case "3":
            t = input("\nDigite o título do livro a ser alugado: ")
            rent_book(t)
            return [True, True]
        case "4":
            t = input("\nDigite o título do livro a ser devolvido: ")
            return_book(t)
            return [True, True]
        case "5" if logged_in_user[0][user_data[3]] == "adm":
            add_book_to_lib()
            return [True, True]
        case "6" if logged_in_user[0][user_data[3]] == "adm":
            rmv_book_from_lib()
            return [True, True]
        case "7" if logged_in_user[0][user_data[3]] == "adm":
            t = input("\nDigite o título do livro:")
            find_book_by_title(t)
            return [True, True]
        case "8" if logged_in_user[0][user_data[3]] == "adm":
            lib_stats()
            return [True, True]
        case "9":
            logoff()
            return [False, True]
        case "0":
            return [False, False]
        case _:
            print("\nOpção inválida.")
            return [True, True]