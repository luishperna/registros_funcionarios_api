# Importanto APIRouter
from fastapi import APIRouter

# importando classe Modificacao
from db_api.schemas.schemas import Modificacao

# importando cursor do banco de dados
from db_config.connection import cursor, conexao

# Criando router_patch
router = APIRouter()

# Função para modificar informações em dados_empregados no banco de dados
@router.patch('/', tags=['Modificar informações'])
def modificar(modificacao: Modificacao):
    try:
        codigo = modificacao.codigo
        atributo = modificacao.atributo
        novo_valor = modificacao.novo_valor

        if atributo == 'codigo':
            return{
                'Status': 'Erro ao modificar',
                'Tipo de erro': 'O atributo codigo não pode ser modificado'
                }
        else:
            modificando_dados_empregados = f'UPDATE dados_empregados \
            SET {atributo} = "{novo_valor}" \
            WHERE codigo = {codigo};'
            cursor.execute(modificando_dados_empregados)
            conexao.commit()
            return {
                    'Status': f'{codigo} - Modificação realizado com sucesso!',
                    'Atualização': f'Atributo {atributo} setado para {novo_valor}',
                    }
    except:
        return {
            'Status': 'Erro ao modificar',
            'Tipo de erro': 'Dados faltantes ou incorretos'
            }