# Extração de Livros utilizando BeautifulSoup4 como principal fonte de scraping de dados
#  FliSol Palmares - PE 2024 - IFPE

# Aula 01 - Extração simples

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd

# Configurações do navegador Firefox
options = Options()
options.headless = False 

# Executar em modo headless (sem interface gráfica)
# firefox_driver_path = 'geckodriver.exe' 
# Substitua pelo caminho do seu executável do geckodriver

# Inicializa o driver do Firefox
driver = webdriver.Firefox(options=options)

# URL do site
url = 'http://books.toscrape.com/'

# Carrega a página
driver.get(url)

# Extrai o HTML da página
html = driver.page_source

# Fecha o navegador
driver.quit()

# Analisa o HTML com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontra todos os títulos dos livros
titles = soup.find_all('h3')

# Lista para armazenar os títulos dos livros
book_titles = []

# Extrai os títulos dos livros
for title in titles:
    book_titles.append(title.a['title'])
    print(book_titles)

# Cria um DataFrame Pandas com os dados
df = pd.DataFrame({'Title': book_titles})

# Salva os dados em um arquivo Excel
excel_file = 'books.xlsx'
df.to_excel(excel_file, index=False)

print("Dados extraídos e salvos com sucesso em", excel_file)
