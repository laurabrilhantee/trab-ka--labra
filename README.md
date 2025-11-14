# API de Endereço
A API permite criar, ler, atualizar e excluir registros de endereços de forma simples e organizada, seguindo o padrão CRUD (Create, Read, Update, Delete).

Este é um projeto inicial de CRUD (Create, Read, Update, Delete),que será expandido no futuro. Este é apenas o escopo inical.

## Funcionalidades

- **GET /enderecos**: Retorna a lista completa de endereços cadastrados no banco.
- **GET /endereco/<id>**: Retorna as informações de um endereço específico pelo ID.
- **POST /endereco**: Adiciona um novo endereço ao banco de dados.
- **PUT /endereco/<id>**: Atualiza todas as informações de um endereço específico.
- **DELETE /endereco/<id>**: Remove um endereço específico do banco.


## Estrutura do Projeto

- **app.py**: Arquivo principal que inicializa o servidor Flask e registra as rotas.
- **db.py**: Configuração do banco de dados SQLite utilizando SQLAlchemy.
- **endereco.db**: Banco de dados SQLite onde os endereços são armazenados.
- **/models/endereco_models.py**: Contém a classe Endereco (model) com todos os campos do banco.
- **/routes/endereco_routes.py**: Arquivo onde ficam todas as rotas da API (CRUD).
- **Comandos_Postman.txt**: Arquivo com exemplos de requisições para testar a API.
- **README.md**: Documentação completa do projeto.


## Endpoints

### 1. **GET /enderecos**

Retorna a lista completa de endereços cadastrados no banco.

#### Exemplo de Resposta:
[
  {
    "id": 1,
    "cep": "60743-330",
    "logradouro": "Rua das Flores",
    "complemento": "Apartamento 301",
    "unidade": "Residencial",
    "bairro": "Serrinha",
    "localidade": "Fortaleza",
    "uf": "CE",
    "estado": "Ceará",
    "regiao": "Nordeste",
    "ibge": "2304400",
    "gia": null,
    "ddd": "85",
    "siafi": "1389"
  },
  {
    "id": 2,
    "cep": "01001-000",
    "logradouro": "Praça da Sé",
    "complemento": "",
    "unidade": "",
    "bairro": "Sé",
    "localidade": "São Paulo",
    "uf": "SP",
    "estado": "São Paulo",
    "regiao": "Sudeste",
    "ibge": "3550308",
    "gia": "1004",
    "ddd": "11",
    "siafi": "7107"
  }
]

### 2. **GET /endereco/<id>**

Retorna as informações de um endereço específico pelo **ID**.

### Exemplo de Requisição:

GET /endereco/1

### Exemplo de Resposta:

{
  "id": 1,
  "cep": "60743-330",
  "logradouro": "Rua das Flores",
  "complemento": "Apartamento 301",
  "unidade": "Residencial",
  "bairro": "Serrinha",
  "localidade": "Fortaleza",
  "uf": "CE",
  "estado": "Ceará",
  "regiao": "Nordeste",
  "ibge": "2304400",
  "gia": null,
  "ddd": "85",
  "siafi": "1389"
}
### 3. **POST /endereco**

Adiciona um novo endereço ao banco de dados.

#### Exemplo de Requisição:

POST /endereco

**Content-Type:** application/json

{
  "cep": "60743-330",
  "logradouro": "Rua das Flores",
  "complemento": "Apartamento 301",
  "unidade": "Residencial",
  "bairro": "Serrinha",
  "localidade": "Fortaleza",
  "uf": "CE",
  "estado": "Ceará",
  "regiao": "Nordeste",
  "ibge": "2304400",
  "gia": null,
  "ddd": "85",
  "siafi": "1389"
}

#### Exemplo de Resposta:

{
  "id": 3,
  "cep": "60743-330",
  "logradouro": "Rua das Flores",
  "complemento": "Apartamento 301",
  "unidade": "Residencial",
  "bairro": "Serrinha",
  "localidade": "Fortaleza",
  "uf": "CE",
  "estado": "Ceará",
  "regiao": "Nordeste",
  "ibge": "2304400",
  "gia": null,
  "ddd": "85",
  "siafi": "1389"
}

## 4. **PUT /endereco/<id>**

Atualiza todas as informações de um endereço específico pelo **ID**.

#### Exemplo de Requisição:

PUT /endereco/3

**Content-Type:** application/json

{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "",
  "unidade": "",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "estado": "São Paulo",
  "regiao": "Sudeste",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}
### 5. **DELETE /endereco/<id>**

Remove um endereço específico pelo **ID**.

#### Exemplo de Requisição:

DELETE /endereco/3

#### Exemplo de Resposta:

{
  "mensagem": "Endereço removido com sucesso"
}

## Como Rodar o Projeto

1. **Clone este repositório:**

  ```bash
  git clone https://github.com/laurabrilhantee/trab-ka--labra.git
  ```

2. **Instale as dependências:**

  Navegue até o diretório do projeto e execute o comando:

  ```bash
  pip install -r requirements.txt
  ```
3. **Inicie o servidor**
  Após a instalação das dependências, inicie o servidor:

  ```bash
  py app.py
  ```
4. **Acesse a API**

A API está disponível em [http://127.0.0.1:5000]

## Validações 

Os dados enviados para a API são validados com Flask e SQLAlchemy para garantir que todos os campos sejam fornecidos corretamente. As validações incluem:

- **CEP** deve estar no formato válido (ex: 00000-000).
- **Logradouro, bairro, localidade, estado e UF** são obrigatórios.
- **UF** deve ter exatamente **2 caracteres** (ex: CE, SP, RJ).
- O **ID deve existir** para operações de consulta, atualização e remoção.

### Dicas:
- https://dillinger.io/ — Para visualizar o README formatado antes de enviar ao GitHub.
- https://readme.so/pt/editor — Para montar o README de forma automática.


## Autor

Desenvolvido por Laura Brilhante e Vinicius Brazão