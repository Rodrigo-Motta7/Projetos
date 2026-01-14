verdade = True

print('----------------------------')
print('Seja Bem-vindo a calculadora')
print('----------------------------')

while verdade:
    n1 = int(input('Digite o primero valor inteiro da operação: '))
    n2 = int(input('Digite o segundo valor inteiro da operação: '))
    print('')
    con = input(f'Os valores digitados são {n1} e {n2}, dejesa alterar eles? Digite "s" para sim e "n" para não: ')
    if con == 's':
        continue
    if con == 'n':
        while verdade:
            print('')
            op = input('Digite a operação que você deseja fazer ("adição", "subtração", "multiplicação" ou "divisão"): ')
            if op not in ["adição", "subtração", "multiplicação", "divisão"]:
                continue

            if op == 'adição':
                resultado = n1 + n2
                verdade = False

            if op == 'subtração':
                resultado = n1 - n2
                verdade = False 

            if op == 'multiplicação':
                resultado = n1 * n2
                verdade = False 

            if op == 'divisão':
                resultado = n1 / n2
                verdade = False

            print(f'O resultado da {op} entre os números {n1} e {n2} é igual a {resultado :.2} .')
        break
    if con != 's' and 'n':
        print('Erro, opção invalida.')
        continue
print('----------------------------')
print('Fechando calculadora')
print('----------------------------')


