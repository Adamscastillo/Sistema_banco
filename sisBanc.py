saldo = 0
limite_saque = 500
numero_saques = 0 
quantidade_saques = 3

depositos = ""
saques = ""

menu = """
====== MENU ======

[1] - DEPOSITAR
[2] - SACAR
[3] - EXTRATO
[4] - AUMENTAR LIMITE DE SAQUE
[0] - SAIR

==================

=> """

while True:
    opcao = input(menu)
    # DEPOSITOS
    if opcao == "1":
       
        valor= float(input("informar o valor de deposito: R$ "))
       
        if valor > 0:
            saldo += valor
            depositos += f"Depósito: R${valor: .2f}\n"
            print(f"\ndepósito de R${valor: .2f} realizado com sucesso !")
        else:
            print("valor inválido, deposite apenas valor positivos.")
    # SAQUES
    elif opcao == "2":

        valor= float(input("informar o valor de saque: R$ "))

        if valor > saldo:
            print("O peração não concluida, saldo insuficiente !")

        elif valor > limite_saque:
            print(f"Operação falhou! seu limite de saque é R${limite_saque:.2f}.")
        
        elif numero_saques >= quantidade_saques:
            print(f"Operação falhou! limites de saque diários foi atingido")
        
        elif valor > 0:
            saldo -= valor
            saques += f"saque: R${ - valor: .2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor: .2f} realizado com sucesso!")
        else:
            print("Valor inválido, informe um valor positivo.")
    # EXTRATO
    elif opcao =="3":
        print("=" *20)
        print("Extrato".center(20))
        print("=" *20)
        print("DEPÓSITO:")
        print(depositos if depositos else "Nenhum depósito realizado.")
        print("SAQUES:")
        print(saques if saques else "Nenhum saque realizado.")
        print(f"\nSaldo atual: R${saldo: .2f}")
        print("=" *20)
    # AUMENTAR O LIMITE 
    elif opcao == "4":
        novo_limite = float(input(f"Seu limite atual é R${limite_saque:.2f}. Informe o novo limite: R$ "))
        
        if novo_limite > 0 and novo_limite > limite_saque:
            limite_saque = novo_limite
            print(f"\nLimite de saque atualizado para R${limite_saque:.2f} com sucesso!")
        elif novo_limite <= limite_saque:
            print(f"\nO novo limite deve ser maior que o limite atual de R${limite_saque:.2f}.")
        else:
            print("Valor inválido. Informe um valor positivo.")
    # OPÇÃO DE SAIR 
    elif opcao =="0":
        print("Obrigado por utilizar nosso banco. Até mais!")
        break
    else:
        print("opção inválidade tente novamente.")
    
    



            

