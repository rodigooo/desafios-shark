def main():
    import subprocess
    import time
    import random
    palavras = ["SHARK", "PYTHON",
                "ESCOLA", "SHARKCODERS",
                "PROGRAMACAO", "COMPUTADOR",
                "CRIATIVIDADE", "ALGORITMO",
                "APRENDIZAGEM", "LINGUAGEM",
                "CODIGO", "FUNCAO",
                "TECNOLOGIA", "INTERATIVIDADE",
                "DESAFIO", "ESTUDANTE",
                "LOGICA", "DESENVOLVIMENTO",
                "PLATAFORMA", "PROJETO"]
    palavraEscolhida = random.choice(palavras)
    letrasAdivinhadas = ""
    erros = 0
    while True:
        letraCorreta = 0
        for l in palavraEscolhida:
            if l in letrasAdivinhadas:
                print(l, end='')
                letraCorreta += 1
            else:
                print("_", end='')
        print()
        if letraCorreta == len(palavraEscolhida):
            print("Ganhaste!")
            subprocess.run("start https://www.youtube.com/watch?v=s0E5Slqdo1M", shell=True)
            quit()
        print(f"Letras já usadas: {letrasAdivinhadas}")
        print()
        guess = input("Adivinha uma letra: ").upper()
        if not (guess in letrasAdivinhadas):
            letrasAdivinhadas += guess
        else:
            print("Letra já utilizada, tenta de novo")
            print()
            time.sleep(0.5)
            continue
        if guess in palavraEscolhida:
            print("Está na palavra!\n")
        else:
            print("Não está na palavra!")
            erros += 1
            print(f"Erros: {erros} de 6\n")
        if erros >= 6:
            print("Perdeste!")
            quit()
        time.sleep(0.5)


if __name__ == "__main__":
    main()