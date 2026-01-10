import streamlit as st

st.set_page_config(
    page_title="LucyAcessível IA",
    layout="centered"
)

st.title("🤖 LucyAcessível IA")
st.subheader("Assistente financeiro educativo e acessível")

st.write(
    "Digite sua dúvida sobre produtos financeiros básicos, "
    "como conta corrente, poupança, cartão de crédito ou empréstimo."
)

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

pergunta_usuario = st.text_input("Digite sua pergunta:")

if pergunta_usuario:
    resposta = responder(pergunta_usuario)
    st.success(resposta)
