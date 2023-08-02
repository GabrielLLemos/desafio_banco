
menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """


saldo = 1000
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        print("Depósito")

        deposito = float(input("Valor do depósito: "))
        
        if deposito < 0:
            print("Valor inválido!")
        else:
            saldo += deposito
            print(f"Deposito efetuado, novo Saldo: R${saldo:.2f}")
            extrato.append(f"Deposito +R${deposito:.2f}")


    elif opcao == "S":
        print("Sacar")

        saque = float(input("Valor do saque: "))

        if saque > saldo:
            print("Saldo insuficiente.")
        elif numero_saques > 2:
            print("Limite de saques atingido. Não é mais possível sacar.")
            print(saldo)
        else:
            saldo -= saque
            print(f"Saque realizado com sucesso. Seu novo saldo é: R${saldo:.2f}")
            extrato.append(f"Saque -R${saque:.2f}")
            numero_saques += 1


    elif opcao == "E":
        print("Extrato: ")
        for i in range(0,len(extrato),1):
            print(extrato[i])
        print(f"R${saldo:.2f}")
        


    elif opcao == "Q":
        break


