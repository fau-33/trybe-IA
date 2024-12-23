import google.generativeai as genai
import os
import gradio as gr

# Configura a chave da API
genai.configure(api_key=os.environ["GEMINI_API"])

# Cria a instância do modelo
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()
initial_prompt = "Você é um consultor de desenvolvimento de projetos."
chat.send_message(initial_prompt)

def gradio_wrapper(message, _history):
    response = chat.send_message(message)
    return response.text


chatInterface = gr.ChatInterface(gradio_wrapper)
chatInterface.launch()
