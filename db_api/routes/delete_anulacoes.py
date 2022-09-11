# Importanto APIRouter
from fastapi import APIRouter

# Criando router_delete
router = APIRouter()

# Importando cursor e conexao com o banco de dados
from db_config.connection import cursor, conexao

# Função para anulação de um registro de um funcionário no banco de dados
@router.delete('/', tags=['Anular registro'])
def anular(cpf:str):
    numero_cpf = cpf

    anulando_registro = f'DELETE dados_pessoais, dados_empregados \
    FROM dados_pessoais \
    INNER JOIN dados_empregados \
    ON dados_pessoais.codigo = dados_empregados.codigo \
    WHERE dados_pessoais.cpf = "{numero_cpf}";'
    cursor.execute(anulando_registro)
    conexao.commit()
    return {
        "Status": "Anulação realizada com sucesso!",
        "Anulação": f"Deletado registro com CPF {numero_cpf}",
        }