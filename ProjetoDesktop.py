import datetime
from tzlocal import get_localzone
import json
from time import sleep

#listas e bancos de dados:
database = {usuario: senha}
notas = {}
menu_inicio = ["Bloco de Notas", "Calculadora", "Data e Hora", "Mudar Nome/Senha", "sair"]

def carregar_dados():
    try:
        with open("dados_usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


def salvar_dados():
    with open("dados_usuarios.json", "w") as arquivo:
        json.dump(database, arquivo)

#função bloco de notas
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
                print("Notas Salvas")
                print(notas)
        elif b1 == "3":
            print("Saindo do Bloco de Notas...")
            return


#Função calculadora
def realizar_operacoes():
    continuar = True

    while continuar:
        # Inicializa o resultado intermediário como zero
        resultado_intermediario = 0
        print("\nCALCULADORA")
        # Operação
        print("\nNova Operação")
        
        num1 = float(input("\nDigite o primeiro número: "))
        operacao = input("\nEscolha a operação (+, -, *, /)")
        num2 = float(input("\nDigite o segundo número:"))

        numeros = [num1, num2]

        resultado = numeros[0]

        for i in range(1, len(numeros)):
            if operacao == '+':
                resultado += numeros[i]
            elif operacao == '-':
                resultado -= numeros[i]
            elif operacao == '*':
                resultado *= numeros[i]
            elif operacao == '/':
                if numeros[i] != 0:
                    resultado /= numeros[i]
                else:
                    resultado = "Não é possível dividir por zero!"
            break

        # Atualiza o resultado intermediário
        resultado_intermediario = resultado

        print("Resultado da operação:", resultado_intermediario)
        sair = str(input("\nDeseja voltar ao menu? [s/n]"))
        if sair == "s":
            return


#Função data e hora
def data_hora():
    fuzo_horario = get_localzone()
    data_hora_atual = datetime.datetime.now(fuzo_horario)

    data_hora_formatada = data_hora_atual.strftime("%d/%m/%y--%H:%M:%S--%Z")
    print("Data e hora atual: ", data_hora_formatada)


#Função mudar senha e login
def mudar_nome_senha():
    username = input("Digite seu nome de usuário atual: ")
    password = input("Digite sua senha atual: ")

    if username in database and database[username] == password:
        novo_username = input("Digite o novo nome de usuário: ")

        if novo_username in database:
            print(" Esse nome de usuário ja esta em uso. escolha outro.")
            return

        novo_password = input("Digite a nova senha: ")

        database[novo_username] = novo_password
        del database[username]

        print("Nome de usuário e senha alterados com sucesso!")
    else:
        print("Nome de usuário e senha incorretos.Tente novamente!")





#inicio do Desktop
while True:
    database = carregar_dados()
    print("""
01 - FAZER LOGIN 
02 - FAZER REGISTRO
03 - DESLIGAR
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

    if inicio == "2":
        print("Fazer Registro.")
        register()
    elif inicio == "1":
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
                    realizar_operacoes()
                elif escolha == "3":
                    data_hora()
                elif escolha == "4":
                    mudar_nome_senha()
                elif escolha == "5":
                    break
                else:
                    print("\nResposta inválida!\n")

        else:
            print("Falha ao fazer login.")
    elif inicio == "3":
        print("Desligando o programa...")
        sleep(2)
        break

    else:
        print("\nResposta inválida!\n")

    salvar_dados()

