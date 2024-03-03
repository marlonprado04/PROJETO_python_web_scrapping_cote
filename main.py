
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
html_elements = list_css_selector_elements("span strong, ul")

# Inicializa a lista de spans
spans = []

# Inicializa a lista de links
links = []

# Agrupa os spans e listas de links
for html_element in html_elements:
    print(html_element)
    # Parseia o elemento HTML
    soup = BeautifulSoup(html_element, 'html.parser')
    if soup.name == 'span':
        if spans:
            spans[-1]['links'] = links
            links = []  # Limpa a lista de links para o próximo grupo
        spans.append({'span': str(soup), 'links': []})
    elif soup.name == 'ul':
        links.extend([str(link) for link in soup.find_all('a')])
    
# Imprime o resultado
for group in spans:
    print(group['span'])
    for link in group['links']:
        print(link)

# Após a raspagem, fecha o navegador
driver.quit()
