# Documentação de Endpoints

## 1. Cadastro de Blocos e Salas

### Endpoint: Criar um Bloco
**Método:** POST  
**Rota:** `/blocos/`  
**Descrição:** Cria um novo bloco com nome e identificação.  
**Restrições:**  
- O nome do bloco deve ser único.
- Identificação deve seguir um formato padrão predefinido.

---

### Endpoint: Criar uma Sala
**Método:** POST  
**Rota:** `/salas/`  
**Descrição:** Cria uma sala associada a um bloco, informando capacidade e recursos disponíveis.  
**Restrições:**  
- A sala deve estar vinculada a um bloco existente.
- A capacidade da sala deve ser um número positivo.

## 2. Gerenciamento de Reservas

### Endpoint: Criar uma Reserva
**Método:** POST  
**Rota:** `/reservas/`  
**Descrição:** Reserva uma sala, especificando bloco, número da sala, data e horário, nome do coordenador e motivo.  
**Restrições:**  
- A sala deve estar disponível no horário especificado.
- O nome do coordenador deve ser informado.
- O horário de término deve ser posterior ao horário de início.

---

### Endpoint: Verificar Disponibilidade de uma Sala
**Método:** GET  
**Rota:** `/salas/{sala_id}/disponibilidade/`  
**Descrição:** Retorna a disponibilidade da sala para um período específico.  
**Restrições:**  
- Deve ser informada uma data e um intervalo de tempo válido.

---

### Endpoint: Cancelar uma Reserva
**Método:** DELETE  
**Rota:** `/reservas/{reserva_id}/`  
**Descrição:** Cancela uma reserva existente.  
**Restrições:**  
- Somente o coordenador que fez a reserva pode cancelá-la.
- Cancelamentos só podem ser feitos antes do horário de início da reserva.

## 3. Regra de Compartilhamento de Espaços

### Endpoint: Listar Salas Disponíveis para Outros Cursos
**Método:** GET  
**Rota:** `/salas/disponiveis/`  
**Descrição:** Retorna a lista de salas livres que podem ser reservadas por outros cursos.  
**Restrições:**  
- Algumas salas podem ser exclusivas para determinados cursos.

## 4. Conflitos de Agendamento

### Endpoint: Criar Reserva Recorrente
**Método:** POST  
**Rota:** `/reservas/recorrente/`  
**Descrição:** Permite a reserva recorrente de uma sala (exemplo: toda segunda-feira das 8h às 10h por um semestre).  
**Restrições:**  
- Não deve haver conflitos de horário.
- Deve ser especificada a recorrência (semanal, mensal etc.).

## 5. Notificações e Relatórios

### Endpoint: Enviar Notificação de Reserva
**Método:** POST  
**Rota:** `/notificacoes/`  
**Descrição:** Simula o envio de notificações sobre reservas futuras.  
**Restrições:**  
- Apenas coordenadores podem receber notificações.

---

### Endpoint: Gerar Relatório de Uso de Salas
**Método:** GET  
**Rota:** `/relatorios/uso-salas/`  
**Descrição:** Gera um relatório com estatísticas de uso das salas, como horários de pico e taxa de ocupação.  
**Restrições:**  
- Apenas usuários autorizados podem acessar relatórios.

---

# Funcionalidades Bônus

## 1. Autenticação e Segurança

### Endpoint: Autenticação de Coordenadores (JWT)
**Método:** POST  
**Rota:** `/auth/login/`  
**Descrição:** Realiza a autenticação do coordenador e retorna um token JWT.  
**Restrições:**  
- O usuário deve estar cadastrado previamente.

---

### Endpoint: Registro de Coordenador
**Método:** POST  
**Rota:** `/auth/register/`  
**Descrição:** Registra um novo coordenador no sistema.  
**Restrições:**  
- Apenas administradores podem cadastrar novos coordenadores.

## 2. Testes Automatizados

- Testes unitários devem garantir a funcionalidade correta dos endpoints.
- Testes de integração para validar o fluxo completo do sistema.

