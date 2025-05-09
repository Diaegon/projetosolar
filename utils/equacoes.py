import json
import matplotlib.pyplot as plt
from reportlab.platypus import Image

caminho_absoluto = r"C:\Users\DIEGO\Desktop\code\projetosolar\inputs\input_solar.json"
with open(caminho_absoluto, 'r') as f:
    inputs = json.load(f)
    
potenciatotalpainel = inputs['dados_cliente']['quantidade_painel'] * inputs['painel']['potencia'] / 1000
potenciaefetiva = potenciatotalpainel * 0.745
energia_gerada = potenciaefetiva * 5.84 * 30
corrente_saida = inputs['inversor']['potencia'] / 220
tensao_queda = (200 * 0.0173 * 10 * corrente_saida) / (220 * inputs['inversor']['cabo']) 
resultado = inputs['dados_cliente']['energia'] / 720
fatordecarga = resultado / inputs['dados_cliente']['carga']

#EQ.DEMANDA MEDIA
equacao = fr"$D_{{\mathrm{{media}}}} = \frac{{\mathrm{{Energia\ media}}}}{{N^{{\circ}}\,\mathrm{{de\ horas}}}} = \frac{{{inputs['dados_cliente']['energia']}}}{{720}} = {resultado:.2f}\ kW$"
#EQ.FATOR DE CARGA
equacao2 = fr"$FC = \frac{{\mathrm{{Energia}}}}{{\mathrm{{Potencia \ instalada \ x \ 720h}}}} = \frac{{{inputs['dados_cliente']['energia']}}}{{{inputs['dados_cliente']['carga']} \ x  \ 720}} = {fatordecarga:.2f}\ kW$"
#EQ. DISJUNTOR PROTECAO INVERSOR
equacao3 = fr"$I_{{\mathrm{{AG}}}} = \frac{{\mathrm{{potencia\ nominal}}}}{{\mathrm{{Tensao\ nominal}}}} = \frac{{{inputs['inversor']['potencia']}}}{{{inputs['inversor']['tensao']}}} = {corrente_saida:.2f}\ A$"
#EQ. QUEDA DE TENSÃO
equacao4 = fr"$\Delta V \% = \frac{{200*\rho*L_c*I_c*cos\varphi}}{{S_c*V_f}}$"


def render_equation_to_image(equation, filename):
    fig = plt.figure(figsize=(3, 1))
    plt.text(0.5, 0.5, f"${equation}$", fontsize=20, ha='center', va='center')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1, dpi=200)
    plt.close()
def insert_equation(equation, story, img_filename):
    render_equation_to_image(equation, img_filename)
    img = Image(img_filename)
    img.drawHeight = 50
    img.drawWidth = 250
    story.append(img)


