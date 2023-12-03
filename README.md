# API Rest para calcular frete.

Bem-vindo à API de Cálculo de Frete! Esta API permite calcular o valor do frete com base nas dimensões e peso do
produto. As requisições devem ser enviadas via método POST, com as informações do produto no corpo da requisição no
formato JSON.
![architecture](/arch.png)

# Endpoint

O endpoint para calcular o frete é:

```bash
POST http://localhost:5000/calcular-frete
```

# Parâmetros da Requisição

A requisição deve incluir as informações do produto no corpo da mensagem, utilizando o formato JSON. Um exemplo válido
seria:

```json
{
  "dimensao": {
    "altura": 102,
    "largura": 40
  },
  "peso": 400
}
```

## Campos Obrigatórios

- dimensao: Objeto contendo as dimensões do produto.
- altura: Altura do produto em centímetros.
- largura: Largura do produto em centímetros.
- peso: Peso do produto em gramas.

# Resposta da API

A API responderá com o valor do frete calculado. O formato da resposta será:

```
[
	{
          "nome":"Entrega Ninja",
    	  "valor_frete": 12.00,
    	  "prazo_dias": 6
	},
	{
    	  "nome":"Entrega KaBuM",
    	  "valor_frete": 8.00,
    	  "prazo_dias": 4
	}
]
```

OBs: caso não atenda os requisitos da transportadora, ela não será retornada na consulta ou será retornado uma lista vazia.


# Códigos de Erro
- **400 Bad Request:** A requisição está mal formada ou faltam parâmetros obrigatórios.
- **500 Internal Server** Error: Um erro interno ocorreu durante o processamento da requisição.


# Como executar ?

Obs: Necessário ter Docker e Docker compose.

Instruções para executar a aplicação:

1. clone o repositório: https://github.com/eltonjncorreia/api-frete
2. entre no diretório raiz do projeto, comando no linux: `cd api-frete/`
3. execute a aplicação com o comando: `docker compose up --build`

Acesse a API no endereço:
http://localhost:5000/docs

# Como está organizado ?

A arquitetura segue a seguinte estrutura:

    infra
        |___api

    shipping_service
        |__domain
            |____ product
            |____ shipping

        |__usecases
            |____ services

    tests
        |___ shipping_service

# Testes

Para executar os testes, entre na raiz do projeto e execute o comando.

`docker compose up integration-tests --build`