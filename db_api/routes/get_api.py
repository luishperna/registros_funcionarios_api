# Importanto APIRouter
from fastapi import APIRouter

# Importando informações da API
from metadata.home_api import informacoes_api

# Criando router_home
router = APIRouter()

# Rota home da API
@router.get('/', tags=['Home da API'])
def home():
    return informacoes_api