from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import time


# Configurando as opções do Firefox
options = FirefoxOptions()
options.add_argument('--headless') #executando em segundo plano
print('Configurei!')

# Abrindo o navegador
navegador = webdriver.Firefox() #passar aqui o parametro options=options 
print('Abri o navegador')

# Acessando o site do Google
navegador.get("https://www.google.com")
print('acessei o navegador')
time.sleep(6)

print('Já esperei e agora vou embora')
navegador.quit()
print('Finalizei!')