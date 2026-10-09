numeros = []

def pedir_numero(lista, prompt): # Função para não repetir o código
    lista.append(float(input(prompt)))

for _ in range(5):
    pedir_numero(numeros, "Escolha um número para adicionar: ")

def bubbsort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1): # Evita os espaços já organizados
            if arr[j] > arr[j + 1]: # Se não estiver organizado
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Troca posição
    return arr

organizado = bubbsort(numeros)

print(organizado)