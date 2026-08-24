import time
lista = []
def lista_num():
    print("Lista atual:")
    for i in range (len(lista)) :
        print(f"{i+1}-{lista[i]}")

def adicionar():
    while True:
        item = input("Digite o item para adicionar a lista: ")
        if item in lista:
            print("Este item ja foi adicionado na lista!")
            time.sleep(2.5)
        else:
            lista.append(item)
            print("Item adicionado com sucesso!")
            time.sleep(2.5)
            break

def remover():
    while True:
        lista_num()
        try:
            remov = int(input("Digite o número do item que deseja remover: "))
        except ValueError:
            print("Isso não é um número, tente novamente!")
            time.sleep(2.5)
            continue
        if remov < 1 or remov > len(lista):
            print("Número inválido, tente novamente!")
            time.sleep(2.5)
            continue

        lista.pop(remov - 1)
        print(f"O item foi removido com sucesso!")
        time.sleep(2.5)
        break

def limpar():
    while True:
        print("Tem certeza que deseja limpar a lista?")
        print("1- Sim")
        print("2- Não")
        try:
            op = int(input("Opção: "))
        except ValueError:
            print("Isso não é um número, tente novamente!")
            time.sleep(2.5)
            continue
            
        if op == 1:
            lista.clear()
            print("Lista limpa com sucesso!")
            time.sleep(2.5)
            break
        elif op == 2:
            print("Limpeza cancelada!")
            time.sleep(2.5)
            break
        else:
            print("Opção inválida!")
            time.sleep(2)
            continue

    

while True:
    print("----------------------------")
    print("Bem-vindo a lista de compras")
    print("----------------------------")
    print("")
    print("1- Acessar lista de compras")
    print("2- Adicionar item a lista de compras")
    print("3- Remover item da lista de compras")
    print("4- Limpar lista de compras")
    print("5- Sair")
    print("")
    try:
        num = int(input("Opção: "))
    except ValueError:
        print("Isso não é um número, tente novamente!")
        time.sleep(2.5)
        continue

    if num == 1:
        if not lista:
            print("A lista esta vazia!")
            time.sleep(2.5)
            continue
        else:
            lista_num()
            time.sleep(2.5)

    elif num == 2:
        adicionar()

    elif num == 3:
        if not lista:
            print("A lista esta vazia!")
            time.sleep(2.5)
            continue
        remover()

    elif num == 4:
        if not lista:
            print("A lista esta vazia!")
            time.sleep(2.5)
            continue
        limpar()

    elif num == 5:
        break

    else:
        print("Opção inválida!")
        time.sleep(2.5)
        continue

print("Finalizando lista de compras!")

