# 🫀 Cardiocare – Previsão de Doença Cardiovascular

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cardiocare-puc.streamlit.app/)

Este projeto utiliza algoritmos de aprendizado de máquina para prever o risco de doenças cardiovasculares com base em características clínicas e comportamentais.

---

## 🚀 Demonstração ao vivo

Acesse a aplicação em:
👉 **[https://cardiocare-puc.streamlit.app](https://cardiocare-puc.streamlit.app)**

---

## 🧠 Modelos utilizados

- 🔹 Regressão Logística
- 🔹 Random Forest
- 🔹 SVM (Support Vector Machine)

Todos os modelos foram treinados e salvos como arquivos `.pkl` e armazenados com **Git LFS**.

---

## 📁 Estrutura do Projeto
```
cardiocare/ ├── modelos/ │ ├── modelo_regressao_logistica.pkl │ ├── modelo_random_forest.pkl │ ├── modelo_svm.pkl │ └── escalador.pkl ├── app.py ├── requirements.txt └── README.md
```

---

## 💻 Como executar localmente

1. Clone o repositório:

```bash
git clone https://github.com/rodrigodel/cardiocare.git
cd cardiocare
pip install -r requirements.txt
streamlit run app.py
