# 🫀 Cardiocare – Previsão de Doença Cardiovascular

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cardiocare-puc.streamlit.app/)

Este projeto utiliza algoritmos de aprendizado de máquina para prever o risco de doenças cardiovasculares com base em características clínicas e comportamentais.

---

## 🚀 Demonstração ao vivo

Acesse a aplicação em:  
👉 **https://cardiocare-puc.streamlit.app**

---

## 🧠 Modelos utilizados

- 🔹 Regressão Logística
- 🔹 Random Forest
- 🔹 SVM (Support Vector Machine)

Todos os modelos foram treinados e salvos como arquivos `.pkl`, armazenados com **Git LFS** neste repositório.

---

## 📁 Estrutura do Projeto

```
cardiocare/
├── modelos/
│   ├── modelo_regressao_logistica.pkl
│   ├── modelo_random_forest.pkl
│   ├── modelo_svm.pkl
│   └── escalador.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## 💻 Como executar localmente

1. Clone o repositório:

```bash
git clone https://github.com/rodrigodel/cardiocare.git
cd cardiocare
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o app:

```bash
streamlit run app.py
```

> ⚠️ Certifique-se de ter o **Git LFS** instalado para baixar os modelos `.pkl`.

---

## ⚙️ Requisitos

- Python 3.8+
- Git LFS configurado
- Bibliotecas Python:

```txt
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## 🤝 Contribuições

Contribuições são muito bem-vindas!  
Sinta-se à vontade para abrir **issues** ou enviar **pull requests** com sugestões, correções ou melhorias.

---

## 👨‍💻 Autor

**Rodrigo Zambon**  
🔗 https://rodrigozambon.com.br  
📧 contato@rodrigozambon.com.br
