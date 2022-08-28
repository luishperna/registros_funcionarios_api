# Importando BaseModel
from pydantic import BaseModel

# Entrada das informações para cadastrar um funcionário
class Funcionario(BaseModel):
    nome: str
    data_nascimento: str
    cpf: str
    email: str
    codigo: int
    cargo: str
    data_inicio: str
    data_cancelamento: str
    comportamento: str

# Entrada para modificar as informações de um funcionário
# Obs.: atributos aceitos para modificar: 
# cargo, data_inicio, data_cancelamento e comportamento
class Modificacao(BaseModel):
    codigo: int
    atributo: str
    novo_valor: str
    