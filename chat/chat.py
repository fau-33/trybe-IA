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
    text = message["text"]
    ulploaded_files = []
    
    for files_info in message["files"]:
        file_path = files_info["path"]
        ulploaded_file_info = genai.upload_file(file_path)
        ulploaded_files.append(ulploaded_file_info)
    
    prompt = [message["text"]]
    prompt.extend(ulploaded_files)  
        
    response = chat.send_message(prompt)
    return response.text


chatInterface = gr.ChatInterface(fn=gradio_wrapper, multimodal=True)
chatInterface.launch()
