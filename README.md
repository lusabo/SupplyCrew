# 🤖 SuppleCrew — Automação Inteligente de Compras Industriais

> O poder dos agentes inteligentes para revolucionar o seu processo de compras.  
> _“Menos cliques. Mais inteligência. Zero retrabalho.”_

---

## 🚀 Visão Geral

**SuppleCrew** é uma plataforma de automação de compras industriais baseada em **CrewAI** e o padrão **MCP (Multi-Agent Collaboration Pattern)**.

Ela transforma processos lentos e manuais de cotação, análise e decisão de compra em uma **orquestra autônoma de agentes inteligentes**, que se comunicam, analisam, decidem e aprendem com cada ciclo de compra.

Ideal para **indústrias médias e grandes**, com operações complexas e exigência de agilidade, rastreabilidade e compliance.

---

## 🧠 Funcionalidades-Chave

- 🧾 Interface simplificada para criação de requisições técnicas  
- 📤 Envio automático de cotações para fornecedores por e-mail estruturado  
- 📥 Leitura e interpretação inteligente de e-mails de resposta  
- 📊 Comparação automática de propostas com critérios configuráveis  
- ✅ Aprovação assistida e geração de ordem de compra  
- 📈 Registro da performance dos fornecedores  
- 🔌 Integração com ERPs como TOTVS via APIs ou conectores diretos  

---

## 🛠️ Tecnologias Utilizadas

| Camada         | Tecnologias                                |
|----------------|---------------------------------------------|
| Backend API    | FastAPI, Pydantic, SQLAlchemy               |
| Inteligência   | CrewAI, MCP Pattern, NLP (spaCy / LLM APIs) |
| E-mails        | SMTP, IMAP, Yagmail, Mailparser             |
| Banco de Dados | PostgreSQL ou SQL Server                    |
| Tarefas        | Celery + Redis (opcional)                   |
| UI (Futura)    | React + Tailwind                            |
| DevOps         | Docker, dotenv, Makefile                    |

---

## 🧬 Estrutura do Projeto

```

supplecrew/
├── app/
│   ├── main.py              # Entrypoint do FastAPI
│   ├── routes/              # Endpoints REST
│   ├── agents/              # Agentes CrewAI (comparador, parser, etc.)
│   ├── services/            # E-mail, ERP, parsing, etc.
│   ├── db/                  # Modelos SQLAlchemy
│   ├── schemas/             # Modelos Pydantic
│   └── core/                # Configurações e utilitários
├── celery\_worker.py         # Worker assíncrono (opcional)
├── .env                     # Variáveis de ambiente
├── requirements.txt
└── README.md

````

---

## 🔧 Como Rodar Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/supplecrew.git
cd supplecrew

# 2. Crie o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # ou .venv\\Scripts\\activate no Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o .env com DB, SMTP, ERP
cp .env.example .env

# 5. Rode a API
uvicorn app.main:app --reload

# 6. Acesse a documentação
http://localhost:8000/docs
````

---

## 🧠 Como Funciona o MCP com Agentes

```
[Usuário] ➡️ [AgentEmail envia cotações]
                   ⬇️
           [AgentParser interpreta respostas]
                   ⬇️
          [AgentComparator define ranking]
                   ⬇️
         [CrewManager propõe decisão final]
                   ⬇️
         [Usuário aprova ou automatiza]
```

---

## 📦 Extensível e Integrável

* 🔌 Pronto para integrar com ERP via REST, banco ou XML
* 🧩 Modular: adicione novos agentes para lógica fiscal, compliance, qualidade, etc.
* 📚 Exporta históricos, scores e análises via API ou planilhas

---

## 👨‍💼 Público-Alvo

* Indústrias com cadeia de suprimentos complexa
* Empresas que usam TOTVS, SAP ou sistemas próprios
* Equipes de compras buscando reduzir retrabalho e acelerar decisões

---

## 📬 Contato

Ficou interessado? Quer integrar ou contribuir? Fale com a gente!

* ✉️ [contato@supplecrew.ai](mailto:contato@supplecrew.ai)
* 🌐 [supplecrew.ai](https://supplecrew.ai) *(em breve)*

---

**SuppleCrew** — *Inteligência artificial para o mundo real das compras industriais.*

