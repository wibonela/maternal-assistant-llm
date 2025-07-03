# maternal-assistant-llm

# Maternal Assistant LLM 🤱🏽🇹🇿

This project presents a Kiswahili Large Language Model (LLM) assistant designed to support breastfeeding mothers in Tanzania — especially those with babies aged 3 to 6 months. The assistant answers health, nutrition, emotional wellbeing, and breastfeeding-related questions using a dataset curated from trusted Swahili sources and WHO/Tanzania MoH guidelines.

## 💡 Features
- Conversational Swahili maternal health support
- Trained on 500+ real-life Q&A pairs from forums, health blogs, and MoH materials
- Hugging Face `t5-small` fine-tuned model
- Deployed on Streamlit Cloud for easy access

## 🚀 Try it Online
The app is hosted on [Streamlit Cloud](https://share.streamlit.io/) and accessible from any device with internet access.

## 🛠 Technologies Used
- Hugging Face Transformers
- T5 Model (`t5-small`)
- Google Colab (for training)
- Streamlit (for deployment)
- GitHub (for app hosting)

## 🧠 Model
The model is fine-tuned on a bilingual (Swahili) Q&A dataset built from:
- WHO guidelines
- Tanzania Food and Nutrition Centre (TFNC)
- Parenting forums (BabyCenter, JamiiForums)
- Social media health pages

## 🔐 Secrets
The Hugging Face API token is stored securely in Streamlit Cloud under **`HF_API_TOKEN`**.

