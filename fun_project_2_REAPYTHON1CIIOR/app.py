import streamlit as st 
import requests 
from datetime import datetime

# Streamlit app for AI Chatbot with Bubble Style UI
st.set_page_config(
    page_title="AI Chatbot Bubble Style",
    page_icon="🤖",
    layout="wide"
)


# CONFIGURATION (CONFIG)
OPENROUTER_API_KEY = "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"
MODEL = "deepseek/deepseek-chat-v3-0324"
HEADERS = {
  "Authorization": f"Bearer {OPENROUTER_API_KEY}",
  "HTTP-Referer": "http://localhost:8501", #Ini buat nentuin http yang bisa akses API Key ini siapa aja, kebetulan ini localhost:8501 tuh buat streamlit
  "X-Title": "AI Chatbot Streamlit"
}
API_URL = "https://openrouter.ai/api/v1/chat/completions" # Endpoint untuk OpenRouter API
#===fungsi untuk mendapatkan response dari OpenRouter API===



# SIDEBAR
st.sidebar.title("Pengaturan Chatbot")
# 1. Sidebar: Pilih Model LLM
AVAILABLE_MODELS = {
    "deepseek/deepseek-chat-v3-0324": "DeepSeek Chat v3",
    "openai/gpt-3.5-turbo": "GPT-3.5 Turbo",
    "openai/gpt-4": "GPT-4"
}
    # Dropdown untuk memilih model LLM
selected_model = st.sidebar.selectbox(
    "Pilih Model LLM",
    options=list(AVAILABLE_MODELS.keys()),
    format_func=lambda x: AVAILABLE_MODELS[x]
)
#2. Sidebar: Bahasa Default Model
# Tambahkan pilihan bahasa di sidebar
LANGUAGES = {
    "id": "Bahasa Indonesia",
    "en": "English"
}
selected_lang = st.sidebar.selectbox(
    "Pilih Bahasa Chatbot",
    options=list(LANGUAGES.keys()),
    format_func=lambda x: LANGUAGES[x]
)
# Mapping prompt system sesuai bahasa
SYSTEM_PROMPTS = {
    "id": "Kamu adalah asisten yang membantu dalam Bahasa Indonesia.",
    "en": "You are a helpful assistant. Use english language to respond."
}
# 3. Sidebar: Tombol Chat Baru
if st.sidebar.button("Chat Baru"):
    st.session_state.chat_history = []
# Update MODEL variable based on selection
MODEL = selected_model

# UI
st.title("🧠 AI Chatbot Bubble Style")
st.caption("""Made by : Felix Kho  
           Github : felixkhoiscoding""")
st.markdown(f"Powered by {MODEL} via OpenRouter 🤖")

# CHAT HISTORY
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# SHOWS PREVIOUS CHAT
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])
        st.caption(f"**{chat['time']}**")

# USER INPUT
if selected_lang == "id":
    user_input = st.chat_input("Tulis pesan di sini...")
else:
    user_input = st.chat_input("Type your message here...")

# PROCESS USER INPUT
if user_input:
    timestamp_user = datetime.now().strftime("%H:%M")
    with st.chat_message("user"):
        st.markdown(user_input)
        st.caption(f"**{timestamp_user}**")
    st.session_state.chat_history.append({
    "role": "user",
    "content": user_input,
    "time": timestamp_user
})

else:
    if selected_lang == "id":
        st.warning("Silakan masukkan pesan untuk memulai percakapan.")
    else:
        st.warning("Please enter a message to start the conversation.")
    st.stop()

# SEND REQUEST TO OPENROUTER API
if selected_lang == "id":
    spinner_text = "Mengetik..."
else:
    spinner_text = "Typing..."
with st.spinner(spinner_text):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPTS[selected_lang]}, # PRMOMPTING MODELNYA INI
            {"role": "user", "content": user_input}
        ]
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)

# HANDLE API RESPONSE
if response.status_code == 200:
    bot_reply = response.json()['choices'][0]['message']['content']
else:
    bot_reply = "⚠️ Maaf, gagal mengambil respons dari OpenRouter."

# SHOW BOT REPLY
timestamp_bot = datetime.now().strftime("%H:%M")
with st.chat_message("assistant") :
        st.markdown(bot_reply)
        st.caption(f"**{timestamp_bot}**")
st.session_state.chat_history.append({
    "role": "assistant",
    "content": bot_reply,
    "time": timestamp_bot
})
