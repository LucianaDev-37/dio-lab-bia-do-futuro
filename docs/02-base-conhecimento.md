# Base de Conhecimento

## Estrutura Atual dos Dados

O agente **LucyAcessível IA** utiliza uma base de conhecimento **simples, controlada e determinística**, implementada diretamente no código da aplicação por meio de **regras baseadas em palavras-chave**, sem uso de modelos generativos.

A lógica do agente é construída em uma função Python que analisa a pergunta do usuário e retorna respostas previamente definidas, garantindo total controle sobre o comportamento do sistema.

Essa abordagem foi escolhida para:

- Garantir previsibilidade das respostas  
- Evitar alucinações  
- Facilitar auditoria e explicação técnica  
- Manter o projeto leve e acessível  
- Tornar o funcionamento compreensível para iniciantes  

📌 **Não são utilizados arquivos externos (JSON, CSV ou banco de dados) nesta versão do protótipo.**  
📌 **Não há integração com APIs de IA generativa.**

---

## Modelo de Funcionamento

A base de conhecimento é acessada por meio de um **motor de regras**, que verifica se determinadas palavras-chave estão presentes na pergunta do usuário.

Cada conjunto de palavras-chave está associado a uma resposta educativa e acessível sobre produtos financeiros básicos.

---

## Conteúdo da Base de Conhecimento

Atualmente, o agente é capaz de responder perguntas relacionadas aos seguintes temas:

- Conta corrente / conta bancária  
- Poupança / economia de dinheiro  
- Cartão de crédito / limite  
- Empréstimos e financiamentos  

As respostas são formuladas em linguagem simples, com foco educativo e acessível.

---

## Exemplo de Implementação no Código

```python
def responder(pergunta):
    pergunta = pergunta.lower()

    if any(p in pergunta for p in ["conta corrente", "conta bancária", "conta do banco"]):
        return (
            "A conta corrente é uma conta bancária usada para receber dinheiro, "
            "pagar contas e fazer transferências. É indicada para o uso diário."
        )

    if any(p in pergunta for p in ["poupança", "guardar dinheiro", "economizar"]):
        return (
            "A poupança é uma forma simples de guardar dinheiro. "
            "Ela rende um pouco e é indicada para reservas financeiras."
        )

    if any(p in pergunta for p in ["cartão", "cartão de crédito", "limite"]):
        return (
            "O cartão de crédito permite fazer compras agora e pagar depois. "
            "É importante usar com cuidado para evitar dívidas."
        )

    if any(p in pergunta for p in ["empréstimo", "financiamento"]):
        return (
            "Um empréstimo é quando o banco empresta dinheiro "
            "e você devolve em parcelas. Posso explicar os tipos básicos se quiser."
        )

    return (
        "Ainda não tenho informações sobre isso. "
        "Posso ajudar com conta corrente, poupança, cartão de crédito ou empréstimo."
    )

## Limitações Atuais

O agente **LucyAcessível IA** possui limitações intencionais, definidas de acordo com o escopo educacional do protótipo:

- Responde apenas a temas previamente definidos  
- Não interpreta contexto complexo ou perguntas ambíguas  
- Não aprende com novas interações  
- Não acessa dados externos, APIs ou bases de dados  

Essas limitações garantem previsibilidade, segurança e facilidade de auditoria do comportamento do agente.

---

## Possíveis Evoluções Futuras

Em versões futuras, o projeto pode ser expandido de forma gradual e controlada, incluindo:

- Externalização da base de conhecimento em arquivos JSON  
- Inclusão de novos produtos e conceitos financeiros  
- Integração opcional com IA generativa de forma supervisionada  
- Expansão do vocabulário de palavras-chave e sinônimos  
- Modularização do código para melhor manutenção  

---

📌 **Observação Final**

A base de conhecimento do agente foi projetada com foco em **clareza, segurança e acessibilidade**, sendo adequada para:

- Demonstrações acadêmicas  
- Projetos educacionais  
- Avaliação técnica inicial por professores ou recrutadores  


