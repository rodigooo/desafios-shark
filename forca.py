def main():
    # -----------------------
    #        Imports
    # -----------------------
    import subprocess
    import time
    import random
    # -----------------------
    #       Variáveis
    # -----------------------
    palavras = ["SHARK", "PYTHON",
                "ESCOLA", "SHARKCODERS",
                "PROGRAMACAO", "COMPUTADOR",
                "CRIATIVIDADE", "ALGORITMO",
                "APRENDIZAGEM", "LINGUAGEM",
                "CODIGO", "FUNCAO",
                "TECNOLOGIA", "INTERATIVIDADE",
                "DESAFIO", "ESTUDANTE",
                "LOGICA", "DESENVOLVIMENTO",
                "PLATAFORMA", "PROJETO"] # Lista de palavras a usar
    palavraEscolhida = random.choice(palavras) # Escolhe uma palavra
    letrasAdivinhadas = ""
    erros = 0
    # -----------------------
    #       Programa
    # -----------------------
    while True:
        letraCorreta = 0 # Reseta o contador
        for l in palavraEscolhida: # Para cada letra na palavra
            if l in letrasAdivinhadas: # Se a letra estiver nas letras que adivinhou
                print(l, end='') # Printa letra
                letraCorreta += 1 # Aumenta contador
            else:
                print("_", end='') # Espaço em branco
        print()
        if letraCorreta == len(palavraEscolhida): # Se os dois foram iguais significa que ganhou
            print("Ganhaste!")
            subprocess.run("start https://www.youtube.com/watch?v=s0E5Slqdo1M", shell=True) # Abre um vídeo :)
            quit() # Sai do programa
        print(f"Letras já usadas: {letrasAdivinhadas}")
        print()
        guess = input("Adivinha uma letra: ").upper()
        if not (guess in letrasAdivinhadas): # Se a letra não foi já usada
            letrasAdivinhadas += guess # Adiciona às letras já usadas
        else:
            print("Letra já utilizada, tenta de novo")
            print()
            time.sleep(0.5) # zzz
            continue
        if guess in palavraEscolhida: # Se a letra adivinhada estiver na palavra
            print("Está na palavra!\n")
        else:
            print("Não está na palavra!")
            erros += 1 # Incrementa o contador de erros
            print(f"Erros: {erros} de 6\n") # Contador para o utilizador
        if erros >= 6: # Se os erros chegarem a 6
            print("Perdeste!")
            quit()
        time.sleep(0.5) # zzz


if __name__ == "__main__": # Evita que o programa corra se fizer import
    main()