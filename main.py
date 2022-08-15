numeros = [0,0,0,0,0,0,0,0,0,0]

pediu_para_sair = False
while not pediu_para_sair:

    print('\n(1) Alterar um valor da lista')
    print('(2) Mostrar a lista')
    print('(0) Sair')
    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        indice = int(input('\n# Índice da posição: '))
        valor = int(input('\n# Novo valor: '))
        numeros[indice] = valor
        print('\n# Valor alterado com sucesso!')

    elif opcao == '2':
        print(f'\n# Conteúdo da lista: {numeros}')

    elif opcao == '0':
        pediu_para_sair = True

    else:
        print('\n# Opção inválida!')

print('\n# Fim do programa!')