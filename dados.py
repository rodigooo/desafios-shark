# --- Importar bibliotecas ---
import random

# --- Definir variáveis ---
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0
soma7 = 0
soma8 = 0
soma9 = 0
soma10 = 0
soma11 = 0
soma12 = 0

# --- Jogar os dados ---
for i in range(10000):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma_dados = dado1 + dado2

    # --- Conta as somas ---
    if soma_dados == 2:
        soma2 += 1
    elif soma_dados == 3:
        soma3 += 1
    elif soma_dados == 4:
        soma4 += 1
    elif soma_dados == 5:
        soma5 += 1
    elif soma_dados == 6:
        soma6 += 1
    elif soma_dados == 7:
        soma7 += 1
    elif soma_dados == 8:
        soma8 += 1
    elif soma_dados == 9:
        soma9 += 1
    elif soma_dados == 10:
        soma10 += 1
    elif soma_dados == 11:
        soma11 += 1
    elif soma_dados == 12:
        soma12 += 1

# --- Mostrar os resultados ---
print("Quantas vezes saiu cada soma:")
print(f"2 -> {soma2}")
print(f"3 -> {soma3}")
print(f"4 -> {soma4}")
print(f"5 -> {soma5}")
print(f"6 -> {soma6}")
print(f"7 -> {soma7}")
print(f"8 -> {soma8}")
print(f"9 -> {soma9}")
print(f"10 -> {soma10}")
print(f"11 -> {soma11}")
print(f"12 -> {soma12}")