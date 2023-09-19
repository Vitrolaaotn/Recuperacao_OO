from classes import *
import os

def main():
    
    sair = False
    while sair == False:
        
        try:
            os.system("cls")
            print("---MENU---")
            print("01 - CADASTRAR CLIENTE")
            print("02 - Sacar")
            print("03 - Depositar")
            print("04 - Transferir")
            print("05 - Exibir Saldo")
            print("00 - SAIR")
            print("--------")
            print("")

            print("Qual opção deseja?")
            menu = int(input(">> "))

            os.system("pause")

            match menu:
                case 1:
                    nome = input("Digite o nome do cliente: ")
                    sobrenome = input("Digite o sobrenome do cliente: ")
                    saldo = input("Digite o saldo inicial da conta: ")
                    Banco.criar_conta(nome, sobrenome, saldo)
                    

                case 2:
                    os.system("cls")
                    Banco.sacar()
                    os.system("pause")

                case 3:
                    os.system("cls")
                    Banco.depositar()
                    os.system("pause")

                case 4:
                    os.system("cls")
                    Banco.transferir()
                    os.system("pause")

                case 5:
                    os.system("cls")
                    Banco.getSaldo()
                    os.system('pause')
                
                case 0:
                    print("SAINDO ...")
                    print("------")
                    sair = True
                
                case _:
                    print("Valor invalido")
                    print("------")

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            print("")