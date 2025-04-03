# 📌 Documentação da API - Sistema de Reservas de Salas

## 🔹 Introdução
Esta API permite a gestão de reservas de salas dentro da UniEVANGÉLICA, incluindo o cadastro e consulta de usuários, blocos, salas, cursos, recursos e reservas.

---

## 🔹 Endpoints Disponíveis

### 👥 Usuários
- `GET /api/get/usuarios/` → Retorna a lista de usuários cadastrados.
- `POST /api/post/usuario/` → Cria um novo usuário.

### 🏢 Blocos
- `GET /api/get/blocos/` → Lista todos os blocos disponíveis.
- `GET /api/get/bloco/<int:id_bloco>/` → Retorna os detalhes de um bloco específico.
- `POST /api/post/bloco/` → Cria um novo bloco.

### 🛠 Recursos
- `GET /api/get/recursos_sala/` → Lista os recursos disponíveis para salas.
- `GET /api/get/recurso_sala/<int:id_recurso>/` → Retorna detalhes de um recurso específico.
- `POST /api/post/recurso_sala/` → Adiciona um novo recurso para salas.

### 🚪 Salas
- `GET /api/get/salas/` → Lista todas as salas cadastradas.
- `POST /api/post/sala/` → Cadastra uma nova sala.

### 🎓 Cursos
- `GET /api/get/cursos/` → Lista todos os cursos registrados.
- `POST /api/post/curso/` → Cadastra um novo curso.

### 📅 Reservas
- `GET /api/get/reservas/` → Lista todas as reservas realizadas.
- `GET /api/get/reserva/<int:id_reserva>/` → Retorna detalhes de uma reserva específica.
- `POST /api/post/reserva/` → Cria uma nova reserva de sala.
- `DELETE /api/delete/reserva/<int:id_reserva>/` → Cancela uma reserva existente.

### ✅ Disponibilidade de Reserva
- `POST /api/post/reserva/disponibilidade/` → Verifica a disponibilidade de uma sala para reserva.

### 📊 Relatórios
- `GET /api/get/relatorio/` → Retorna relatórios estatísticos sobre as reservas.

---

## 📌 Observações
- Os endpoints `POST` exigem envio de dados no corpo da requisição em formato JSON.
- Os endpoints `DELETE` removem registros do sistema e devem ser usados com cautela.
- Para consultas específicas, utilize os endpoints com `<int:id_*>` para buscar registros individuais.
