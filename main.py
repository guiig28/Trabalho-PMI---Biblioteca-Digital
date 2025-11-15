#imports
from functions import user, book

# user.register()
# print(user.user_list)

# user.login()
# print(user.logged_in_user)
# user.logoff()
# print(user.logged_in_user)


print(user.user_list)
print(user.logged_in_user)

book.book_add("Livro 1")

print(user.user_list)
print(user.logged_in_user)



