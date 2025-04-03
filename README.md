# 📚 Sistema de Reserva de Salas - FTT

## 💡 Descrição do Projeto
Este sistema web, desenvolvido com Django e Django REST Framework, gerencia a reserva de salas em um ambiente educacional com APIs bem definidas para blocos, salas, recursos, cursos e reservas. Utiliza PostgreSQL em um container Docker para escalabilidade e eficiência. A API segue o padrão RESTful, com serializers para manipulação de dados e documentação acessível via Markdown e Postman. Conta com testes automatizados, logs e autenticação JWT para garantir confiabilidade, segurança, auditoria e prevenção de falhas. 🚀

## 🎯 Funcionalidades
- Cadastro de Blocos, Salas, Recursos da Sala, Usuários, e Reservas.
- Gerenciamento de Reservas.
- Regras de Compartilhamento.
- Controle de Conflitos.
- Notificações e Relatórios.

## 📂 Documentação
A documentação da API estará disponível no repositório em breve.

- **Requisitos Funcionais e o que foi implementado**: 👉 [DOCS - REQUISITOS](https://github.com/ThomasNicholas21/ProjetoUni/blob/master/docs/requisitos.md)
- **Endpoints da API**: 👉 [DOCS - ENDPOINTS](https://github.com/ThomasNicholas21/ProjetoUni/blob/master/docs/endpoints.md)
- **Download arquivo Json para Postman**: 👉 [POSTMAN](https://github.com/ThomasNicholas21/ProjetoUni/raw/master/docs/Unievangelica%20API.postman_collection.json)

### 💻 Tecnologias Utilizadas
- **Backend:** Django (Python)
- **Banco de Dados:** PostgreSQL
- **Docker:** Para ambiente conteinerizado
- **Testes:** Django TestCase
- **Log System:** Simulação de logs personalizados na pasta `logs`

## 🏗 Estrutura do Projeto
- **`app/`**: Contém o código-fonte do projeto Django
- **`database/`**: Arquivo docker-compose para inicialização do banco de dados
- **`docs/`**: Documentação da API, requisitos funcionais e do sistema
- **`env_file/.env_example`**: Arquivo modelo para configuração do ambiente

---

## 🙋‍♂️ Como Rodar o Projeto

### Sem Docker
1. **Configurar o ambiente**
   - Copie o arquivo `env_example` e renomeie para `.env`
   - Preencha as informações necessárias para conectar ao banco PostgreSQL e o ative.

2. **Criar ambiente virtual e instalar dependências**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Inicializar o banco de dados e rodar a aplicação**
   ```bash
   cd app/
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

### Com Docker
1. **Configurar o ambiente**
   - Copie `env_example` para `.env`
     
  
2. **Criar ambiente virtual e instalar dependências**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Build e up dos containers**
   ```bash
   cd database/
   docker-compose up --build
   ```

4. **Criar migrações e superusuário**
   ```bash
   cd app/
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

5. **Acessar a aplicação**
   - O servidor estará rodando em `http://localhost:8000`

---

## 📌 Testes
Para rodar os testes automatizados da API:
```bash
cd app/
python manage.py test
```

## 📝 Logs

Os logs personalizados estão armazenados na pasta logs/, onde são geradas informações de execução do sistema. Para simular utilize o seguinte comando:
```bash
cd app/
python manage.py simular_notificacoes
```


## 🚀 Conventional Commits
Segue a tabela com os principais tipos de commits utilizados neste projeto:

| Tipo | Descrição |
|------|-----------|
| `feat` | Adição de nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Alteração na documentação |
| `style` | Implementação e justes de estilização |
| `refactor` | Refatoração de código sem alteração de funcionalidade |
| `test` | Adição ou modificação de testes |
| `chore` | Tarefas de manutenção (build, dependências) |

---


### 🚀 Feito por Thomas
