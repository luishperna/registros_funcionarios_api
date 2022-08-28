# Importando bibliotecas/módulos para integração com banco de dados - MySQL
import mysql.connector
from dotenv import load_dotenv
from os import getenv

# Carregando as variáveis de ambiente
load_dotenv()

# Realizando a conexão com o banco de dados
conexao = mysql.connector.connect(
    host=getenv('HOST'),
    user=getenv('USER'),
    password=getenv('PASSAWORD'),
    database=getenv('DATABASE')
)

# Executando a conexão no banco de dados
cursor = conexao.cursor()