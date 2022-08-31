# Importanto APIRouter
from fastapi import APIRouter

# Importando classe Funcionario
from db_api.schemas.schemas import Funcionario

# Importando mysql.connector
import mysql.connector

# Importando cursor e conexao com o banco de dados
from db_config.connection import cursor, conexao

# Criando router_post
router = APIRouter()

# Função para cadastrar um funcionário no banco de dados
@router.post('/', tags=['Cadastrar funcionário'])
def cadastrar(funcionario: Funcionario):
    try:
        nome = funcionario.nome
        data_nascimento = funcionario.data_nascimento
        cpf = funcionario.cpf
        email = funcionario.email
        codigo = funcionario.codigo
        cargo = funcionario.cargo
        data_inicio = funcionario.data_inicio
        data_cancelamento = funcionario.data_cancelamento
        comportamento = funcionario.comportamento

        # Verificando se o valor é nulo ou uma data e aplicando as correções nas aspas
        if (data_cancelamento == 'NULL') or (data_cancelamento == 'null'):
            data_cancelamento = data_cancelamento.replace('"','')
        else:
            data_cancelamento = f'"{data_cancelamento}"'

        conexao.autocommit = False

        inserindo_dados_pessoais = f'INSERT INTO dados_pessoais(\
        codigo, nome, data_nascimento, cpf, email) \
        VALUES({codigo}, "{nome}", "{data_nascimento}", "{cpf}", "{email}");'
        cursor.execute(inserindo_dados_pessoais)
        
        inserindo_dados_empregados = f'INSERT INTO dados_empregados(\
        codigo, cargo, data_inicio, data_cancelamento, comportamento) \
        VALUES({codigo}, "{cargo}", "{data_inicio}", {data_cancelamento}, "{comportamento}");'
        cursor.execute(inserindo_dados_empregados)

        conexao.commit()
        return  {
            'Status': 'Cadastrado realizado com sucesso!',
            'Funcionário(a)': f'{nome}',
            'Código': f'{codigo}'
            }
    except mysql.connector.Error as error:
        conexao.rollback()
        return {
            'Status': 'Erro ao cadastrar',
            'Tipo de erro': f'{error}',
            'Causas': 'Dados duplicados, faltantes ou incorretos'
            }