import httpx
from bs4 import BeautifulSoup
import json

# URL da página
url = "https://books.toscrape.com/"
# Fazendo a requisição HTTP
response = httpx.get(url)
# Criando um objeto BeautifulSoup para analisar o conteúdo HTML da página
soup = BeautifulSoup(response.text, "html.parser")
# Encontrando todos os elementos HTML que representam os livros na página
books = soup.find_all("article", class_="product_pod")

# Lista para armazenar as informações dos livros
books_info = []
# Iterando sobre cada elemento de livro encontrado
for book in books:
    # Extraindo o título do livro
    title = book.h3.a["title"]
    # Extraindo o preço do livro
    price = book.find("p", class_="price_color").get_text().strip()
    # Extraindo a avaliação do livro (classe CSS indica a avaliação)
    rating = book.p["class"][1]
    # Extraindo a disponibilidade do livro
    stock = book.find("p", class_="instock availability").get_text().strip()

    # Criando um dicionário com as informações do livro
    book_info = {
        "title": title,
        "price": price,
        "rating": rating,
        "availability": stock
    }
    # Adicionando o dicionário à lista de informações dos livros
    books_info.append(book_info)

    # Imprimindo as informações de cada livro (opcional)
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print(f"Available: {stock}")
    print()

# Salvando as informações dos livros em um arquivo JSON
with open("books_info.json", 'w', encoding='utf-8') as json_file:
    json.dump(books_info, json_file, ensure_ascii=False, indent=4)
