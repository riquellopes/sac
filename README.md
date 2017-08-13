Documentação
============

O app de sac foi divido em 2 projetos, **SacBackend** onde é feita toda a gestão das informações,
com Flask. E o **SacFrontend** que é uma [spa](https://en.wikipedia.org/wiki/Single-page_application), escrita em [React](https://facebook.github.io/react/). Para orquestrar todos esses serviços eu utilizei [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/).

##### Montando ambiente:

```bash
    make install
```

##### Para levantar os containers:

```bash
    make up # Após basta acessar http://localhost:8080/
```
##### Para acessar um container específico:

```bash
    make olx-backend or
    make olx-frontend
```

#### Para executar os testes:

```bash
    make backend-test or # Executa os testes unitários.
    make backend-test-cov # Verifica o nível de cobertura.
    make front-end-test
```

#### Outros

```bash
    make migrate # Cria uma nova migração
    make upgrade # Utilizado para criar o banco, e definir informações iniciais.
```
