class Usuario:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    def __init__(self, agencia, nro_conta, usuario_cpf):
        self.agencia = agencia
        self.nro_conta = nro_conta
        self.usuario_cpf = usuario_cpf

def menu(): 
    menu = """
    [uc] Criar usuário
    [bac] Criar uma conta-corrente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [conf] Configurações
    => """
    return input(menu)

def adminMenu():
    adminMenu = """
    [lu] Listar Usuários Cadastrados
    [lc] Listar Contas Cadastradas
    [return] Retornar ao menu anterior
    => """
    return input(adminMenu)


def deposito(saldo, valor_deposito, extrato, lista_depositos):
    if valor_deposito > 0:
        saldo += valor_deposito

        lista_depositos.append(valor_deposito)

        print("======= Valor depositado com sucesso! =======")
        #print(saldo) # Linha de depuração

    else:
        print("======= Depósito inválido. Apenas valores maiores que zero podem ser depositados. =======")

    return saldo, extrato, lista_depositos

def saque(*, saldo, extrato, valor_saque, limite_valor_saque, numero_saques, LIMITE_SAQUES, lista_saques):

    if valor_saque <= limite_valor_saque and valor_saque <= saldo and numero_saques < LIMITE_SAQUES:
                
        numero_saques += 1

        lista_saques.append(valor_saque)

        saldo -= valor_saque

        print("======= Valor sacado com sucesso! =======")
       #print(saldo) # Linha de depuração

    elif valor_saque > saldo:
        print("======= Saldo insuficiente. O valor a ser sacado deverá ser menor ou igual o seu saldo. =======")
        #print(saldo) # Linha de depuração

    elif valor_saque > limite_valor_saque:
        print("======= Falha. Valor maior que o limite diário permitido. =======")
        #print(saldo) # Linha de depuração

    elif numero_saques >= LIMITE_SAQUES:
        print("======= Falha. Você excedeu o limite de saques diários. =======")
        #print(saldo) # Linha de depuração

    return saldo, extrato, lista_saques, numero_saques

def bank_statement(saldo, /, *, extrato, lista_depositos, lista_saques):
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

def create_user_account(*, lista_usuarios, nome, cpf, endereco):
    
    for usuario in lista_usuarios:
        if usuario.cpf == cpf:
            print("======= Usuário já cadastrado. Tente novamente. =======")
            return lista_usuarios

    usuario = Usuario(nome=nome, cpf=cpf, endereco=endereco)
    lista_usuarios.append(usuario)
    print("======= Usuário criado com sucesso! =======")

    return lista_usuarios

def create_savings_account(*, lista_contas, cpf_usuario, numero_conta, NRO_AGENCIA):
    
    for temp_nro_conta in lista_contas:
        if temp_nro_conta == numero_conta:
            print("======= Conta já cadastrada. Tente novamente. =======")
            return lista_contas

    numero_conta += 1   
    conta = Conta(agencia=NRO_AGENCIA, nro_conta=numero_conta, usuario_cpf=cpf_usuario)
    lista_contas.append(conta)
    print("======= Conta-corrente criada com sucesso! =======")

    return lista_contas, numero_conta

def main():
    lista_usuarios =[]
    lista_contas = []
    lista_depositos = []
    lista_saques = []
    saldo = 0
    limite_valor_saque = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 0
    LIMITE_SAQUES = 3
    NRO_AGENCIA = "0001"

    while True:
        opcao = menu()

        #print(f"Opção digitada: '{opcao}'")  # Linha de depuração

        if opcao == "d":
            valor_deposito = float(input("Digite o valor a ser depositado: "))

            ''' Aqui a funcao deposito se torna um objeto de primeira classe e atribui os valores de retorno as variaveis saldo, extrato e lista_depositos.
                Os parametros da funcao deposito estao sendo passados por posicao. Portanto, se a ordem for alterada, 
                a atribuicao das variaveis sera invertida e/ou mal interpretada'''
            saldo, extrato, lista_depositos = deposito(saldo, valor_deposito, extrato, lista_depositos)

        elif opcao == "s":
            #print(saldo) # Linha de depuração

            valor_saque = float(input("Digite o valor a ser sacado: "))

            ''' Aqui a funcao saque se torna um objeto de primeira classe e atribui os valores de retorno as variaveis saldo, extrato e lista_saques.
                Os parametros da funcao saque estao sendo passados por nome. Portanto, se a ordem for alterada, 
                nao havera prejuizo nos valores atribuidos as variaveis, pois sao cojunto de chave:valor'''
            saldo, extrato, lista_saques, numero_saques = saque(
                extrato=extrato,
                saldo=saldo,
                valor_saque=valor_saque,
                limite_valor_saque=limite_valor_saque,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
                lista_saques = lista_saques
            )

        elif opcao == "e":
            bank_statement(saldo, extrato=extrato, lista_depositos=lista_depositos, lista_saques=lista_saques)

        elif opcao == "uc":
            print("======= Para começarmos, por favor, insira os dados abaixo =======")

            nome = str(input("Nome completo: ")).upper()


            while True:
                try: 
                    cpf = int(input("Insira o seu CPF - Somente números: ")) 
                    break
                except ValueError:
                    print("CPF inválido, use somente números")
            
            
            print("======= O endereço deverá seguir o formato: Rua, Nro - bairro - cidade-estado(sigla) =======")
            print("======= Exemplo: Rua Dr Aires Martins Torres, 180 - Vila São Francisco - São Paulo-SP =======")
            endereco = str(input("Endereço: ")).upper()

            lista_usuarios = create_user_account(
                lista_usuarios = lista_usuarios, 
                nome=nome,
                cpf=cpf,
                endereco=endereco
            )

        elif opcao == "bac":
            ''''
            --> Itere a lista de usuários pelo CPF:
                * Se houver um CPF cadastrado: chamar a função Criar Conta e passar esse CPF como parâmetro;
                * Senão: Parar, orientar a criação de um usuário e voltar ao menu inicial.
            '''
            print("======= Para começarmos, por favor, insira os dados abaixo =======")

            while True:
                try: 
                    cpf_usuario = int(input("Insira o seu CPF - Somente números: ")) 
                    break
                except ValueError:
                    print("CPF inválido, use somente números")

            for usuario in lista_usuarios:
                if usuario.cpf == cpf_usuario:
                    lista_contas, numero_conta = create_savings_account(
                    lista_contas = lista_contas, 
                    cpf_usuario = cpf_usuario,
                    numero_conta = numero_conta,
                    NRO_AGENCIA = NRO_AGENCIA
                    )

                else:
                    print("======= Você ainda não possui um usuário cadastrado. Faça um novo cadastro para criar a sua conta. =======")

        elif opcao == "conf":
            while True:
                admin = adminMenu()
                if admin == "lu":
                    if len(lista_usuarios) > 0:
                            for usuario in lista_usuarios:
                                print(f"Nome: {usuario.nome}, CPF: {usuario.cpf}, Endereço: {usuario.endereco}")
                    else:
                        print("Ainda não há usuários cadastrados.")

                elif admin == "lc":
                    if len(lista_contas) > 0:
                        for conta in lista_contas:
                            print(f"CPF: {conta.usuario_cpf}, Número da Conta: {conta.nro_conta}, Agência: {conta.agencia}")
                    else:
                        print("Ainda não há contas cadastradas.")

                elif admin == "return":
                    break
        
        elif opcao == "q":
            break
        else:
            print("======= Operação inválida, por favor selecione novamente a opção desejada =======")
main()