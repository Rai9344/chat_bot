# importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# nav wtz web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#definir contatos e grupos e mensagens a ser enviadas
contatos = ['nome do contato', 'nome do grupo ']
mensagem = 'Ola pessoal, essa mensagem foi enviada automaticamente, ela foi criada em python, caso você tenha recebida o codigo rodou.'
#search groups
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(0.10)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(0.5)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)




for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

# campo de pesquisa 'copyable-text selectable-text'

#campo de msg 'copyable-text selectable-text'

# send msg to contact or group