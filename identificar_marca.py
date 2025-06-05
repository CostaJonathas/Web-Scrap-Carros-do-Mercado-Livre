'''
🏷️ Identificação de Marca e Associação com Imagens

Este trecho do script é responsável por identificar automaticamente a marca de cada carro com base em seu nome
e associar uma imagem correspondente ao logotipo da marca, enriquecendo os dados coletados para uso em relatórios
visuais, dashboards e arquivos CSV finais.

🔎 Funcionalidades principais:
- Varre cada nome de carro coletado anteriormente (lista Lnome) e busca por marcas conhecidas.
- Se encontrar o nome da marca no texto:
  - Adiciona a marca à lista Lmarca.
  - Associa a imagem do logotipo correspondente à lista Marca_img.
  - Remove o nome da marca do título do carro, deixando apenas o modelo (armazenado em Lnomes).

📦 Dados resultantes:
- Lmarca → Lista com as marcas identificadas (ex: Honda, Ford, Hyundai...)
- Marca_img → URLs dos logotipos das marcas, para uso visual.
- Lnomes → Nome do carro com a marca removida (ex: "Civic 2.0 Touring").

🗂️ Dados organizados no dicionário carros_ML:
- 'Carro'         → Lnomes
- 'Ano'           → Lano
- 'Quilometragem' → Lkm
- 'Preco'         → Lpreco
- 'Classificacao' → Lclass
- 'IMG'           → Limg (imagem do anúncio)
- 'Marca'         → Lmarca
- 'IMG_MARCA'     → Marca_img (logotipo da marca)
- 'Categoria'     → Ltipo
- 'Regiao'        → Lregiao

🛠️ Observações:
- A lista de marcas deve estar sincronizada com a lista de imagens (img_marcas).
- A detecção é feita por inclusão do nome da marca no nome do carro (case-insensitive).
- Marcas com variações (ex: 'Lifan' e ' Lifan') são tratadas.
- O resultado final é exportado em um arquivo .csv codificado em UTF-8.
'''

# Lista de marcas que serão buscadas nos nomes dos carros
marcas = [
    "Renault", "Mitsubishi", "Ford", "Citroën", "Chevrolet", "Toyota",
    "Mercedes-benz", "Volkswagen", "Fiat", "Jeep", "Hyundai", "Honda",
    "Kia", "Nissan", "Land Rover", "Bmw", "Suzuki", "Peugeot", "Dodge",
    "Chery", "Volvo", "Audi", "Jac", 'Subaru', 'Jaguar', 'Lexus', 'Mini',
    'Porsche', 'Smart', 'Byd', ' Lifan', 'Troller', 'Lifan', 'Ram'
]

# Lista de URLs das imagens dos logotipos correspondentes às marcas
img_marcas = [
    "https://ibb.co/nB4w8vk", "https://ibb.co/wL1Vy3y", "https://ibb.co/58Q1QR7", "https://ibb.co/HxFTJT7",
    "https://ibb.co/mqCpBCw", "https://ibb.co/2Yrgx99", "https://ibb.co/WPFzN6w", "https://ibb.co/VwjZPwk",
    "https://ibb.co/LnFqLNS", "https://ibb.co/stKwzTH", "https://ibb.co/t2sqf6y", "https://ibb.co/m5hkxQ3",
    "https://ibb.co/25X97T9", "https://ibb.co/GnZRQNp", "https://ibb.co/y4NHk5X", "https://ibb.co/XCs24tx",
    "https://ibb.co/CQ6DjT3", "https://ibb.co/dBjpdFK", "https://ibb.co/tHy3w4r", "https://ibb.co/ctZ5hcc",
    "https://ibb.co/4WnZ209", "https://ibb.co/SKwYP5h", "https://ibb.co/9ZH1cGm", "https://ibb.co/VMXZcM0",
    "https://ibb.co/N7KyxQ7", "https://ibb.co/WFXT49t", "https://ibb.co/TMwzkCW", 'https://ibb.co/Y8QLfkf',
    "https://ibb.co/4SfSfZ8", "https://ibb.co/YtNV5H8", "https://ibb.co/5hYWLMq", "https://ibb.co/xjShY844",
    "https://ibb.co/PN9M26r"
]

# Listas auxiliares para armazenar os resultados do processamento
Marca_img = []  # Armazena o link da imagem da marca identificada
Lmarca = []     # Armazena a marca identificada
Lnomes = []     # Armazena o nome do carro sem a marca

