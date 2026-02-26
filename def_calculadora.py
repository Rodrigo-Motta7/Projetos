def operacao():
    verdade = True

    while verdade:
        print("----------------------------------------")
        print("Bem-vindo a calculadora")
        print("----------------------------------------")
        a = int(input("Digite o primeiro número inteiro da operação: "))
        b = int(input("Digite o segundo número inteiro da operação: "))
        print("----------------------------------------")
        print(f"Os números digitados são {a} e {b}.")
        print("")
        while verdade:
            cont = input('Deseja fazer alguma alteração? "s" para sim e "n" para não: ')
            if cont not in ("s", "n"):
                print("Erro: Alternativa invalida!")
                continue

            if cont == "s":
                break

            if cont =="n":
                while verdade:
                    print("----------------------------------------")
                    print(f"Escolha qual operação será feita entre {a} e {b}.")
                    nome_funcao = input("Digite quais dessas operações será utilizada. (soma, subtração, multiplicação ou divisão): ")
                    print("----------------------------------------")
                    
                    operacoes = {
                        "soma": soma,
                        "subtração": subtração,
                        "multiplicação": multiplicação,
                        "divisão": divisão
                    }
                    if nome_funcao == "divisão" and b == 0:
                        print("Não é possível fazer divisão por zero!")
                        print("----------------------------------------")
                        break

                    if nome_funcao not in operacoes:
                        print("Erro: Digite uma operação válida!")
                        continue
                    funcao = operacoes[nome_funcao]
                    verdade = False
    resultado = funcao(a,b)
    
    print(f"O resultado da {nome_funcao} entre {a} e {b} é = {resultado}.")
    print("----------------------------------------")
    print("Fechando calculadora.")  
    print("")          

def soma(a,b):
    return a + b

def subtração(a,b):
    return a - b

def multiplicação(a,b):
    return a * b

def divisão(a,b):
    return a / b

operacao()