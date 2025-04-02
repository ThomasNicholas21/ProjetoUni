# 🏢 Sistema de Gerenciamento de Reservas de Salas Acadêmicas

## 📄 Finalidade do Projeto
A UniEVANGÉLICA necessita de um sistema eficiente para o gerenciamento de reservas de salas acadêmicas, permitindo que coordenadores de curso possam visualizar e reservar espaços de maneira organizada e automatizada.

Este sistema tem como principais objetivos:
- ✅ Garantir a disponibilidade de salas.
- ⛔ Evitar conflitos de agendamento.
- 📊 Gerar relatórios e notificações para otimizar o uso das salas.

---

## 👨‍💻 Tecnologias Utilizadas
### ✨ Backend
- **Linguagem:** Python
- **Framework:** Django
- **Django REST Framework (DRF):** Para a construção da API RESTful

### 🏛️ Banco de Dados
- **PostgreSQL:** Banco de dados relacional
- **Docker:** Facilita o gerenciamento do PostgreSQL

### 🛠️ Motivos para Usar Docker
- ✨ **Facilidade de Configuração**
- 🛠️ **Isolamento e Portabilidade**
- 🛢️ **Gerenciamento Simplificado**
- ⚡ **Escalabilidade**

---

## 📈 Requisitos Funcionais e Funcionalidades Implementadas

### ✅ 1. **Cadastro de Blocos e Salas**  
- Registro de blocos físicos (ex.: "Bloco A", "Bloco de Laboratórios").  
- Associação de salas aos blocos, contendo:
  - Capacidade máxima de ocupação.
  - Recursos (projetor, computadores, quadros inteligentes).
  - Restrições de uso (ex.: exclusividade para cursos específicos).  

### ⏰ 2. **Gerenciamento de Reservas**  
- **Reserva de Salas:**
  - Seleção de bloco, sala, data/horário.
  - Registro do coordenador e motivo.
- **Consulta de Disponibilidade:** Verificação em tempo real.
- **Cancelamento de Reservas:** Endpoint dedicado para remoção de agendamentos.

### 🏠 3. **Regras de Compartilhamento**  
- **Salas Compartilháveis:** Salas podem ser utilizadas por outros cursos quando livres.
- **Restrições Específicas:** Algumas salas podem ter acesso exclusivo.

### ⛔ 4. **Controle de Conflitos**  
- **Impedimento de Duplicidade:** Evita reservas conflitantes.
- **Reservas Recorrentes:** Suporte para agendamentos periódicos.

### 📈 5. **Notificações e Relatórios**  
- **Notificações:** Logs simulados alertando sobre reservas futuras.
- **Relatórios Estatísticos:**
  - Salas mais utilizadas.
  - Horários de maior demanda.
  - Taxa de ocupação.

---

## 🌐 Boas Práticas e Arquitetura
### 🔗 API RESTful
- **Endpoints intuitivos** com métodos HTTP adequados (GET, POST, PUT, DELETE).

### 🏦 Banco de Dados
- **Modelagem Relacional:** Tabelas otimizadas para `Blocos`, `Salas`, `Reservas`, `Cursos` e `RecursoSala`.
- **Consultas Eficientes:** Uso de índices para buscas rápidas.

### 🔒 Segurança (Bônus)
- **Autenticação JWT:** Apenas coordenadores autenticados podem acessar.

### ⚖️ Testes (Bônus)
- **Testes Unitários:** Cobertura para regras de negócio (ex.: conflitos de horário).

---

