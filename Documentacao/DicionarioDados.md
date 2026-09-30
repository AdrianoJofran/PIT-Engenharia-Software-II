# Dicionário de Dados

## Tabela Maquina

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | Integer | Identificador da máquina |
| nome | Varchar | Nome da máquina |
| fabricante | Varchar | Fabricante da máquina |
| setor | Varchar | Setor onde está instalada |

## Tabela Tecnico

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | Integer | Identificador do técnico |
| nome | Varchar | Nome do técnico |
| especialidade | Varchar | Área de atuação |

## Tabela Manutencao

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | Integer | Identificador da manutenção |
| maquina_id | Integer | Máquina relacionada |
| tecnico_id | Integer | Técnico responsável |
| data | Date | Data da manutenção |
| descricao | Text | Descrição do serviço |
| status | Varchar | Situação da manutenção |
