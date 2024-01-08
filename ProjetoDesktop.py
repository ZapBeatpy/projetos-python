usuario = "victor"
senha = "61613172"
database = {usuario: senha}
notas = {}
menu_inicio = ["Bloco de Notas", "Calculadora", "Data e Hora", "Mudar Nome/Senha", "Advinha", "sair"]

def bloco_notas():
    while True:
        print("BLOCO DE NOTAS")
        print("""
        [1]. Nova Nota
        [2]. Ver notas
        [3]. Sair
        """)
        b1 = str(input("Escolha uma Opção[1-3]: "))

        if b1 == "1":
            print("Nova Nota")
            titulo = str(input("").upper())
            conteudo = str(input(f"{titulo}\n"))
            notas[titulo] = conteudo
        elif b1 == "2":
            if not notas:
                print("Sem Notas")
            else:
                print(notas)
        elif b1 == "3":
            print("Saindo do Bloco de Notas...")
            return

while True:

    print("""
01 - FAZER LOGIN 
02 - FAZER REGISTRO.
    """)
    inicio = str(input(": ").lower())

    def register():
        username = input("Escolha um nome de usuário: ")

        while username in database:
            print("Este nome de usuário já está em uso. Tente outro.")
            username = input("Escolha um nome de usuário: ")

        password = input("Escolha uma senha: ")
        database[username] = password
        print("Registro bem-sucedido!")

    def login():
        username = input("Usuário: ")
        password = input("Senha: ")

        if username in database and database[username] == password:
            print("Login bem-sucedido! Bem-vindo,", username)
            return True
        else:
            print("Nome de usuário ou senha incorretos. Tente novamente.")
            return False

    if inicio == "registro":
        print("Fazer Registro.")
        register()
    elif inicio == "login":
        print("Fazer Login")
        logged_in = login()
        if logged_in:
            while True:
                for c, item in enumerate(menu_inicio, 1):
                    print(f"[{c}]. {item}")
                escolha = input("\nEscolha um Item: ")
                if escolha == "1":
                    bloco_notas()
                elif escolha == "2":
                    pass
                elif escolha == "3":
                    pass
                elif escolha == "4":
                    pass
                elif escolha == "5":
                    pass
                elif escolha == "6":
                    break
                else:
                    print("\nResposta inválida!\n")

        else:
            print("Falha ao fazer login.")
            break
    else:
        print("\nResposta inválida!\n")
        break
