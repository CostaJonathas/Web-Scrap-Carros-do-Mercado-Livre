'''
Web Scraper de Anúncios de Carros - Coletando Dados do Mercado Livre

Este script foi desenvolvido para extrair dados de anúncios de veículos do site Mercado Livre,
focando na coleta de informações úteis para análise de mercado automotivo. Utilizamos Selenium
para automatizar a navegação e extração de dados diretamente das páginas de listagem.

🔍 Informações extraídas por veículo:
- Nome do carro
- Ano de fabricação
- Quilometragem
- Preço
- Classificação do preço (Satisfatório, Mediano, Insatisfatório)
- Imagem do anúncio
- Tipo de carroceria (ex: SUV, Sedan, Hatch etc.)
- Região do anúncio

🛠️ Tecnologias utilizadas:
- Python 3.x
- Selenium WebDriver (Google Chrome)
- Bibliotecas: `pandas`, `requests`, `re`, `math`

📍 Como alterar o tipo de carro na pesquisa:
O script está configurado para buscar apenas carros do tipo SUV, mas é possível alterar o tipo 
trocando o código no final da URL original (armazenada na variável `url`). Abaixo estão os códigos
de carroceria aceitos pelo Mercado Livre para você substituir conforme necessário:

| Tipo de Carro       | Código para URL                |
|---------------------|-------------------------------|
| Caminhão leve       | VEHICLE*BODY*TYPE_452764      |
| Conversível         | VEHICLE*BODY*TYPE_452754      |
| Coupé               | VEHICLE*BODY*TYPE_452753      |
| Furgão              | VEHICLE*BODY*TYPE_452763      |
| Hatch               | VEHICLE*BODY*TYPE_452756      |
| Minivan             | VEHICLE*BODY*TYPE_452762      |
| Monovolume          | VEHICLE*BODY*TYPE_452761      |
| Off-Road            | VEHICLE*BODY*TYPE_452757      |
| Perua               | VEHICLE*BODY*TYPE_452755      |
| Pick-up             | VEHICLE*BODY*TYPE_452760      |
| Roadster            | VEHICLE*BODY*TYPE_452765      |
| Sedan               | VEHICLE*BODY*TYPE_452758      |
| SUV                 | VEHICLE*BODY*TYPE_452759      |
| Van                 | VEHICLE*BODY*TYPE_452766      |

💡 Exemplo de URL modificada:
Para buscar apenas por **Sedans**, troque a linha:
url = 'https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/carros_NoIndex_True_VEHICLE*BODY*TYPE_452759'
'''

# Importa as bibliotecas necessárias
import pandas as pd
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configuração do Selenium
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Listas para armazenar os dados coletados
Lnome = []     # Nome do carro
Lano = []      # Ano de fabricação
Lkm = []       # Quilometragem
Lpreco = []    # Preço
Lclass = []    # Classificação de preço (satisfatório, mediano, insatisfatório)
Limg = []      # URL da imagem do carro
Ltipo = []     # Tipo do carro (neste caso, 'SUV' fixo)
Lregiao = []   # Localização (cidade/estado) do vendedor

# URL da primeira página da categoria SUV
url = 'https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/carros_NoIndex_True_VEHICLE*BODY*TYPE_452759'
driver.get(url)

# --- Primeira página: Nome e tipo do carro ---
for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, 'a.ui-search-item__group__element'))):
    Lnome.append(driver.find_elements(By.CSS_SELECTOR, 'a.ui-search-item__group__element')[i].text)
    print(driver.find_elements(By.CSS_SELECTOR, 'a.ui-search-item__group__element')[i].text)
    Ltipo.append('SUV')  # Adiciona o tipo fixo para todos (pode ser dinâmico futuramente)

# Região do vendedor (ex: "São Paulo", "Rio de Janeiro")
for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, 'span.ui-search-item__group__element'))):
    Lregiao.append(driver.find_elements(By.CSS_SELECTOR, 'span.ui-search-item__group__element')[i].text)
    print(driver.find_elements(By.CSS_SELECTOR, 'span.ui-search-item__group__element')[i].text)

