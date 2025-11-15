user_list = [['teste', '123', []]]
logged_in_user = ['teste', '123', []]

def register():
    while True: #Verificando se o nome de usuário é único
        un_exists = False
        username = input("\nDigite seu nome de usuário: ")

        for u in user_list:
            if u[0] == username:
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

    user_list.append([username, password, []]) #[usuário, senha, lista de livros cadastrados[]]
    print("\nUsário cadastrado com sucesso.")

def update_user():
    i = user_list.index([logged_in_user[0]])
    user_list[i] = logged_in_user

def logoff():
    logged_in_user.clear()

def login():
    logoff()

    username = input("\nDigite seu nome de usuário: ")
    password = input("\nDigite sua senha: ")

    for u in user_list:
        if u[0] == username: #Validando usuário 
            if u[1] == password: #Validando senha
                logged_in_user.append(u[0])
                logged_in_user.append(u[1])
                logged_in_user.append(u[3])

                print("\nLogin efetuado com sucesso.")

            break

    if len(logged_in_user) == 0:
        print("\nUsuário ou senha inválidos.")


