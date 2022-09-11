# Importanto APIRouter
from fastapi import APIRouter

# Importando cursor do banco de dados
from db_config.connection import cursor

# Criando router_get
router = APIRouter()

# Função para consultar um funcionário pelo cpf no banco de dados
@router.get('/', tags=['Consultar funcionário'])
def consultar(cpf:str):
    try:
        numero_cpf = cpf

        obtendo_dados_funcionario = f'SELECT dados_pessoais.codigo, nome, data_nascimento, \
            cpf, email, cargo, data_inicio, data_cancelamento, comportamento\
            FROM dados_pessoais\
            INNER JOIN dados_empregados\
            ON dados_pessoais.codigo = dados_empregados.codigo\
            WHERE dados_pessoais.cpf = "{numero_cpf}";'

        cursor.execute(obtendo_dados_funcionario)

        # Pegando resultado da consulta no banco de dados em forma de lista
        resultado_consulta = cursor.fetchall()

        get_codigo = resultado_consulta[0][0]
        get_nome = resultado_consulta[0][1]
        get_data_nascimento = resultado_consulta[0][2]
        get_cpf = resultado_consulta[0][3]
        get_email= resultado_consulta[0][4]
        get_cargo = resultado_consulta[0][5]
        get_data_inicio = resultado_consulta[0][6]
        get_data_cancelamento = resultado_consulta[0][7]
        get_comportamento = resultado_consulta[0][8]
        return  {
            "codigo": f"{get_codigo}",
            "nome": f"{get_nome}",
            "data_nascimento": f"{get_data_nascimento}",
            "cpf": f"{get_cpf}",
            "email": f"{get_email}",
            "cargo": f"{get_cargo}",
            "data_inicio": f"{get_data_inicio}",
            "data_cancelamento": f"{get_data_cancelamento}",
            "comportamento": f"{get_comportamento}",
            }
    except:
        return {
            "Status": "Erro ao consultar",
            "Tipo de erro": "CPF incorreto ou não cadastrado"
            }