from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import time


# Configurando as opções do Firefox
options = FirefoxOptions()
options.add_argument('--headless')

# Abrindo o navegador
navegador = webdriver.Firefox()

# Acessando o site do Google
navegador.get("https://www.google.com")

# Encontrando o campo de busca e digitando a consulta
search_box = navegador.find_element(By.NAME, 'q')
search_box.send_keys("valor do dólar hoje")
search_box.send_keys(Keys.RETURN)

# Esperando a página carregar
time.sleep(5)

# Encontrando e imprimindo o valor do dólar
dolar_element = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
extenso_value = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[2]')
print("Valor do dólar hoje:", 'R$' + dolar_element.text + ' ' + extenso_value.text)
time.sleep(4)

# Fechando o navegador
navegador.quit()
