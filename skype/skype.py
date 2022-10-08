from conta import Conta

def main():

    # Logar na aplicação
    # ------------------
    print("Logue no Skype")
    email = input("Email: ")
    senha = input("Senha: ")
    my_account = Conta(email, senha)


    # Consultar chat de mensagens
    # ---------------------------
    contato = my_account.ler_mensagens()


    # Enviar mensagens
    # ----------------
    my_account.enviar('mensagem', contato)


if (__name__ == '__main__'):
    main()