# --- Coleta das imagens da primeira página ---
j = 0
while True:
    if j < 48:  # Limita a 48 imagens por página
        try:
            url = driver.find_elements(By.CSS_SELECTOR, 'img.ui-search-result-image__element')[j].get_attribute('src')

            # Ignora imagens base64 usadas como placeholder
            if url.startswith('data:image/gif'):
                continue
            else:
                j += 1
                Limg.append(url)
                print(url)

            # Rola a página a cada 5 imagens para forçar o carregamento lazy loading
            if j % 5 == 0:
                driver.execute_script("window.scrollBy(0, 1000);")
        except:
            continue
    else:
        break

# --- Ano e quilometragem dos carros ---
for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute'))):
    if i % 2 == 0:
        # Alterna entre ano e km
        Lano.append(int(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute')[i].text))
        print(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute')[i].text)
    else:
        Lkm.append(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute')[i].text)
        print(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute')[i].text)

# --- Preço + Classificação ---
for i in range(5, len(driver.find_elements(By.CSS_SELECTOR, 'span.andes-money-amount__fraction'))):
    preco = float(driver.find_elements(By.CSS_SELECTOR, 'span.andes-money-amount__fraction')[i].text))
    Lpreco.append(preco)
    print(preco)

    # Classificação por faixa de preço
    if preco <= 45_000:
        Lclass.append('Satisfatório')
    elif preco >= 85_000:
        Lclass.append('Insatisfatório')
    else:
        Lclass.append('Mediano')

# --- Verifica se existe o botão "Seguinte" ---
if driver.find_elements(By.CSS_SELECTOR, 'span.andes-pagination__arrow-title')[1].text == 'Seguinte':
    proxima = driver.find_elements(By.CSS_SELECTOR, 'span.andes-pagination__arrow-title')[1]
    driver.execute_script("window.scrollBy(0, 100000);")
    proxima.click()

# --- Loop pelas próximas páginas ---
while True:
    # Nome e tipo
    for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, 'a.ui-search-item__group__element'))):
        Lnome.append(driver.find_elements(By.CSS_SELECTOR, 'a.ui-search-item__group__element')[i].text)
        print(driver.find_elements(By.CSS_SELECTOR, 'a.ui-search-item__group__element')[i].text)
        Ltipo.append('SUV')

    # Região
    for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, 'span.ui-search-item__group__element'))):
        Lregiao.append(driver.find_elements(By.CSS_SELECTOR, 'span.ui-search-item__group__element')[i].text)
        print(driver.find_elements(By.CSS_SELECTOR, 'span.ui-search-item__group__element')[i].text)

    # Imagens
    j = 0
    while True:
        if j < 48:
            try:
                url = driver.find_elements(By.CSS_SELECTOR, 'img.ui-search-result-image__element')[j].get_attribute('src')

                if url.startswith('data:image/gif'):
                    continue
                else:
                    j += 1
                    Limg.append(url)
                    print(url)

                if j % 5 == 0:
                    driver.execute_script("window.scrollBy(0, 1000);")
            except:
                continue
        else:
            break

    # Ano e KM
    for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute'))):
        if i % 2 == 0:
            Lano.append(int(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute')[i].text))
            print(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute')[i].text)
        else:
            Lkm.append(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute')[i].text)
            print(driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-card-attributes__attribute')[i].text)

    # Preço + classificação
    for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, 'span.andes-money-amount__fraction'))):
        preco = float(driver.find_elements(By.CSS_SELECTOR, 'span.andes-money-amount__fraction')[i].text))
        Lpreco.append(preco)
        print(preco)

        if preco <= 45_000:
            Lclass.append('Satisfatório')
        elif preco >= 85_000:
            Lclass.append('Insatisfatório')
        else:
            Lclass.append('Mediano')

    # Se ainda tiver página seguinte, clica nela e continua
    if driver.find_elements(By.CSS_SELECTOR, 'span.andes-pagination__arrow-title')[1].text == 'Seguinte':
        proxima = driver.find_elements(By.CSS_SELECTOR, 'span.andes-pagination__arrow-title')[1]
        driver.execute_script("window.scrollBy(0, 100000);")
        proxima.click()
    else:
        break

# --- Impressão de debug: tamanhos das listas ---
print(len(Lnome))
print(len(Lano))
print(len(Lkm))
print(len(Lpreco))
print(len(Lclass))
print(len(Limg))
print(len(Ltipo))
print(len(Lregiao))
