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

# Importações
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Configurações do WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

# URL da página
url = "https://animecenterbr.com/youkoso-jitsuryoku-light-novel-pt-br"

# Carrega a página
driver.get(url)

# Define função para aguardar renderização do body
def render_body_content(seconds=10):
    # Espera até que o body seja carregado na página
    wait = WebDriverWait(driver, seconds)
    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except Exception as e:
        print("TimeoutException:", e)

# Define função para retornar uma lista de elementos de determinadas tags
def list_tag_elements(tag):
    # Renderiza body
    render_body_content()

    # Encontra todas as tags procuradas na página
    tags = driver.find_elements(By.TAG_NAME, tag)

    # Cria variável para armazenar tags
    values = []
    
    # Armazena cada elemento na lista de valores
    for element in tags:
        values.append(element.get_attribute("outerHTML"))
    
    return values

# Define função para retornar uma lista de elementos de determinada css selector
def list_css_selector_elements(selector):
    # Renderiza body
    render_body_content()

    # Encontra todas as tags procuradas na página através do css selector
    tags = driver.find_elements(By.CSS_SELECTOR, selector)

    # Cria variável para armazenar tags
    values = []
    
    # Armazena cada elemento na lista de valores
    for element in tags:
        values.append(element.get_attribute("outerHTML"))
    
    return values
    
# Obtém o HTML dos elementos
html_elements = list_css_selector_elements("li>a")

# Imprime o HTML formatado para cada elemento
for html_element in html_elements:
    soup = BeautifulSoup(html_element, 'html.parser')
    print(soup.prettify()) 

# Após a raspagem, fecha o navegador
driver.quit()