# desafio_frexco
  Api realizada para o desafio Frexco
 
## :construction: Status <br/>
🚀 Concluído

## :toolbox: Tecnologias
* [Django](https://www.djangoproject.com)
* [Django Rest Framework](https://www.django-rest-framework.org)
* [SQLite](https://sqlite.org/index.html)

## :hammer_and_wrench: Preparando o ambiente
```   
# Clone este repositório:
 $ git clone <https://github.com/felipemdf/desafio_frexco.git>

# Acesse a pasta do projeto no terminal/cmd 
 $ cd ./desafio_frexco/
 
# Acesse a url no seu navegador
  <http://localhost:8080>
```

## Endpoints
  ### GET /regions
  Responsável por retornar a listagem de todas as regiões cadastradas no banco de dados.
  #### Parâmetros
  Nenhum
  #### Respostas
  ##### OK! 200
  Exemplo de resposta:
  ```
  [
    {
      "id": 5,
      "name": "Mamão",
      "region_id": 4
    },
    {
      "id": 6,
      "name": "Abacaxi",
      "region_id": 5
    },
    {
      "id": 7,
      "name": "Ameixa",
      "region_id": 5
    }
  ]
  ```
  ### GET /regions/${id}
  Listagem de uma região no banco de dados.
  #### Parâmetros
  id.
  #### Respostas
  ##### OK! 200
  Exemplo de resposta:
  ```
  {
    "id": 4,
    "name":"Norte",
  }
  ```
  
  ### POST /regions
  Criação de uma nova região no banco de dados.
  #### Parâmetros
  name: nome de uma região.
  #### Respostas
  ##### Created! 201
  Exemplo de resposta:
  ```
  {
    "id": 4,
    "name":"norte",
  }
  ```
  
  ### PUT /regions/${id}
  Atualização de uma região já existente no banco de dados.
  #### Parâmetros
  name: nome de uma região.
  #### Respostas
  ##### OK! 200
  Exemplo de resposta:
  ```
  {
    "id": 4,
    "name":"Sul",
  }
  ```
  ### DELETE /regions/${id}
  Remoção de uma região no banco de dados.
  #### Parâmetros
  id.
  #### Respostas
  ##### No Content! 204
  Exemplo de resposta:
  ```
  No body returned for response
  ```
  
  ### GET /fruits
  Responsável por retornar a listagem de todas as frutas cadastradas no banco de dados.
  #### Parâmetros
  Nenhum
  #### Respostas
  ##### OK! 200
  Exemplo de resposta:
  ```
  [
    {
      "id": 5,
      "name": "Mamão",
      "region_id": 4
    },
    {
      "id": 6,
      "name": "Abacaxi",
      "region_id": 5
    },
    {
      "id": 7,
      "name": "Ameixa",
      "region_id": 5
    }
  ]
  ```
  ### GET /fruits/${id}
  Listagem de uma fruta no banco de dados.
  #### Parâmetros
  id.
  #### Respostas
  ##### OK! 200
  Exemplo de resposta:
  ```
  {
    "id": 7,
    "name":"Ameixa",
    "region_id": 5
  }
  ```
  
  ### GET /region/${id}/fruits
  Listagem de frutas em uma região.
  #### Parâmetros
  id.
  #### Respostas
  ##### OK! 200
  Exemplo de resposta:
  ```
  [
    {
      "name": "Abacaxi"
    },
    {
      "name": "Ameixa"
    },
    {
      "name": "Uva"
    }
  ]
  ```
  
  ### POST /fruits
  Criação de uma nova fruta no banco de dados.
  #### Parâmetros
  name: nome de uma fruta.
  region_id: id de uma região.
  #### Respostas
  ##### Created! 201
  Exemplo de resposta:
 ```
  {
    "id": 7,
    "name":"Ameixa",
    "region_id": 5
  }
  ```
  
  ### PUT /fruits/${id}
  Atualização de uma fruta já existente no banco de dados.
  #### Parâmetros
  name: nome de uma fruta.
  region_id: id de uma região.
  #### Respostas
  ##### OK! 200
  Exemplo de resposta:
 ```
  {
    "id": 7,
    "name":"Ameixa",
    "region_id": 6
  }
  ```
  ### DELETE /fruits/${id}
  Remoção de uma fruta no banco de dados.
  #### Parâmetros
  id.
  #### Respostas
  ##### No Content! 204
  Exemplo de resposta:
  ```
  No body returned for response
  ```
