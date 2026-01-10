# Código da Aplicação

Esta pasta contém o código da aplicação **LucyAcessível IA**, um chatbot financeiro educativo baseado em regras.

A implementação foi mantida **simples e funcional**, conforme o objetivo do projeto, concentrando a lógica em um único arquivo.

---

## Estrutura Atual

src/
├── app.py # Aplicação Streamlit com motor de regras simples
└── requirements.txt #  Dependências do projeto (streamlit)

---

## Tecnologias Utilizadas

- Python
- Streamlit
- Motor de regras baseado em palavras-chave

📌 O projeto **não utiliza IA generativa**.

---

## Como Rodar a Aplicação

### 1️⃣ Instalar dependências

```bash
pip install -r requirements.txt
streamlit run src/app.py
```

 A aplicação será aberta automaticamente no navegador.

## Observações

- As respostas do agente são pré-definidas, garantindo segurança e previsibilidade.
- Perguntas fora do escopo recebem respostas neutras e controladas.
- A estrutura pode ser expandida futuramente para múltiplos arquivos, se necessário.
