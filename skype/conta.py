import warnings

from skpy import Skype

class Conta:

    def __init__(self, email, password):
        self.__conta = Skype(email, password)
        self.contatos = self.__get_contatos()


    def __get_contatos(self):
        conversas = self.__conta.contacts

        contatos = []
        for contato in conversas:
            nome_completo = self.__get_contact_name(contato)

            contatos.append({
                "id": contato.id,
                "nome": nome_completo,
                "status": contato.mood
            })

        return contatos


    @staticmethod
    def __get_contact_name(contato):
        if (contato.name.last is not None):
            return "{} {}".format(contato.name.first, contato.name.last)
        else:
            return contato.name.first


    def ler_mensagens(self, contato = None):

        if (contato is None):
            print("\n" * 50)
            print("Escolha um contato para ver as mensagens:\n")
            self.lista_contatos()
            contato = self.__verifica_contato_escolhido()

        mensagens = []
        mensagens_contato = contato.chat.getMsgs()
        for mensagem in mensagens_contato:

            data_hora = mensagem.time.strftime("%d/%m/%Y %H:%M:%S")

            if (mensagem.type == 'RichText'):
                mensagens.append({
                    "data_hora": data_hora,
                    "conteudo": mensagem.plain,
                    "tipo": mensagem.type,
                    "contato": mensagem.user.name
                })
            else:
                mensagens.append({
                    "data_hora": data_hora,
                    "conteudo": mensagem.content,
                    "tipo": mensagem.type,
                    "contato": mensagem.user.name
                })

        def sort_by_key(list): return list['data_hora']
        mensagens = sorted(mensagens, key=sort_by_key)

        self.__imprime_mensagens(mensagens)

        return contato


    def __imprime_mensagens(self, mensagens):
        for mensagem in mensagens:
            print("{}: {}".format(mensagem["contato"], mensagem["conteudo"].strip()))
        print("")


    def enviar(self, envia, contato = None):

        if (contato is None):
            print("\n" * 50)
            print("Escolha um contato:\n")
            self.lista_contatos()
            contato = self.__verifica_contato_escolhido()

        if (envia == 'mensagem'):
            self.__send_message(contato)
        else:
            warnings.warn("Do nothing!")


    def __send_message(self, contato):
        print("(Enter) - Cancela mensagem")
        print("(#alt) - Altera o contato")
        print("(#list) - Lista as mensagens da conversa\n")

        nao_deseja = False
        while (not nao_deseja):
            msg = input("Digite sua mensagem: ")

            if (msg == ''):
                nao_deseja = True
            elif (msg == '#list'):
                self.ler_mensagens(contato)
            elif (msg == '#alt'):
                self.ler_mensagens()
            elif (msg.strip().upper() or msg.strip().upper() is None):
                contato.chat.sendMsg(msg)
            else:
                nao_deseja = True
                warnings.warn("Erro ao enviar a mensagem!\n\n")

        return False


    def lista_contatos(self):
        index = 0
        for contato in self.contatos:
            print("({}) - {}".format(index + 1, contato['nome']))
            index += 1


    def __mostra_contato_escolhido(self, contato_escolhido):

        nome_contato = self.__get_contact_name(contato_escolhido)
        nome_contato = "* {} ".format(nome_contato)
        caracteres_contato = ''.join("#" for letra in nome_contato)

        print(caracteres_contato)
        print(nome_contato)
        print(caracteres_contato)


    def __verifica_contato_escolhido(self):
        escolheu = False
        while (not escolheu):
            escolhido = input("\nContato (número): ")

            if (escolhido.isnumeric()):
                tamanho_lista = len(self.contatos) - 1
                escolhido = int(escolhido) - 1

                if (escolhido > tamanho_lista or escolhido < 0):
                    warnings.warn("Contato inexistente")
                else:
                    print("\n" * 50)
                    contato_escolhido = self.__conta.contacts[self.contatos[escolhido]['id']]
                    self.__mostra_contato_escolhido(contato_escolhido)
                    escolheu = True
                    return contato_escolhido
            else:
                warnings.warn("Contato inválido, tente novamente.")