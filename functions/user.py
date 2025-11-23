#imports
import json

user_data = ("username", "password", "booklist")
user_list = []
# logged_in_user: dict[str, any] = {user_data[0]: None, user_data[1]: None, user_data[2]: []}
logged_in_user: dict[str, any] = {user_data[0]: "teste", user_data[1]: "123", user_data[2]: ["titulo 1", "titulo 3"]}

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

    user_list.append({user_data[0]: username, user_data[1]: password, user_data[2]: []}) 
    print("\nUsário cadastrado com sucesso.")

def update_user():
    found_user = False
    for i in range(len(user_list)):
        if user_list[i][user_data[0]] == logged_in_user[user_data[0]]: 
            user_list[i] = logged_in_user
            found_user = True
    
    if not found_user:
        print("\nErro ao encontrar usuário.")

    with open('data/users.json', 'w') as users_json:
        json.dump(user_list, users_json, indent=4)

def load_users():
    with open('data/users.json', 'r', encoding='utf-8') as users_json:
        data = json.load(users_json)

    user_list.extend(data)



    

        

def logoff():
    if logged_in_user != {user_data[0]: None, user_data[1]: None, user_data[2]: []}:
       print("\nEncerrando sessão")
       return {user_data[0]: None, user_data[1]: None, user_data[2]: []}


def login():
    logoff()

    username = input("\nDigite seu nome de usuário: ")
    password = input("\nDigite sua senha: ")

    for u in user_list:
        if u[user_data[0]] == username: #Validando usuário 
            if u[user_data[1]] == password: #Validando senha
                print("\nLogin efetuado com sucesso.")
                return u

    if logged_in_user == {user_data[0]: None, user_data[1]: None, user_data[2]: []}:
        print("\nUsuário ou senha inválidos.")


