import streamlit as st
from engine import call_openrouter

st.set_page_config(page_title="AI Master OoG", layout="wide")

# Inicializa o histórico na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 AI Master OoG")

# Seleção de Agentes na barra lateral
modo = st.sidebar.selectbox(
    "Selecione o Agente:",
    ("Ask", "Plan", "Agent", "Study")
)

# Prompts de sistema atualizados para cada especialidade
system_prompts = {
    "Ask": "Você é um desenvolvedor Sênior. Responda de forma técnica e concisa.",
    "Plan": "Atue como Arquiteto de Software. Estruture o projeto com pastas, DB e API.",
    "Agent": "Você é um Agente de Execução. Forneça código pronto para uso ou passos detalhados.",
    "Study": "Você é um Professor e Pesquisador. Explique de forma didática e profunda."
}

# Exibição do chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Como posso ajudar?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # SINCRONIZAÇÃO: O contexto enviado contém o System Prompt atual + Histórico completo
    contexto = [{"role": "system", "content": system_prompts[modo]}] + st.session_state.messages

    with st.chat_message("assistant"):
        # Chamada com o histórico completo para manter o raciocínio contínuo
        response = st.write_stream(call_openrouter(contexto))
        #st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
