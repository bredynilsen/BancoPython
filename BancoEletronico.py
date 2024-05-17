import textwrap
def menu():
    menu = """==========================================
| DIGITE A OPÇAO DESEJADA:
| [u] Criar Usuário
| [c] Abrir Conta Corrente
| [l] Listar
| [d] Depositar
| [s] Sacar
| [e] Extrato
| [q] Sair
==========================================
=> """
    return input(textwrap.dedent(menu))
           



def deposito(saldo, valor, extrato, /):
   
    if valor > 0:
        saldo += valor
        extrato += f"▲ Depósito: R$ {valor:.2f}\n"
        print("==========================================") 
        print(f"Deposito no valor de {valor:.2f} realizado com SUCESSO.") 
    else:
            print("╳ Operação falhou! O valor informado é inválido. ╳ ")
    return saldo, extrato
           
def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
                
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("╳ Operação falhou! Você não tem saldo suficiente. ╳ ")

    elif excedeu_limite:
        print("╳ Operação falhou! O valor do saque excede o limite. ╳ ")

    elif excedeu_saques:
        print("╳ Operação falhou! Número máximo de saques excedido. ╳ ")

    elif valor > 0:
        saldo -= valor
        extrato += f"▼ Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("==========================================") 
        print(f"Saque no valor de {valor:.2f} realizado com SUCESSO.")
    else:
        print("╳ Operação falhou! O valor informado é inválido. ╳ ")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO =================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("__________________________________________")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    while True:

        opcao = menu() 

        if opcao == "d":
            valor=float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("╳ Operação inválida, por favor selecione novamente a operação desejada. ╳ ")
        
if __name__ == "__main__":
    main()
'''
Novas funcões:
listar contas
listar usuários
Listar numero de contas


criar usuário:
armazenar usuarios em lista>> 
armazennar CHAVE-
usuario: nome, nascimento, cpf, endereço
endereço : string: logradouro, nro, bairro, cidade/sigla estado.
armazenar somente cpf
não pode existir 2 usuarios com mesmo cpf

armazenar contas em lista>>
conta: agencia, nro da conta e usuario
nro conta: seqeuncuai comecado em 1
agencia = 0001
pode haver varias contas por usuario

para vincular usuario a conta, filtre a lista de usuarios buscando o nuero do CPF informado para cada usuario da lista
'''

