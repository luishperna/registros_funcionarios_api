# Importanto APIRouter
from fastapi import APIRouter

# importando classe Funcionario
from db_api.schemas.schemas import Funcionario

# importando cursor e conexao com o banco de dados
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

        desabilitando_autocommit = 'SET autocommit = 0'
        cursor.execute(desabilitando_autocommit)
        conexao.commit()

        iniciando_transacao = 'START TRANSACTION;'
        cursor.execute(iniciando_transacao)
        conexao.commit()

        inserindo_dados_pessoais = f'INSERT INTO dados_pessoais(\
        codigo, nome, data_nascimento, cpf, email) \
        VALUES({codigo}, "{nome}", "{data_nascimento}", "{cpf}", "{email}");'
        cursor.execute(inserindo_dados_pessoais)
        conexao.commit()
        
        inserindo_dados_empregados = f'INSERT INTO dados_empregados(\
        codigo, cargo, data_inicio, data_cancelamento, comportamento) \
        VALUES({codigo}, "{cargo}", "{data_inicio}", "{data_cancelamento}", "{comportamento}");'
        cursor.execute(inserindo_dados_empregados)
        conexao.commit()

        comitando = 'COMMIT;'
        cursor.execute(comitando)
        conexao.commit()

        habilitando_autocommit = 'SET autocommit = 1'
        cursor.execute(habilitando_autocommit)
        conexao.commit()
        return  {
            'Status': 'Cadastrado realizado com sucesso!',
            'Funcionário(a)': f'{nome}',
            'Código': f'{codigo}'
            }
    except:
        return {
            'Status': 'Erro ao cadastrar',
            'Tipo de erro': 'Dados duplicados, faltantes ou incorretos'
            }