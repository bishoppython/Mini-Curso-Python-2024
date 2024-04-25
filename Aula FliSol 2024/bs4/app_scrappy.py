# Extração de Livros utilizando BeautifulSoup4 como principal fonte de scraping de dados
#  FliSol Palmares - PE 2024 - IFPE

# Aula 01 - Extração Paginação

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Configurações do navegador Firefox
options = Options()
options.headless = False  # Executar em modo headless (sem interface gráfica)
#firefox_driver_path = 'caminho_para_o_executavel_do_geckodriver'  # Substitua pelo caminho do seu executável do geckodriver

# Inicializa o driver do Firefox
driver = webdriver.Firefox(options=options) #, executable_path=firefox_driver_path)

# URL base do site
base_url = 'http://books.toscrape.com/'

# Lista para armazenar os títulos dos livros
book_titles = []

# Loop para navegar por todas as páginas
while True:
    # Carrega a página atual
    driver.get(base_url)
    
    # Extrai o HTML da página
    html = driver.page_source
    
    # Analisa o HTML com BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Encontra todos os títulos dos livros na página atual
    titles = soup.find_all('h3')
    
    # Extrai os títulos dos livros e adiciona à lista
    for title in titles:
        book_titles.append(title.a['title'])
    
    # Verifica se há um link para a próxima página
    next_button = soup.find('li', class_='next')
    if next_button is None:
        break  # Se não houver próximo botão, interrompe o loop
    
    # Constrói a URL da próxima página
    next_page_url = base_url + next_button.a['href']
    
    # Atualiza a URL base para a próxima página
    base_url = next_page_url
    
    # Aguarda alguns segundos para evitar sobrecarregar o servidor
    time.sleep(2)

# Fecha o navegador
driver.quit()

# Cria um DataFrame Pandas com os dados
df = pd.DataFrame({'Title': book_titles})

# Salva os dados em um arquivo Excel
excel_file = 'books_pagine.xlsx'
df.to_excel(excel_file, index=False)

print("Dados extraídos e salvos com sucesso em", excel_file)
