#imports
from functions import interface, user, book
    
user.load_users()
book.load_books()

logged_in = False

while True:
    app_is_on = True
    
    if not logged_in:
        returns = interface.menu_logged_off()
        logged_in = returns[0]
        app_is_on = returns[1]
    else:
        returns = interface.menu_logged_in()
        logged_in = returns[0]
        app_is_on = returns[1]

    if app_is_on == False:
        print("Encerrando Programa.")
        break
