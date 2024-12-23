import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Verifique a existência do arquivo antes de fazer o upload
file_path_golden = "cachorro_golden_retriever.png"
if os.path.isfile(file_path_golden):
    dog_colen = genai.upload_file(path=file_path_golden)
else:
    print(f"Arquivo não encontrado: {file_path_golden}")

file_path_collie = "cachorro_collie_acho.png"
if os.path.isfile(file_path_collie):
    dog_bordercollie = genai.upload_file(path=file_path_collie)
else:
    print(f"Arquivo não encontrado: {file_path_collie}")

response = model.generate_content([dog_bordercollie, "Pode identificar a raça do cachorro da foto e me dar duas ou três frases de informações a respeito dele? "
   "De preferência, alguma curiosidade interessante em português, citando a fonte da informação e sempre de um jeito leve e interessante." ])

print(response.text)
