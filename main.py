# Importando FastAPI
from fastapi import FastAPI

# Importando CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

# Importando descrição da API
from metadata.description_api import descricao

# Importando rotas
from db_api.routes.get_home import router as router_home
from db_api.routes.get_status import router as router_status
from db_api.routes.get_consultas import router as router_get
from db_api.routes.post_cadastros import router as router_post
from db_api.routes.patch_modificacoes import router as router_patch
from db_api.routes.delete_anulacoes import router as router_delete

# Criando API
app = FastAPI(
    title='RegistrosFuncionariosAPI',
    description=descricao,
    version='1.0.0',
    contact={
         "name": "Luís Perna",
         "url": "https://luishperna.com.br/",
    }
)

# Liberando CORS (Compartilhamento de Recursos de Origem Cruzada) do navegador
# Possibilitando a comunicação entre um Front-End com JavaScript e um Back-End externo, no caso a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utilizando as rotas
app.include_router(router=router_home)
app.include_router(router=router_status, prefix='/status')
app.include_router(router=router_post, prefix='/funcionarios/cadastros')
app.include_router(router=router_get, prefix='/funcionarios/consultas/{cpf}')
app.include_router(router=router_patch, prefix='/funcionarios/modificacoes')
app.include_router(router=router_delete, prefix='/funcionarios/anulacoes/{cpf}')
