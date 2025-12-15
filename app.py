import streamlit as st
from datetime import datetime, date

# --- Configurações da Página ---
st.set_page_config(page_title="Agendamento Barbearia", page_icon="✂️")

st.title("✂️ Barbearia do Mestre")
st.subheader("Agende seu horário com facilidade")

# --- Dados da Barbearia (Edite aqui) ---
SEU_NUMERO_WHATSAPP = "5511999999999" # Coloque seu número com DDD (ex: 55 + DDD + Numero)
HORARIOS = ["09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
SERVICOS = ["Corte de Cabelo", "Barba", "Cabelo + Barba (Completo)", "Pezinho/Sobrancelha"]

# --- Formulário de Agendamento ---
with st.container():
    st.write("---")
    nome_cliente = st.text_input("Seu Nome:")
    
    col1, col2 = st.columns(2)
    with col1:
        data_agendamento = st.date_input("Escolha a Data", min_value=date.today())
    with col2:
        horario_escolhido = st.selectbox("Escolha o Horário", HORARIOS)
        
    servico_escolhido = st.selectbox("Qual serviço deseja?", SERVICOS)

    # Formatar a data para o padrão brasileiro
    data_formatada = data_agendamento.strftime("%d/%m/%Y")

    # --- Lógica do Botão ---
    st.write("---")
    st.info("Ao clicar em 'Agendar', você será redirecionado para o WhatsApp para confirmar o pedido.")

    # Criação da mensagem do WhatsApp
    msg = f"Olá! Gostaria de agendar um horário.%0A%0A*Nome:* {nome_cliente}%0A*Data:* {data_formatada}%0A*Horário:* {horario_escolhido}%0A*Serviço:* {servico_escolhido}"
    
    link_whatsapp = f"https://wa.me/{SEU_NUMERO_WHATSAPP}?text={msg}"

    # Validação simples para não enviar vazio
    if nome_cliente:
        st.link_button("✅ Agendar no WhatsApp", link_whatsapp)
    else:
        st.warning("Por favor, preencha seu nome para liberar o botão de agendamento.")