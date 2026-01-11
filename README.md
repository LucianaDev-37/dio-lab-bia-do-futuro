# 🤖 LucyAcessível IA — Agente Financeiro Inclusivo Baseado em Regras

## 📌 Visão Geral

**LucyAcessível IA** é um assistente financeiro educativo, desenvolvido como um **protótipo funcional**, com foco em:

- acessibilidade
- clareza na comunicação
- segurança das respostas
- ausência de alucinações

O agente responde dúvidas básicas sobre **produtos financeiros**, utilizando um **motor de regras baseado em palavras-chave**, garantindo respostas **determinísticas e auditáveis**.

---

## 🎯 Objetivo do Projeto

Criar um chatbot simples e funcional, capaz de:

- explicar conceitos financeiros básicos
- atender usuários iniciantes
- evitar respostas especulativas ou inseguras
- demonstrar, na prática, o uso de **IA baseada em regras** no contexto financeiro

📌 **Importante:** Este projeto **não utiliza IA generativa**.

---

## 🧠 O que o agente faz hoje

- ✅ Chat interativo via **Streamlit**
- ✅ Responde perguntas sobre:
  - conta bancária
  - poupança
  - cartão de crédito
- ✅ Trata perguntas fora do escopo com mensagem segura
- ✅ Interface simples e acessível

---

## 🚀 Aplicação Funcional

A aplicação foi desenvolvida com:

- Python
- Streamlit
- Motor de regras por palavras-chave
- Código concentrado em um único arquivo (`app.py`)

📁 **Código:** `src/app.py`

---

## ▶️ Como Rodar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/LucianaDev-37/LucyAcessivel-IA


```

---

### 2️⃣ Instale as dependências

pip install -r src/requirements.txt

---

### 3️⃣ Execute a aplicação

---

A aplicação será aberta automaticamente no navegador.

---

### 📸 Demonstração da Aplicação

Imagens da aplicação em funcionamento estão disponíveis na pasta `assets`:

- Tela inicial do chatbot
- Exemplos de perguntas válidas
- Tratamento de perguntas fora do escopo

Esses registros comprovam o funcionamento do protótipo.

---

### 📂 Estrutura do Repositório

```text
lucyacessivel-ia/
├── README.md
├── src/
│   ├── app.py
│   └── requirements.txt
├── assets/
│   └── imagens/
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
└── data/
    └── README.md
```

---

### 🔐 Segurança e Confiabilidade

- Não há uso de LLMs
- Não há geração de texto livre
- Todas as respostas são previamente definidas
- Perguntas fora do escopo recebem respostas neutras e seguras

Isso garante:

- previsibilidade
- controle
- ausência de alucinações

---
