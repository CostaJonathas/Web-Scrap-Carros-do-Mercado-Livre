# Wer Scraping Mercado Livre

# 🔍 Análise de Carros Usados - Web Scraping + SQL + DataFrame

Este projeto realiza **web scraping de anúncios de carros usados** no Mercado Livre, extrai informações detalhadas de cada veículo (como marca, ano, quilometragem e preço), classifica os preços, identifica automaticamente a **marca e imagem da logo** correspondente, e armazena os dados em um **banco de dados SQL Server** para futuras análises no Power BI ou outras ferramentas.

---

## 🚗 Funcionalidades

- Coleta de anúncios de carros usados por tipo (SUV, Sedan, Hatch etc.)
- Extração de:
  - Nome do carro
  - Preço
  - Quilometragem
  - Ano
  - Categoria
  - Localização
  - Imagem do carro
- Classificação automática de preço (Satisfatório, Mediano, Insatisfatório)
- Identificação automática da marca a partir do nome do carro
- Associação com a logo da marca (via links externos)
- Armazenamento dos dados em:
  - Planilha CSV (`carros.csv`)
  - Banco de dados SQL Server

---

## 📂 Estrutura do Projeto

carros_mercado_livre/

├── scraping_carros.py # Web scraping e criação do DataFrame

├── identificar_marca.py # Função para identificar a marca e logo

├── enviar_para_sql.py # Conexão e envio dos dados para o banco SQL Server

├── carros.csv # Arquivo gerado com todos os dados

└── README.md # Documentação do projeto


---

## 🧪 Pré-requisitos

- Python 3
- SQL Server com instância ativa (ex: `SQLEXPRESS`)
- ODBC Driver 17 for SQL Server
- Pacotes Python:

🛠️ Como usar

Configure seu SQL Server e crie o banco de dados Carros com a tabela:

CREATE TABLE Carros (
    Carro NVARCHAR(255),
    Ano NVARCHAR(50),
    Quilometragem NVARCHAR(50),
    Preço NVARCHAR(50),
    Classificação NVARCHAR(50),
    IMG NVARCHAR(MAX),
    Marca NVARCHAR(100),
    IMG_MARCA NVARCHAR(MAX),
    Categoria NVARCHAR(50),
    Região NVARCHAR(100)
)

Rode o scraping para gerar os dados:

Scrap carros sedã.ipynb

Analise os dados com Power BI, Excel ou Dashboards.

🧰 Tecnologias utilizadas:

- Python 3.x
- pandas para análise de dados
- requests e Selenium para scraping
- pyodbc para conexão com SQL Server
- SQL Server Express
- Power BI (opcional)
- CSV como backup local

📈 Objetivo

Criado para praticar Web scrapping de forma mais avançada para ajudar no processo de aprendizado de ETL e visualização de dados, além de servir como base para comparar os preços de carros pelo Power BI calssificando da forma que preferir.

```bash
pip install pandas pyodbc requests selenium
