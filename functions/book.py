#Imports
from .user import logged_in_user, update_user

booklist: list = logged_in_user[2]

def book_add(title: str):
    if title in booklist:
        print("Livro ja existe na biblioteca.")
    else:
        booklist.append("title")
        print("Livro adicionado a biblioteca.")
