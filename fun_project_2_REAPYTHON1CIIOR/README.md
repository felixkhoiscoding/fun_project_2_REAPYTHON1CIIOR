

# FITUR PEMBEDA DENGAN CHATBOT YANG DIAJARKAN DI ZOOM!
1. Pengaturan Chatbot
    - Sidebar Pemilihan Model LLM
        - Selain dapat memilih model LLMM, caption "Powered by ___ via OpenRouter🤖" akan berubah sesuai model LLM yang dipilih
    - Sidebar Pemilihan Bahasa Chatbot
        - Pesan pada "Input User" berubah sesuai bahasa yang dipilih
            - en : "Type your message here..."
            - id : "Tulis pesan di sini..."
        - Pesan pada "Warning" untuk memasukkan pesan berubah sesuai bahasa yang dipilih
            - en : "Please enter a message to start the conversation"
            - id : "Silahkan masukkan pesan untuk memulai percakapan"
    - Sidebar Tombol "Chat Baru"
        - Jika dipencet maka seluruh chat akan hilang
2. Timestamp
    - Terdapat catatan waktu pesan user terkirim dan pesan chatbot terkirim

3. Page Title sudah dicustom


# Documentation (Made by 'Claude 3.5 Sonnet' Agent )

    ## Technical Overview
    This AI Chatbot application is built using Streamlit and integrates with OpenRouter API to provide conversational AI capabilities. The application supports multiple language models and bilingual interface (Indonesian/English).

    ### Key Components

    1. **Configuration**
    - Uses OpenRouter API for accessing various LLM models
    - Configurable API endpoint and authentication
    - Support for multiple AI models (DeepSeek, GPT-3.5, GPT-4)

    2. **User Interface**
    - Sidebar controls for customization
    - Chat bubble interface for messages
    - Timestamps for all messages
    - Responsive layout with wide screen support

    3. **Features**
    - Model Selection:
        - DeepSeek Chat v3
        - GPT-3.5 Turbo
        - GPT-4
    
    - Language Support:
        - Indonesian (id)
        - English (en)
    
    - Chat Management:
        - Chat history persistence
        - New chat creation
        - Real-time message timestamps

    ### Code Structure

    1. **Initialization**
    ```python
    # Configuration and imports
    import streamlit as st
    import requests
    from datetime import datetime
    ```

    2. **State Management**
    - Uses Streamlit's session state for chat history
    - Maintains language preferences
    - Preserves model selection

    3. **API Integration**
    - OpenRouter API communication
    - Error handling for failed requests
    - Response processing and formatting

    4. **User Interface Components**
    - Chat input field
    - Message display
    - Language switcher
    - Model selector
    - Chat reset button

    ### Usage Instructions

    1. **Starting the Application**
    ```bash
    streamlit run app.py
    ```

    2. **Configuration**
    - Select preferred LLM model from sidebar
    - Choose interface language (ID/EN)
    - Start new chat using "Chat Baru" button

    3. **Chatting**
    - Type message in input field
    - View real-time responses
    - Check timestamps for message history
    - Reset chat when needed

    ### Dependencies
    - streamlit
    - requests
    - datetime

    ### Error Handling
    - API connection failures
    - Invalid user inputs
    - Model response errors
