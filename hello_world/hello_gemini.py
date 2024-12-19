import google.generativeai as genai
import os


genai.configure(api_key=os.environ["GEMINI_API"])

model = genai.GenerativeModel("gemini-1.5-flash")
response =  model.generate_content("Criei uma história sobre o tempo passando rápido")
print(response.text)