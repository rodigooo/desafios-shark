# --- Imports ---

from os import remove as rem_file
from os import makedirs as makefolder
from time import sleep as zzz
from subprocess import run as shell
import json

# --- Declarar as variáveis ---

lista = []
save_path = "lista_compras_save\\lista.txt"
save_list_success = "Lista Guardada"
empty_list_error = "Lista vazia"
rem_list_success = "Lista removida"
rem_list_error = "Ainda não há uma lista guardada"
add_to_list_success = "Item adicionado à lista"
add_to_list_error = "Erro: Item já está na lista"
rem_from_list_success = "Item removido da lista"
rem_from_list_error = "Erro: Esse item não está na lista"
success_save = None
makefolder("lista_compras_save", exist_ok=True)

# --- Funções ---

def carregar():
    global lista
    try:
        with open(save_path, 'r') as file: # Tenta abrir o ficheiro
            lista = json.load(file) # Carrega a lista
    except FileNotFoundError: # Se não existir o ficheiro
        pass # Lista fica vazia (ver em cima)


def guardar(list_to_save):
    global success_save
    if list_to_save: # Vê se a lista não está vazia
        with open(save_path, 'w') as file: # Abre o ficheiro
            json.dump(list_to_save, file)
        print(save_list_success)
        success_save = True # Guarda se conseguiu salvar ou não

    else: # Se estiver vazia
        print(empty_list_error)
        success_save = False


def apagar(path):
    global lista
    try: # Tenta o seguinte
        rem_file(path) # Remover o ficheiro
        lista = []
        print(rem_list_success)

    except FileNotFoundError: # Se não existir
        print(rem_list_error)


def adicionar(item, list_to_add):
    if item not in list_to_add: # Vê se o item não está já na lista
        list_to_add.append(item) # Adiciona o item
        print(add_to_list_success)

    else: # Se estiver
        print(add_to_list_error)

    return list_to_add # Retorna a lista com o item adicionado, ou inalterada


def remover(item, list_to_remove):
    if item in list_to_remove: # Vê se o item está na lista
        list_to_remove.remove(item) # Remove o item
        print(rem_from_list_success)

    else: # Se não estiver
        print(rem_from_list_error)

    return list_to_remove # Retorna a lista com o item removido, ou inalterada


def ver(list_to_see):
    count = 0 # Contador
    if list_to_see: # Se a lista tiver algo
        for i in list_to_see: # Faz quantas vezes há itens na lista
            print(i, end=", ") # Printa os itens
            count += 1 # Incrementa o contador
            if count % 5 == 0: # A cada 5 itens printados...
                print() # Muda de linha
        print() # Muda de linha
    else: # Se a lista estiver vazia
        print(empty_list_error)



# --- Loop Principal ---
def main():
    global lista
    print("\n=== Lista de compras ===")
    print("Opções:")
    print("  1 - Adicionar à lista")
    print("  2 - Remover da lista")
    print("  3 - Ver a lista")
    print("  4 - Guardar a lista")
    print("  5 - Guardar e sair")
    print("  6 - Sair sem guardar")
    print("  7 - Apagar a lista")
    op = input("Selecione a opção: ")

    if op == "1":
        item_to_add = input("Que item deseja adicionar? ")
        lista = adicionar(item_to_add.lower(), lista)

    elif op == "2":
        item_to_remove = input("Que item deseja remover? ")
        lista = remover(item_to_remove.lower(), lista)

    elif op == "3":
        ver(lista)

    elif op == "4":
        guardar(lista)

    elif op == "5":
        guardar(lista)
        if success_save:
            quit()

    elif op == "6":
        quit()

    elif op == "7":
        apagar(save_path)
    zzz(0.5)
    shell("pause",shell = True)

if __name__ == "__main__":
    carregar()
    while True:
        main()