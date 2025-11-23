#imports
from functions import user, book

# user.register()
# print(user.user_list)

# user.logged_in_user = user.login()
# print(user.logged_in_user)
# user.logged_in_user = user.logoff()
# print(user.logged_in_user)

# print(book.library)
# book.add_book_to_lib("titulo 1", 2)
# book.add_book_to_lib("titulo 3", 4)
# print(book.library)
# book.rmv_book_from_lib("titulo 2", 3)
# book.rmv_book_from_lib("titulo 3", 4)
# print(book.library)

# book.rent_book("titulo 1")
# print(book.library)
# print(user.user_list)
# print(user.logged_in_user)
# book.rent_book("titulo 3")
# print(book.library)
# print(user.user_list)
# print(user.logged_in_user)
# book.return_book("titulo 3")
# print(book.library)
# print(user.user_list)
# print(user.logged_in_user)

# book.find_book_by_title("titulo 1")


book.load_books()
user.load_users()
print(book.library)
print(user.user_list)
