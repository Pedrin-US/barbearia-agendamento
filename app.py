import streamlit as st
from datetime import datetime, date

# --- Configurações da Página ---
st.set_page_config(page_title="Agendamento Barbearia", page_icon="✂️")

st.title("✂️ Bigode Barber")
st.subheader("Agende seu horário com facilidade")

# --- Dados da Barbearia (Edite aqui) ---
SEU_NUMERO_WHATSAPP = "5571984290236" # Coloque seu número com DDD (ex: 55 + DDD + Numero)
HORARIOS = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30","09:00", "09:30", "10:00", "10:30", "11:00", "11:30","12:00", "12:30", "13:00", "13:30", "14:00", "14:30","15:00", "15:30", "16:00", "16:30", "17:00", "17:30","18:00", "18:30", "19:00", "19:30", "20:00", "20:30","21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
SERVICOS = ["BARBA R$15", "CABELO R$25", "BARBA+CABELO R$35", "NEVOU R$100", "LUZES R$80", "PEZINHO R$10", "PIGMENTAÇÃO R$10"]

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

