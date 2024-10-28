# Atividade sobre saque bancário do curso de Engenharia de Dados da DIO 


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[o] Sair


"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        quantia_depositada = float(input('Insira o valor de depósito: '))
                                   
        if quantia_depositada < 0:
            print('Operação não disponível')

        else:
            saldo += quantia_depositada
            extrato += f'Depósito de R$ {quantia_depositada:.2f}\n'
    
    elif opcao == "s":
        quantia_sacada = float(input('Insira o valor de saque: '))

        excedeu_saldo = quantia_sacada > saldo 
        excedeu_limite = quantia_sacada > limite
        excedeu_n_saques = numero_saques >= limite_saques


        if excedeu_saldo:
            print('Sua tentativa de saque é maior que o saldo disponível')

        elif excedeu_limite:
            print('A quantia a ser sacada é maio do que o limite permitido')

        elif excedeu_n_saques: 
            print('Você já atingiu o limite de saques diários')

        elif quantia_sacada > 0:
            saldo -= quantia_sacada
            print(f'Você sacou {quantia_sacada} ')
            extrato += f"Saque de R$ {quantia_sacada:.2f}\n"
            numero_saques += 1
            print(f'Seu número de saques é: {numero_saques}')

        else:
            print('Operação falhou pois o valor informado é inválido')


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print('Não foi realizado movimentações')
        else:
            print(extrato)
        
        print(f'\nSaldo de R$ {saldo:.2f}')
        print('-----------------------------')
    

    elif opcao == "o":
        break 
    
    else:
        print('Opção não disponível')

# Finalizado