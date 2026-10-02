import subprocess
import requests


url = "https://economia.awesomeapi.com.br/json/"
op = None
while op != "2":
    print("-" * 15)
    print("App de Câmbio")
    print("-" * 15)
    print("1 - Câmbio")
    print("2 - Sair")
    op = input("Seleciona a opção: ")
    if op == "1":
        origem = input("\n Insere o código da moeda de origem: ")
        destino = input("\n Insere o código da moeda de destino: ")
        url += f"{origem}-{destino}"
        try:
            request = requests.get(url)
            statuscode = request.status_code
            if statuscode == 200:
                json = request.json()[0]
                for index, i in json.items():
                    print(f"{index}: {i}")
            elif statuscode == 400:
                print("Erro! Endereço mal-formatado!")
            elif statuscode == 403:
                print("Proibido, não deverias estar a ver isto lol")
            elif statuscode == 404:
                print("Não existe! Escreveste bem os códigos das moedas?")
            elif statuscode == 500:
                print("Erro do servidor, tenta depois.")
            subprocess.run("pause", shell=True)
        except requests.exceptions.ConnectionError:
            print("Não deu para conectar. Tens internet?")
            subprocess.run("pause", shell=True)
    elif op == "2":
        print("Tchau")
    else:
        print("Opção inválida\n")
        subprocess.run("pause", shell=True)
quit()