#imports
import json

user_data = ("username", "password", "booklist", "role")
user_role = ("user", "adm")
user_list = []
logged_in_user = []

def register():
    while True: #Verificando se o nome de usuário é único
        un_exists = False
        username = input("\nDigite seu nome de usuário: ")

        for u in user_list:
            if u[user_data[0]] == username:
                un_exists = True
                print("\nNome de usuário já existente.")

        if not un_exists:
            break

    while True: #Validando senha
        password = input("\nDigite sua senha: ")
        conf_password = input("\nConfirme sua senha: ")

        if password != conf_password:
            print("\nAs senhas são diferentes.")
        else:
            break

    user_list.append({user_data[0]: username, user_data[1]: password, user_data[2]: [], user_data[3]: user_role[0]}) 
    update_user()
    print("\nUsário cadastrado com sucesso.")

def register_adm():
    while True: #Verificando se o nome de usuário é único
        un_exists = False
        username = input("\nDigite seu nome de usuário: ")

        for u in user_list:
            if u[user_data[0]] == username:
                un_exists = True
                print("\nNome de usuário já existente.")

        if not un_exists:
            break

    while True: #Validando senha
        password = input("\nDigite sua senha: ")
        conf_password = input("\nConfirme sua senha: ")

        if password != conf_password:
            print("\nAs senhas são diferentes.")
        else:
            break

    user_list.append({user_data[0]: username, user_data[1]: password, user_data[2]: [], user_data[3]: user_role[1]})
    update_user() 
    print("\nAdmin cadastrado com sucesso.")

def update_user():
    if len(logged_in_user)> 0:
        for i in range(len(user_list)):
            if user_list[i][user_data[0]] == logged_in_user[0][user_data[0]]: 
                user_list[i] = logged_in_user[0]

    with open('data/users.json', 'w') as users_json:
        json.dump(user_list, users_json, indent=4)

def load_users():
    with open('data/users.json', 'r', encoding='utf-8') as users_json:
        data = json.load(users_json)

    user_list.extend(data)        

def logoff():
    logged_in_user.clear()
    print("\nEncerrando sessão")
       


def login():
    logoff()

    while len(logged_in_user) == 0:
        username = input("\nDigite seu nome de usuário: ")
        password = input("\nDigite sua senha: ")

        for u in user_list:
            if u[user_data[0]] == username: #Validando usuário 
                if u[user_data[1]] == password: #Validando senha
                    print("\nLogin efetuado com sucesso.")
                    logged_in_user.append(u)

        if len(logged_in_user) == 0:
            print("\nUsuário ou senha inválidos.")
