# Importando FastAPI
from fastapi import FastAPI

# Importando descrição da API
from metadata.description_api import descricao

# Importando rotas
from db_api.routes.get_api import router as router_home
from db_api.routes.get_status import router as router_status
from db_api.routes.get_consultas import router as router_get
from db_api.routes.post_cadastros import router as router_post
from db_api.routes.patch_modificacoes import router as router_patch
from db_api.routes.delete_anulacoes import router as router_delete

# Criando API
api = FastAPI(
    title='RegistrosFuncionariosAPI',
    description=descricao,
    version='1.0.0',
    contact={
         "name": "Luís Perna",
         "url": "https://luishperna.com.br/",
    }
)

# Utilizando as rotas
api.include_router(router=router_home, prefix='/api')
api.include_router(router=router_status, prefix='/api/status')
api.include_router(router=router_post, prefix='/funcionarios/cadastros')
api.include_router(router=router_get, prefix='/funcionarios/consultas/{cpf}')
api.include_router(router=router_patch, prefix='/funcionarios/modificacoes')
api.include_router(router=router_delete, prefix='/funcionarios/anulacoes/{cpf}')
