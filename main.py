"""
Opção de passos 1:
1. Código acessa a página raiz contendo todos os links dos capítulos
2. Código varre e agrupa todos os links de acordo com a seção do volume específico
3. Código acessa cada link individualmente, renderiza o HTML e faz o scrapping do texto e imagem formatado
4. Código cria arquivo .ODT e salva as imagens e textos formatados no arquivo criado (com o nome do capítulo)
5. Código retorna para etapa 1


Opção de passos 2:

1. Usuário vai copiar a URL específica que deseja fazer download (pois são muitas variações possíveis, impossível de colocar no código)
2. Código renderiza o HTML e faz o scrapping do texto e imagem formatado
3. Código cria arquivo .ODT e salva as imagens e textos formatados no arquivo criado (com o nome do capítulo)
4. Usuário retorna para etapa 1


Links de exemplo:

https://animecenterbr.com/youkoso-jitsuryoku-prologo-vol-1/
https://animecenterbr.com/youkoso-jitsuryoku-capitulo-1-vol-1/
https://animecenterbr.com/youkoso-jitsuryoku-vol-1-ss-horikita-uma-certa-manha-na-piscina/
    
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações do WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

# URL da página da web que você deseja analisar
url = "https://animecenterbr.com/youkoso-jitsuryoku-light-novel-pt-br"

# Carrega a página
driver.get(url)

# Espera até que o body seja carregado na página
wait = WebDriverWait(driver, 10)
try:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
except Exception as e:
    print("TimeoutException:", e)

# Encontra todos os links das tags <a> contidos nas <li>
links = driver.find_elements(By.CSS_SELECTOR, '#post-1309 > div > div:nth-child(1) > div.col-12.col-lg-8.mb-3.order-2.order-lg-1 > div.row > div.col-12.col-xl-9.mb-3.order-1.order-xl-2 > div.post-text-content.my-3 > ul:nth-child(13) > li > a')

# Imprime os links
for link in links:
    print(link.get_attribute("href"))

# Após a raspagem, feche o navegador
driver.quit()

