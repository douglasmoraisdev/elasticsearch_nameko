# Elasticsearch Nameko

Lib para utilizar Elasticsearch no framework Nameko.


## Instalação
Adicionar ao `requirements.txt` do projeto:

```
git+https://github.com/douglasmoraisdev/elasticsearch_nameko.git#egg=elasticsearch_nameko
```

OU manualmente com PIP:
```bash
$ pip install git+https://github.com/douglasmoraisdev/elasticsearch_nameko.git#egg=elasticsearch_nameko
```



## Configuração
A Lib utiliza `o arquivo config.yml` para sua configuração. As mesmas podem ser encontradas no arquivo 'sample.config.yml', e consumidas via arquivo .env, se for o padrão do projeto.

```yml
ELASTIC_HOST: # Host Elasticsearch
ELASTIC_INDEX: # Index Elasticsearch
ELASTIC_PORT: # Porta Elasticsearch
ELASTIC_USER: # Usuario Elasticsearch
ELASTIC_PASS: # Password Elasticsearch

```

## Importação e uso
Para utilizar o log basta importar o objeto `elasticsearch_nameko` da package e utilizar os métodos.

## Métodos

### bulk_post(bulk_body: list)
Realiza um post em bulk para o índice configurado.

#### params
* bulk_body(required, type: list): Lista com o payload a enviar

Exemplo:
```py
from elasticsearch_nameko import ElasticSearch

class SomeNamekoService:

    name = 'some_nameko_service'

    # Dependencies
    es = ElasticSearch()


    def some_nameko_endpoint(self):

        index_data = [{'field_value': 1},
                      {'field_value': 2},
                      {'field_value': 3}
                    ]

        es.bulk_post(index_data)

```
