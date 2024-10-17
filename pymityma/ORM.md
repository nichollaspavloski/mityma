#### EXPLICAÇÃO DATABASE FIRST

1. para gerar as classes a partir do banco de dados, foi necessário a instalação de um pacote (sqlacodegen)
2. o seguinte comando cria o arquivo py com as classes do banco de dados
```
sqlacodegen postgresql+psycopg2://username:password@localhost/mityma --outfile sqlamodels.py
```


#### EXPLICAÇÃO CODEFIRST

1. a aplicação foi desenvolvida desde o início utilizando o ORM SQLAlchemy, então as classes foram criadas manualmente para criação das tabelas do banco de dados (./api/model/models.py)
2. para consulta/persistência dos dados, é utilizado o método `session.add` (commands.py:20) em que se passa uma instância da classe modelo como parâmetro para inserir/atualizar o registro no banco de dados

