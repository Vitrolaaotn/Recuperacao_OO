class Cliente():
    def __init__(self, nome, sobrenome, saldo, conta):
        self.nome=nome
        self.sobrenome= sobrenome
        self.saldo = saldo
        self.conta= conta
    
class Banco(Cliente):
    def __init__(self):
        self.clientes = []
        
    def criar_conta(self, nome, sobrenome, saldo, conta ):
            cliente = Cliente(nome, sobrenome,saldo)
            self.clientes.append(cliente)
            self.conta =+ 1
            print (f"O cliente foi cadastrado com sucesso, com o saldo {saldo}, guarde o número da sua conta que é {conta}")

    def sacar(self):
        valorsacado = input("Digite o valor que deseja sacar:")
        if valorsacado>self.saldo:
            print ('O valor que deseja sacar não existe na conta')
        elif valorsacado<=self.saldo:
            valorsacado=-self.saldo
            print (f'Seu novo saldo é {self.saldo}')
    
    def depositar(self,saldo):
        self.saldo = saldo
        valordepositado = input("Digite o valor que deseja depositar:")
        self.saldo +=valordepositado    
        return self.saldo
    
    def transferir(self, destino, conta,):
        self.destino = destino
        

        destino= input(int("Digite o número da conta que deseja transferir"))

        if destino==conta:
            self.valor = input(int("Digite valor que deseja transferir"))
        
            if self.saldo<self.valor:
                print ('Você não possui o valor que deseja transferir')
            elif self.saldo>=self.valor:
                self.saldo=- self.valor
            
        else: 
            print('O número da conta não existe')
        
    def getSaldo(self):
        return self.saldo



