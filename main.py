import json
from gerar_pdf import gerar_memorial, gerar_procuracao


caminho_absoluto = r"C:\Users\DIEGO\Desktop\code\projetosolar\inputs\input_solar.json"
with open(caminho_absoluto, 'r') as f:
    inputs = json.load(f)


gerar_memorial(inputs)
gerar_procuracao(inputs)