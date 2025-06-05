# SCRIPT: Inserção de dados de carros do Mercado Livre em SQL Server
#
# OBJETIVO:
# Este script tem como objetivo transferir os dados tratados de um DataFrame (df), contendo
# informações de veículos extraídos do Mercado Livre, para uma tabela chamada "Carros" no
# banco de dados SQL Server local. Antes da inserção, os registros da categoria "SUV" são
# excluídos da tabela para evitar duplicidade.
#
# FUNCIONALIDADES:
# - Conexão com o banco de dados SQL Server usando autenticação do Windows.
# - Remoção de registros antigos da tabela `Carros` com base na categoria.
# - Inserção de novos dados para cada linha do DataFrame:
#   → Carro: nome/título do anúncio
#   → Ano: ano de fabricação
#   → Quilometragem: km rodados
#   → Preço: valor do carro
#   → Classificacao: avaliação de preço (satisfatório, mediano, insatisfatório)
#   → IMG: link da imagem do carro
#   → Marca: marca identificada
#   → IMG_MARCA: imagem do logotipo da marca
#   → Categoria: tipo de carro (SUV, Sedan, Hatch, etc.)
#   → Regiao: localização do anúncio
#
# PRÉ-REQUISITOS:
# - O DataFrame `df` precisa estar previamente carregado e formatado corretamente.
# - A tabela `Carros` já deve existir no banco com as colunas correspondentes.
# - O driver ODBC do SQL Server deve estar instalado na máquina.
#
# OBSERVAÇÕES:
# - Este script exclui apenas os carros da categoria "SUV" antes de inserir novos.
#   Para outras categorias, o comportamento precisa ser adaptado.
# - Certifique-se de que não há valores nulos nas colunas obrigatórias do DataFrame.
# - A conexão usa "Trusted_Connection=yes", ou seja, autenticação via login do Windows.

import pyodbc  # Importa a biblioteca para conectar com o banco de dados SQL Server via ODBC

# Define o nome do servidor SQL Server (substitua pelo nome real da sua instância local)
server = '{COLOQUE O NOME DO SEU SERVIDOR AQUI}\SQLEXPRESS'

# Nome do banco de dados que será usado
database = 'Carros'

# Monta a string de conexão com o banco usando o driver ODBC e autenticação do Windows
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'

# Estabelece a conexão com o banco de dados
conn = pyodbc.connect(connection_string)

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Remove registros antigos da tabela 'Carros' apenas da categoria 'SUV'
cursor.execute("DELETE FROM Carros WHERE Categoria = 'SUV'")

# Percorre cada linha do DataFrame df para inserir os dados no banco
for index, row in df.iterrows():
    # Essas atribuições são redundantes (opcional remover), mas representam as colunas que serão usadas
    row['Carro'] = row['Carro']
    row['Ano'] = row['Ano']
    row['Quilometragem'] = row['Quilometragem']
    row['Preco'] = row['Preco']
    row['Classificacao'] = row['Classificacao']
    row['IMG'] = row['IMG']
    row['Marca'] = row['Marca']
    row['IMG_MARCA'] = row['IMG_MARCA']
    row['Categoria'] = row['Categoria']
    row['Regiao'] = row['Regiao']
    
    # Insere os dados da linha atual na tabela 'Carros'
    cursor.execute(
        "INSERT INTO Carros (Carro, Ano, Quilometragem, Preço, Classificação, IMG, Marca, IMG_MARCA, Categoria, Região) values(?,?,?,?,?,?,?,?,?,?)",
        row['Carro'], row['Ano'], row['Quilometragem'], row['Preco'], row['Classificacao'],
        row['IMG'], row['Marca'], row['IMG_MARCA'], row['Categoria'], row['Regiao']
    )

# Confirma todas as alterações feitas no banco (commit das inserções)
conn.commit()

# Fecha a conexão com o banco
conn.close()

# Informa no terminal que os dados foram enviados com sucesso
print("Enviado para o SQL")
