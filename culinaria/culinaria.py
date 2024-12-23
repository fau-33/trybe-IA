import google.generativeai as genai
import os

# Configura a chave da API
genai.configure(api_key=os.environ["GEMINI_API"])

# Cria a instância do modelo
model = genai.GenerativeModel("gemini-1.5-flash")

# Faz o upload da imagem
food_plate = genai.upload_file(path="prato-de-comida.png", display_name="Prato")

# Prepara o prompt
prompt = "Pode identificar com cuidado o que é servido nesse prato e estimar grosseiramente as suas calorias?"

# Chama generate_content passando uma lista com o prompt e a imagem
response = model.generate_content([prompt, food_plate])

# Imprime o texto da resposta
print(response.text)
