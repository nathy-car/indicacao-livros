import json
import requests

url = "https://www.googleapis.com/books/v1/volumes?q=subject:fantasy"
resposta = requests.get(url) # vai armazenar os livros encontrados
dados = resposta.json() 
livros = dados["items"]
print(dados.keys()) # vai mostrar as chaves que a API possui

primeiro_livro = dados.get("items", []) [0]
volume_info = primeiro_livro.get("volumeInfo", {})
print(volume_info.keys()) # vai mostrar as chaves presentes dos livros

