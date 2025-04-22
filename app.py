import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# Criar diretório local de modelos, se necessário
os.makedirs("modelos", exist_ok=True)

# === Carregamento dos modelos locais ===
try:
    model_rf = joblib.load("modelos/modelo_random_forest.pkl")
    model_lr = joblib.load("modelos/modelo_regressao_logistica.pkl")
    model_svm = joblib.load("modelos/modelo_svm.pkl")
    scaler   = joblib.load("modelos/escalador.pkl")
    st.success("✅ Modelos carregados com sucesso!")
except FileNotFoundError as e:
    st.error(f"❌ Erro ao carregar modelos: {e}")

# === Função de predição ===
def prever_diagnostico(dados_input):
    df = pd.DataFrame([dados_input])

    df_encoded = pd.get_dummies(df, columns=['gender', 'cholesterol', 'gluc'], drop_first=True)
    colunas_treinadas = scaler.feature_names_in_
    for col in colunas_treinadas:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[colunas_treinadas]
    dados_normalizados = scaler.transform(df_encoded)

    pred_lr = model_lr.predict(dados_normalizados)[0]
    pred_rf = model_rf.predict(df_encoded)[0]
    pred_svm = model_svm.predict(dados_normalizados)[0]

    return pred_lr, pred_rf, pred_svm

# === Interface Streamlit ===
st.title("🫀 Previsão de Doença Cardiovascular")
st.markdown("Preencha os dados abaixo:")

age = st.number_input("Idade", min_value=0, max_value=120, step=1)
height = st.number_input("Altura (cm)", min_value=100, max_value=250, step=1)
weight = st.number_input("Peso (kg)", min_value=30, max_value=200, step=1)
ap_hi = st.number_input("Pressão Sistólica (ap_hi)", min_value=80, max_value=250)
ap_lo = st.number_input("Pressão Diastólica (ap_lo)", min_value=40, max_value=200)
gender = st.selectbox("Gênero", ['male', 'female'])
cholesterol = st.selectbox("Colesterol", ['normal', 'acima_do_normal', 'muito_alto'])
gluc = st.selectbox("Glicose", ['normal', 'acima_do_normal', 'muito_alto'])
smoke = st.selectbox("Fumante?", [0, 1])
alco = st.selectbox("Consome álcool?", [0, 1])
active = st.selectbox("Fisicamente ativo?", [0, 1])

if st.button("Prever"):
    entrada = {
        'age': age,
        'height': height,
        'weight': weight,
        'ap_hi': ap_hi,
        'ap_lo': ap_lo,
        'gender': gender,
        'cholesterol': cholesterol,
        'gluc': gluc,
        'smoke': smoke,
        'alco': alco,
        'active': active
    }

    lr, rf, svm = prever_diagnostico(entrada)

    st.subheader("Resultado da Predição:")
    st.write(f"**Regressão Logística:** {'Doente' if lr else 'Saudável'}")
    st.write(f"**Random Forest:** {'Doente' if rf else 'Saudável'}")
    st.write(f"**SVM:** {'Doente' if svm else 'Saudável'}")
