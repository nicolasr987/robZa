#importar blibiotecas
#navegar pro zap web
#mandarmensagem
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(50)
contatos = ['Bobocas , Jessica Meu Amor Minha Vida']
mensagem = ['manda foto da ra.....']
def buscar_contatos(contato): campo_pesquisa == driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
time.sleep(5)
campo_pesquisa.click()
campo_pesquisa.send_keys(contato)
campo_pesquisa.send_keys(Keys.ENTER)
 
for contato in contatos:
   buscar_contatos(contato)
   enviar_mensagem(mensagem)
       #copyable-text selectable-text
       