from conta import Conta
from cliente import Cliente

def play():
    conta1 = Conta(1, "Fulano", 1.0, 2)
    print(conta1.extrato())

    conta2 = Conta(2, "Beltrano", 4.0, 2)
    print(conta2.extrato())

    conta3 = Conta(3, "Sicrano", 10.0, 2000.0)
    print(conta3.extrato())

    print("\nTransferindo valores do(a) {} para o/a {}".format(conta2.get_titular(), conta1.get_titular()))
    conta2.transfere(3.0, conta1)
    print(conta2.extrato())
    print(conta1.extrato())

    ##########################

    print("\n")

    cliente1 = Cliente('Nico')
    print(cliente1.nome)
    cliente1.nome = 'Nicobocco'
    print(cliente1.nome)

    ##########################

if (__name__ == "__main__"):
    play()