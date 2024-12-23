import google.generativeai as genai
import os

# Configura a chave da API
genai.configure(api_key=os.environ["GEMINI_API"])

# Cria a instância do modelo
model = genai.GenerativeModel("gemini-1.5-flash")

# Faz o upload da imagem
vacation_image = genai.upload_file(path="social_media_viagem.png", display_name="Prato")

# Prepara o prompt
prompt = "PPode gerar uma descrição dessa imagem para o Instagram? Quero algo para escrever no post e uma descrição da imagem para fins de acessibilidade."

# Chama generate_content passando uma lista com o prompt e a imagem
response = model.generate_content([prompt, vacation_image])

# Imprime o texto da resposta
print(response.text)
