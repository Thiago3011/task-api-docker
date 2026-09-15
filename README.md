# Task API — Multiambiente com Docker

API REST desenvolvida com FastAPI como laboratório prático de Docker,
ambientes e integração com PostgreSQL.

## Objetivo

O projeto foi desenvolvido para entender, na prática, como uma aplicação
Backend funciona em diferentes ambientes e como seus serviços se comunicam
dentro de uma infraestrutura containerizada.

## Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Pydantic
- psycopg

## Arquitetura

```text
              ┌──────────────┐
              │   Task API   │
              │   FastAPI    │
              └──────┬───────┘
                     │
               Docker Network
                     │
              ┌──────▼───────┐
              │  PostgreSQL  │
              └──────────────┘
```

## Conceitos praticados

- Containerização de aplicações
- Docker Compose
- Variáveis de ambiente
- Ambientes Development, Staging e Production
- Volumes para persistência
- Comunicação entre containers
- PostgreSQL em container
- Healthcheck
- Controle da ordem de inicialização dos serviços
- Configuração externa por ambiente

## Como executar

### Development

```bash
docker compose --env-file .env.development up -d
```

A API ficará disponível em:

```text
http://localhost:8000
```

Documentação Swagger:

```text
http://localhost:8000/docs
```

### Encerrar os serviços

```bash
docker compose --env-file .env.development down
```

## Banco de dados

O PostgreSQL não é exposto diretamente para o host.

A API se conecta ao banco pela rede interna do Docker Compose usando o
nome do serviço:

```text
postgres:5432
```

O banco utiliza um volume Docker para persistência dos dados.

## Estrutura de ambientes

O projeto utiliza arquivos de ambiente diferentes para manter o mesmo
código da aplicação com configurações distintas:

```text
.env.development
.env.staging
.env.production
```

## Observações

Este projeto foi desenvolvido como laboratório de aprendizado em Docker,
PostgreSQL, ambientes e comunicação entre serviços.

A proposta não é transformar a Task API em um sistema grande, mas usar sua
evolução para consolidar conceitos de infraestrutura aplicados a uma API
Backend.

## Próximos passos

Novas evoluções de Backend, regras de negócio e arquitetura serão exploradas
em projetos específicos de portfólio.
