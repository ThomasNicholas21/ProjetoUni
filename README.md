# 📚 Sistema de Reserva de Salas - FTT

## 💡 Descrição do Projeto
Este é um sistema web desenvolvido com Django para gerenciar a reserva de salas em um ambiente educacional. O sistema oferece APIs para o cadastro de blocos, salas, recursos das salas, cursos e reservas, garantindo que cada reserva siga regras bem definidas.

### 💻 Tecnologias Utilizadas
- **Backend:** Django (Python)
- **Banco de Dados:** PostgreSQL
- **Docker:** Para ambiente conteinerizado
- **Testes:** Django TestCase
- **Log System:** Simulação de logs personalizados na pasta `logs`

## 🏗 Estrutura do Projeto
- **`app/`**: Contém o código-fonte do projeto Django
- **`database/`**: Scripts e arquivos de inicialização do banco de dados
- **`logs/`**: Pasta para simulação de logs personalizados
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

2. **Build e up dos containers**
   ```bash
   cd database/
   docker-compose up --build
   ```

3. **Criar migrações e superusuário**
   ```bash
   cd app/
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

4. **Acessar a aplicação**
   - O servidor estará rodando em `http://localhost:8000`

---

## 📌 Testes
Para rodar os testes automatizados da API:
```bash
cd app/
python manage.py test
```

## 📝 Logs

Os logs personalizados estão armazenados na pasta logs/, onde são geradas informações de execução do sistema.

## 📂 Documentação
A documentação da API estará disponível no repositório em breve.

- **Endpoints da API**: [Em breve]
- **Requisitos Funcionais**: [Em breve]
- **Requisitos do Sistema**: [Em breve]


## 🚀 Conventional Commits
Segue a tabela com os principais tipos de commits utilizados neste projeto:

| Tipo | Descrição |
|------|-----------|
| `feat` | Adição de nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Alteração na documentação |
| `style` | Ajustes de formatação (espaços, indentação) |
| `refactor` | Refatoração de código sem alteração de funcionalidade |
| `test` | Adição ou modificação de testes |
| `chore` | Tarefas de manutenção (build, dependências) |

---


### 🚀 Feito por Thomas
