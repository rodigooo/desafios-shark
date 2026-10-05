# --- Importar bibliotecas ---
import random

# --- Definir variáveis ---
somas = {}

for i in range(2, 13):
    somas[f"soma{i}"] = 0

# --- Jogar os dados ---
for i in range(10000):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma_dados = dado1 + dado2

    # --- Conta as somas ---
    somas[f"soma{soma_dados}"] += 1

# --- Mostrar os resultados ---
print("Quantas vezes saiu cada soma:")
for i in range(2, 13):
    print(f"{i} -> {somas[f"soma{i}"]}")