# Projeto Data Engineering - ETL com Firebird e Airflow

Projeto de estudos para construir um pipeline ETL usando um banco legado Firebird (`.FB5`), Python com SQLAlchemy e Apache Airflow para orquestracao.

## Objetivo

Extrair dados de vendas do Firebird, tratar essas informacoes e disponibilizar os dados em uma estrutura adequada para analise.

Os campos de interesse para a evolucao da query sao:

- nome do aluno
- nome responsavel
- valor da venda
- produtos vendidos
- descontos
- forma de pagamento
- data pagamento

## Estrutura

- `dags/`: DAGs do Apache Airflow.
- `db/`: conexao com o banco Firebird.
- `src/extract/`: camada de extracao.
- `src/transform/`: camada de transformacao.
- `src/load/`: camada de carga.
- `dataset/`: banco local Firebird, fora do Git.

## Como configurar

1. Copie `.env.example` para `.env`.
2. Ajuste o caminho do `fbclient.dll`, se necessario.
3. Ajuste `FIREBIRD_DATABASE` se o banco estiver em outro caminho.
4. Suba o Airflow com Docker Compose.

```powershell
docker compose up -d
```

## Status atual

- Ambiente com Docker e Airflow configurado.
- Conexao com Firebird organizada em `db/conexao_db.py`.
- Extracao inicial criada em `src/extract/extract.py`.
- DAG `pipeline_vendas` preparada para orquestrar extract, transform e load.

## Proximos passos

- Mapear as tabelas de vendas no Firebird.
- Criar a query principal com joins e agregacoes.
- Implementar a transformacao dos dados.
- Carregar o resultado em um banco analitico, provavelmente PostgreSQL.
- Evoluir para carga incremental, logs e dashboards.

## Observacao

O banco `.FB5`, logs, `.env` e arquivos de configuracao local ficam fora do Git para evitar subir arquivos grandes ou configuracoes da maquina.
