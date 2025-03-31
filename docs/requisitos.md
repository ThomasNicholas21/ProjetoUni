# Sistema de Gerenciamento de Reservas de Salas Acadêmicas

# Finalidade do Projeto

A UniEVANGÉLICA necessita de um sistema eficiente para o gerenciamento de reservas de salas acadêmicas, permitindo que coordenadores de curso possam visualizar e reservar espaços de maneira organizada e automatizada. O objetivo principal desta API é oferecer um meio confiável para o controle de reservas, garantindo a disponibilidade e evitando conflitos de agendamento, além de fornecer relatórios e notificações para otimizar o uso das salas.

# Requisitos Técnicos

## Tecnologias Utilizadas
Para o desenvolvimento deste sistema, adotaremos as seguintes tecnologias:

### Backend:
- **Linguagem:** Python
- **Framework:** Django
- **Django REST Framework (DRF):** Para a construção da API RESTful

### Banco de Dados:
- **PostgreSQL:** Utilizado como banco de dados relacional
- **Docker:** Para facilitar o gerenciamento do PostgreSQL

## Justificativa para o Uso de Docker com PostgreSQL
Facilidade de Configuração, Isolamento, Portabilidade, Gerenciamento Simplificado e Escalabilidade.

## Requisitos Funcionais

### 1. Cadastro de Blocos e Salas
- **Cadastro de Blocos**: O sistema deve permitir o cadastro de blocos acadêmicos contendo nome e identificação única.
- **Cadastro de Salas**: Cada sala deve estar associada a um bloco, possuir uma capacidade máxima de alunos e uma lista de recursos disponíveis (projetor, quadro digital, ar-condicionado, etc.).

### 2. Gerenciamento de Reservas
- **Criar Reserva**:
  - A reserva deve conter:
    - Bloco e número da sala
    - Data e horário de início e término
    - Nome do coordenador que realizou a reserva
    - Motivo da reserva
  - O sistema deve verificar a disponibilidade antes de confirmar a reserva.
- **Visualizar Disponibilidade**:
  - O usuário deve poder consultar a disponibilidade de uma sala em um período específico.
- **Cancelar Reserva**:
  - Um coordenador deve poder cancelar uma reserva previamente realizada.

### 3. Regra de Compartilhamento de Espaços
- **Reservas por Outros Cursos**: Se uma sala pertencente a um curso estiver livre, outros cursos podem reservá-la.
- **Restrições Específicas**: Algumas salas podem ser restritas a determinados cursos, como laboratórios específicos.

### 4. Conflitos de Agendamento
- **Evitar Duplicidade**: O sistema deve impedir que duas reservas sejam feitas para a mesma sala e horário.
- **Reservas Recorrentes**:
  - Deve ser possível criar reservas recorrentes (exemplo: toda segunda-feira das 8h às 10h por um semestre).
  - O sistema deve tratar conflitos em reservas recorrentes e informar ao usuário.

### 5. Notificações e Relatórios
- **Notificações de Reservas**:
  - O sistema deve simular o envio de notificações (via logs) para alertar sobre reservas futuras.
- **Geração de Relatórios**:
  - O sistema deve fornecer estatísticas sobre:
    - Salas mais reservadas
    - Horários de pico de uso
    - Taxa de ocupação geral

## Observações
O sistema deve garantir que as regras de reserva sejam respeitadas, evitando sobreposições e permitindo um gerenciamento eficiente das salas acadêmicas. Além disso, deve oferecer relatórios detalhados para análise e planejamento futuro.