# Função que identifica a marca dentro de um texto e associa a imagem da marca
def identificar_marca(texto):
    for marca in marcas:
        if marca.lower() in texto.lower():  # Verifica se a marca está presente no texto
            Lmarca.append(marca)  # Adiciona a marca encontrada

            # Associa a marca à imagem correta, manualmente indexada
            if marca == "Renault":
                Marca_img.append(img_marcas[19])
            elif marca == "Mitsubishi":
                Marca_img.append(img_marcas[26])
            elif marca == "Ford":
                Marca_img.append(img_marcas[7])
            elif marca == "Citroën":
                Marca_img.append(img_marcas[4])
            elif marca == "Chevrolet":
                Marca_img.append(img_marcas[3])
            elif marca == "Toyota":
                Marca_img.append(img_marcas[22])
            elif marca == "Mercedes-benz":
                Marca_img.append(img_marcas[15])
            elif marca == "Volkswagen":
                Marca_img.append(img_marcas[24])
            elif marca == "Fiat":
                Marca_img.append(img_marcas[6])
            elif marca == "Jeep":
                Marca_img.append(img_marcas[11])
            elif marca == "Hyundai":
                Marca_img.append(img_marcas[25])
            elif marca == "Honda":
                Marca_img.append(img_marcas[8])
            elif marca == "Kia":
                Marca_img.append(img_marcas[12])
            elif marca == "Nissan":
                Marca_img.append(img_marcas[17])
            elif marca == "Land Rover":
                Marca_img.append(img_marcas[13])
            elif marca == "Bmw":
                Marca_img.append(img_marcas[1])
            elif marca == "Suzuki":
                Marca_img.append(img_marcas[21])
            elif marca == "Peugeot":
                Marca_img.append(img_marcas[18])
            elif marca == "Dodge":
                Marca_img.append(img_marcas[5])
            elif marca == "Chery":
                Marca_img.append(img_marcas[2])
            elif marca == "Volvo":
                Marca_img.append(img_marcas[23])
            elif marca == "Audi":
                Marca_img.append(img_marcas[0])
            elif marca == "Jac":
                Marca_img.append(img_marcas[9])
            elif marca == "Subaru":
                Marca_img.append(img_marcas[20])
            elif marca == "Jaguar":
                Marca_img.append(img_marcas[10])
            elif marca == "Lexus":
                Marca_img.append(img_marcas[14])
            elif marca == "Mini":
                Marca_img.append(img_marcas[16])
            elif marca == "Smart":
                Marca_img.append(img_marcas[27])
            elif marca == "Byd":
                Marca_img.append(img_marcas[28])
            elif marca == "Lifan" or marca == " Lifan":
                Marca_img.append(img_marcas[29])
            elif marca == "Troller":
                Marca_img.append(img_marcas[30])
            elif marca == "Porsche":
                Marca_img.append(img_marcas[31])
            elif marca == "Ram":
                Marca_img.append(img_marcas[32])

            # Remove a marca do nome original do carro para deixar apenas modelo e versão
            Lnomes.append(i.replace(marca, ''))
            break  # Para de procurar após encontrar a primeira marca válida

# Percorre a lista `Lnome` e chama a função para identificar marca de cada item
for i in Lnome:
    texto = i
    identificar_marca(texto)

# Cria o dicionário com todos os dados organizados
carros_ML = {
    'Carro' : Lnomes,              # Nome do carro sem a marca
    'Ano' : Lano,                  # Ano do carro
    'Quilometragem' : Lkm,         # Quilometragem
    'Preco' : Lpreco,              # Preço
    'Classificacao' : Lclass,      # Classificação do preço (bom, médio, ruim)
    'IMG' : Limg,                  # Imagem do carro
    'Marca' : Lmarca,              # Marca identificada
    'IMG_MARCA' : Marca_img,       # Imagem do logotipo da marca
    'Categoria' : Ltipo,           # Tipo de carro (SUV, Sedan etc.)
    'Regiao' : Lregiao             # Localização do anúncio
}

# Impressão de verificação para checar se todas as listas têm o mesmo tamanho
print(len(Lmarca))
print(len(Marca_img))
print(len(Lnomes))
print(len(Lnome))

# Criação do DataFrame e exportação para CSV
df = pd.DataFrame(carros_ML)
df = df[['Carro', 'Ano', 'Quilometragem', 'Preco', 'Classificacao', 'IMG', 'Marca', 'IMG_MARCA', 'Categoria', 'Regiao']]
df.to_csv('carros.csv', index=False, encoding='utf-8')  # Exporta o arquivo CSV final
