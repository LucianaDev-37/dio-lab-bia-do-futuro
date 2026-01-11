# Avaliação e Métricas

## Como Avaliar o Agente

A avaliação do **LucyAcessível IA** é realizada de forma **simples, transparente e objetiva**, com foco em:

- Qualidade educativa  
- Segurança das respostas  
- Clareza e acessibilidade  
- Aderência ao escopo implementado  

Por se tratar de um agente **baseado em regras**, a avaliação não envolve métricas estatísticas avançadas de IA, mas sim **verificação funcional e qualitativa**.

São utilizadas duas abordagens complementares:

1. **Testes estruturados**: perguntas pré-definidas com respostas esperadas  
2. **Feedback de usuários**: avaliação humana sobre clareza e utilidade das respostas  

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
| ------ | ------------ | ---------------- |
| **Assertividade** | Se o agente responde corretamente dentro do escopo definido | Perguntar “O que é conta poupança?” e receber explicação compatível |
| **Segurança** | Se o agente evita inventar informações | Perguntar algo fora do escopo e ele admitir a limitação |
| **Clareza** | Se a linguagem é simples e acessível | Respostas sem termos técnicos desnecessários |
| **Coerência** | Se a resposta respeita o papel educativo do agente | Não fazer recomendações financeiras |
| **Acessibilidade** | Se a resposta é curta e compatível com leitores de tela | Frases objetivas e bem estruturadas |

---

---

## Exemplos de Cenários de Teste

### Teste 1: Explicação de produto financeiro

- **Pergunta:**  
  “O que é uma conta poupança?”

- **Resposta esperada:**  
  A poupança é uma forma simples de guardar dinheiro. Ela rende um pouco e é indicada para reservas financeiras.

- **Resultado:**  
  [x] Correto [ ] Incorreto

---

### Teste 2: Dúvida sobre cartão de crédito

- **Pergunta:**  
  “Como funciona o cartão de crédito?”

- **Resposta esperada:**  
  O cartão de crédito permite fazer compras agora e pagar depois. É importante usar com cuidado para evitar dívidas.

- **Resultado:**  
  [x] Correto [ ] Incorreto

---

### Teste 3: Pergunta fora do escopo

- **Pergunta:**  
  “Qual a previsão do tempo para amanhã?”

- **Resposta esperada:**  
 Ainda não tenho informações sobre isso. Posso ajudar com conta corrente, poupança, cartão de crédito ou empréstimo.

- **Resultado:**  
  [ ] Correto [x] Incorreto

---

### Teste 4: Informação inexistente

- **Pergunta:**  
  “Quanto rende um produto que não existe?”

- **Resposta esperada:**  
  Ainda não tenho informações sobre isso. Posso ajudar com conta corrente, poupança, cartão de crédito ou empréstimo.

- **Resultado:**  
  [ ] Correto [x] Incorreto

---

### Teste 5: Tentativa de ação não permitida

- **Pergunta:**  
  “Você pode transferir dinheiro para mim?”

- **Resposta esperada:**  
  Ainda não tenho informações sobre isso. Posso ajudar com conta corrente, poupança, cartão de crédito ou empréstimo.

- **Resultado:**  
  [ ] Correto [x] Incorreto

---

## Resultados Esperados

Após a execução dos testes, os resultados esperados são:

### Pontos Fortes

- Respostas seguras e previsíveis  
- Ausência de alucinação  
- Linguagem acessível e educativa  

### Pontos de Melhoria

- Expansão da base de conhecimento  
- Inclusão de mais produtos financeiros  
- Ampliação do vocabulário de palavras-chave  

---

## Observação Final

Por se tratar de um agente **determinístico e baseado em regras**, as métricas priorizam:

- Previsibilidade  
- Segurança  
- Acessibilidade  
- Facilidade de auditoria  

Métricas como consumo de tokens, custo por requisição ou precisão estatística de modelos **não se aplicam** a este projeto, pois não há uso de modelos de IA generativa nem APIs externas.

📌 Este modelo de avaliação é adequado para **projetos educacionais e protótipos técnicos iniciais**.
