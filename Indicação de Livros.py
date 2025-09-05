import requests
import os

def livros():
    os.system('cls')

    genero_escolhido = input("Digite o gênero que você quer (fantasy, mistery, terror, drama): ") 
    quantidade_livros = int(input("Digite a quantidade de livros que você deseja: "))
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genero_escolhido}"
    resposta = requests.get(url) # vai armazenar os livros encontrados
    dados = resposta.json() 
    livros = dados["items"]

    if not livros:
        print("Não há livros para esse gênero!")
        voltar = input("Aperte a tecla ENTER para voltar")

    else:
        for elemento in livros[:quantidade_livros]:
            info = elemento.get("volumeInfo", {})  
            print(info.get("title", "Sem título"))
            print(info.get("authors", ["Autor desconhecido"]))
            print(info.get("description", "Sem descrição"))

livros()
