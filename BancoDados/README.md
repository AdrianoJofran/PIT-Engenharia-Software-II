Banco de Dados do Sistema de Controle de Manutenção Industrial

Tabela: Maquina

- id
- nome
- fabricante
- setor

Tabela: Tecnico

- id
- nome
- especialidade

Tabela: Manutencao

- id
- maquina_id
- tecnico_id
- data
- descricao
- status

Relacionamentos

- Uma máquina pode possuir várias manutenções.
- Um técnico pode realizar várias manutenções.
- Cada manutenção está vinculada a uma máquina e a um técnico.
`
