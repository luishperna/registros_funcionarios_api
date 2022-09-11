# Importanto APIRouter
from fastapi import APIRouter

# Criando router_status
router = APIRouter()

# Função para retorno de status da API
@router.get('/', tags=['Verificar status da API'])
def status():
    return {"Api": "Rodando"}