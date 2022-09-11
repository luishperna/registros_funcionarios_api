<h1 align="center">RegistrosFuncionariosApi</h1>

<p align="center">
<img src="https://img.shields.io/badge/operações-crud-539cf2?style=for-the-badge"/>
<img src="https://img.shields.io/badge/api-v1.0.0-009485?style=for-the-badge"/>
<img src="https://img.shields.io/badge/python-346f9e?style=for-the-badge&logo=python&logoColor=ffdd54"/>
<img src="https://img.shields.io/badge/FastAPI-2e303e?style=for-the-badge&logo=fastapi"/>
<img src="https://img.shields.io/badge/mysql-00758f.svg?style=for-the-badge&logo=mysql&logoColor=white"/>
</p>

Esta Interface de Programação de Aplicação (API) proporciona as 4 principais operações para controlar registros de funcionários em um banco de dados SGBD MySQL, o famoso CRUD:

 - **C**reate ➔ Cadastrar informações de um funcionário
 - **R**ead ➔ Consultar informações de um funcionário
 - **U**pdate ➔ Modificar informações de um funcionário
 - **D**elete ➔ Anular registro de um funcionário
 
---

## :blue_book: Documentação

Acesse a **documentação da RegistrosFuncionariosApi** para saber mais sobre a API e como utilizá-la.

Disponível em: [https://registros-funcionarios-api-docs.luishperna.com.br](https://registros-funcionarios-api-docs.luishperna.com.br)

---

## :oncoming_automobile: URLs - Rotas

Rotas (endpoint) para acesso à RegistrosFuncionariosAPI:

1. **Home**

    `URL` [https://registros-funcionarios-api.luishperna.com.br](https://registros-funcionarios-api.luishperna.com.br)

2. **Swagger UI/OpenAPI**

    `URL` [https://registros-funcionarios-api.luishperna.com.br/docs](https://registros-funcionarios-api.luishperna.com.br/docs)

    `URL` [https://registros-funcionarios-api.luishperna.com.br/openapi.json](https://registros-funcionarios-api.luishperna.com.br/openapi.json)

3. **Status**

    `URL` [https://registros-funcionarios-api.luishperna.com.br/status](https://registros-funcionarios-api.luishperna.com.br/status)

4. **Cadastros**

    `URL` [https://registros-funcionarios-api.luishperna.com.br/funcionarios/cadastros](https://registros-funcionarios-api.luishperna.com.br/funcionarios/cadastros)

5. **Consultas**

    `URL` [https://registros-funcionarios-api.luishperna.com.br/funcionarios/consultas/{cpf}](https://registros-funcionarios-api.luishperna.com.br/funcionarios/consultas/{cpf})

6. **Modificações**

    `URL` [https://registros-funcionarios-api.luishperna.com.br/funcionarios/modificacoes](https://registros-funcionarios-api.luishperna.com.br/funcionarios/modificacoes)

7. **Anulações**

    `URL` [https://registros-funcionarios-api.luishperna.com.br/funcionarios/anulacoes/{cpf}](https://registros-funcionarios-api.luishperna.com.br/funcionarios/anulacoes/{cpf})


---

## :left_right_arrow: Compatibilidade

A RegistrosFuncionariosAPI utiliza do formato `JSON` para realizar as comunicações entre os sistemas, assim facilitando o tráfego de dados entre aplicações distintas e havendo um ponto em comum entre diversas linguagens de programação.

---

## :warning: Finalidade da API

A API foi desenvolvida com a finalidade de simular uma aplicabilidade em uma empresa fictícia, sendo assim, não apresentando usabilidade real.

O foco da RegistrosFuncionariosApi é apenas para fins de estudo pessoal sobre Interface de Programação de Aplicações.

---

## :no_entry_sign: Restrição do uso da API

A utilização da RegistrosFuncionariosAPI está restrita apenas para testes ou fins de estudo sobre consumo de API, visto que os dados inseridos poderam ser acessados, alterados ou apagados por qualquer usuário com acesso a API.

Além disso, a API e o banco de dados estão sujeitos a paradas ou desligamento por fatores externos, como os serviços de hospedagens utilizados para o deploy das aplicações.

---

## :man_technologist: Tecnologias utilizadas

- Linguagem de Programação: `python`

- Framework Web: `FastAPI`

- Validação de Dados: `pydantic`

- Servidor Web ASGI: `uvicorn`

- SGBD: `MySQL`

- Driver MySQL: `mysql-connector-python`

- Gerenciamento Variáveis de Ambiente: `python-dotenv`

- Hospedagem/Deploy:
  - API: `Vercel`
  - MySQL: `db4free`

- Editor de Código/IDE: `visual studio code`

- Versionamento e repositório remoto: `git` `github`

---

## Autor

| [<img src="https://avatars.githubusercontent.com/u/96630233?s=400&u=3400cfe6ba8fb87692f4f14cbdbef3e5cc996b67&v=4" width=115><br><sub>Luís Henrique Perna</sub>](https://github.com/luishperna) |
| :---: |