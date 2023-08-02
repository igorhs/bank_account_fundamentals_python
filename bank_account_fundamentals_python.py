menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

lista_depositos = []
lista_saques = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)  # Remova espaços em branco do início e do final da entrada

    print(f"Opção digitada: '{opcao}'")  # Linha de depuração

    if opcao == "d":
        deposito = float(input("Digite o valor a ser depositado: "))

        if deposito > 0:
            saldo += deposito

            lista_depositos.append(deposito)

            print("Valor depositado com sucesso!")

        else:
            print("Depósito inválido. Apenas valores maiores que zero podem ser depositados.")

    elif opcao == "s":
        saque = float(input("Digite o valor a ser sacado: "))

        if saque <= limite and saque <= saldo and numero_saques < LIMITE_SAQUES:
                
            numero_saques += 1

            lista_saques.append(saque)

            saldo -= saque

            print("Valor sacado com sucesso!")

        elif saque > saldo:
            print("Saldo insuficiente. O valor a ser sacado deverá ser menor ou igual o seu saldo.")

        elif saque > limite:
            print("Falha. Valor maior que o limite diário permitido.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Falha. Você excedeu o limite de saques diários.")

    elif opcao == "e":
        print( 
                '''
    ======= EXTRATO BANCÁRIO =======

    DEPÓSITOS
    ---------------------------------
    ''')
        for deposito in lista_depositos:
            print(f"    +R$: {deposito:.2f}")


        print( 
                '''
    SAQUES
    ---------------------------------
    ''')
        for saque in lista_saques:
            print(f"    -R$: {saque:.2f}")

        print(
        f'''
    ---------------------------------
    SALDO ATUAL:         R${saldo:.2f}
    ---------------------------------
        ''')

    elif opcao == "q":
        break

    else:
      print("Operação inválida, por favor selecione novamente a opção desejada")