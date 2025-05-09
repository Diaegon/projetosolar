import json
from datetime import datetime 
from dateutil.relativedelta import relativedelta
from utils.equacoes import potenciatotalpainel, potenciaefetiva, energia_gerada,tensao_queda

caminho_absoluto = r"C:\Users\DIEGO\Desktop\code\projetosolar\inputs\input_solar.json"
with open(caminho_absoluto, 'r') as f:
    inputs = json.load(f)


data_de_hoje = datetime.now()
data_futura = data_de_hoje+relativedelta(months=1)

def texto_introducao():
    return f"   O presente relatório técnico tem por objetivo apresentar o memorial descritivo \
                       para implantação de um Gerador Fotovoltaico de fabricação da <b>{inputs['inversor']['marca']} {inputs['inversor']['modelo']}</b>. \
                         Este modelo e quantidade de gerador foi previamente aprovado pelo proprietário da residência.\
                             Este gerador fotovoltaico se conectará ao sistema de baixa tensão, após a medição \
                                de energia da ENEL. O mesmo terá como objetivo suprir parte das cargas desta residencia. \
                                 A previsão de ligação do sistema elétrico é para <b>{data_futura.strftime("%d de %B de %Y")}</b>."
def texto_loc():
    return f"No diagrama de situação é ilustrada a planta de situação da residência onde será \
 implantado na {inputs['endereco']['logradouro']}, {inputs['endereco']['numero_casa']}  {inputs['endereco']['complemento']}, {inputs['endereco']['municipio']}, {inputs['endereco']['estado']}. A tabela 2.1 \
 mostra o georeferenciamento da localidade de instalação e do gerador."
def texto_loc2():
    return "A área de telhado da residência foi escolhida por apresentar vantagens de insolação \
 permanente durante todas as horas do dia para evitar o sombreamento dos painéis \
 fotovoltaicos e segurança dos equipamentos"
def texto_carginst():
    return f"A carga instalada é típica de um estabelecimento {inputs['dados_cliente']['classeconsumo']}, constituído de iluminação e \
 eletrodomésticos diversos, sendo {inputs['dados_cliente']['carga']} kW.  A energia \
 media de consumo é de  {inputs['dados_cliente']['energia']} kWh."
def texto_calculo_demanda():
    return "Considerando um mês comercial com 720 horas, pode-se calcular a demanda média \
 mensal através da equação:"
def texto_calculo_demanda2():
    return "Esta demanda média está dentro do limite da potência máxima injetada no sistema \
da ENEL, de acordo com a norma NT - 010."
def texto_calculo_fc():
    return "O fator de carga médio desta residência é calculado através da equação:"


def texto_geradorfv():
# logica dos inversores
 #- inversor de 3kW até 7kw sempre vão ter duas entradas para string
 #- inversor de 7.1kw até 16.9kw sempre vão ter 3 entradas para string
 #- inversor de 17kw até 26.9kw sempre vão ter 4 entradas para string
 #- inversor de 27kw até 40kw sempre vão ter 6 entradas para string

 #inicio da logica dos inversores e paineis
  #  quantidade_de_paineis = {inputs['dados_cliente']['quantidade_painel']}
   # texto = f"O Gerador Fotovoltaico escolhido para compor a geração suplementar da residência Alvo deste projeto é composto de {quantidade_de_paineis}  módulos Fotovoltaicos {inputs['painel']['marca']}  {inputs['painel']['modelo']}  de {inputs['painel']['potencia']} Wp"

    return f"O Gerador Fotovoltaico escolhido para compor a geração suplementar da residência \
    Alvo deste projeto é composto de {inputs['dados_cliente']['quantidade_painel']}  módulos Fotovoltaicos {inputs['painel']['marca']}  {inputs['painel']['modelo']}  de {inputs['painel']['potencia']} Wp \
a e {inputs['dados_cliente']['quantidade_inversor']}  inversor {inputs['inversor']['marca']} {inputs['inversor']['modelo']} . \
O   modulo   solar   fotovoltaico   monocristalino   ({inputs['painel']['potencia']} Wp)   possui   as   características \
técnicas   apresentado   na   tabela   a seguir.   Considerando   que   os   módulos   instalados   são   os   de \
{inputs['painel']['potencia']} , e que eles tem uma tensão elétrica de máxima potência (Vmp) de {inputs['painel']['vp']} Vmp. A \
solução prevista para ser instalada tem 1 arranjo com 6 módulos. Tendo um sistema total \
com {inputs['dados_cliente']['quantidade_painel']} módulos que resultam numa potência total de {potenciatotalpainel:.2f} kWp." 
#TEM QUE AJUSTAR A LÓGICA DESSA ULTIMA PARTE DOS ARRANJOS



def texto_potenciafv():
    return f"O georeferenciamento do local da instalação do Gerador Fotovoltaico estabelece o \
valor de 74,5% das Condições de Teste padrão (STC) do modulo Fotovoltaico. Por essa \
premissa,  terei   uma   Potencia   resultante   do  meu  Gerador  Fotovoltaico  (GF)  também   de \
74,5% da Potencia instalada ({potenciatotalpainel:.2f} kW). Assim, a Potencia efetiva do GF é de  {potenciaefetiva:.2f}kW, o\
que satisfaz a demanda média calculada."
def texto_calculo_enegiagerada():
    return f"Considerando a potência média disponível de  {potenciaefetiva:.2f} kW  e a média anual do ponto \
georeferenciado do sistema Horas de Sol a Pico (HSP) que é de 5,84 kWh/m2/dia, como \
parâmetro de medição da radiação solar em um mês comercial, pode-se calcular a energia \
média através do produto destas duas grandezas, que resulta em {energia_gerada:.0f} kWh."
def texto_diagramas():
    return "A figura a seguir apresenta o esquema básico de ligação de um Gerador Fotovoltaico. \
Nesta   figura   pode   ser   ver   todas   as   partes   que   compõem   o   sistema,   desde   o   Gerador \
Fotovoltaico até a conexão à carga e à rede."
def texto_parametrizacao():
    return "O inversor para cumprir sua função de proteção, é parametrizado com os seguintes \
valores, de modo a não exceder os limites recomendados pela norma NT – 010 Coelce."
def texto_instalacao():
    return "A residência é alimentada através da rede de baixa tensão da ENEL em 220V. O \
ponto de entrega se dá em um quadro instalado junto ao muro da propriedade."
def texto_diagramauni():
    return "O diagrama unifilar geral se encontra em anexo."
def texto_dimensionamento_protecao():
    return f"Este   Gerador   Fotovoltaico   será   conectado   ao   barramento   de   baixa   tensão   do \
consumidor, logo abaixo da proteção geral, que é constituída por um disjuntor {inputs['dados_cliente']['fornecimento']} \
de   {inputs['dados_cliente']['disjuntor_geral']}   A.   Por   sua   vez,   o   ramal   de   interligação   do   Gerador   Fotovoltaico   ao   quadro   de \
medição é feito por  um  disjuntor {inputs['inversor']['numero_fases']} {inputs['inversor']['protecao']} de A. Esta capacidade de condução foi \
calculada através da seguinte equação."
def texto_dimensionamento_protecao2():
    return f"A interligação entre o Gerador Fotovoltaico e o quadro de medição será feito através \
de um cabo de cobre flexível, isolado em PVC com uma seção reta de {inputs['inversor']['cabo']} mm², e sua \
proteção se dará através de um disjuntor de {inputs['inversor']['protecao']} A. \
O   dimensionamento   do   condutor   de   {inputs['inversor']['cabo']}  mm²   atende   aos   critérios   de   máxima \
capacidade de corrente, já que o mesmo tem capacidade térmica de conduzir até {inputs['inversor']['correntemax']} A; e \
atende também ao critério de máxima queda de tensão. \
Como trata-se da interligação de um gerador, a máxima queda de tensão permitida é \
de 3%. A equação abaixo apresenta o cálculo desta queda." 
def texto_dimensionamento_protecao3():
    return f"Introduzindo estes valores na equação anterior resulta em uma queda de tensão de {tensao_queda:.2f} %, o que satisfaz plenamente o limite máximo de queda que é de 3%."
def texto_disjuntores():
    return f"A proteção geral é feita através de um disjuntor {inputs['dados_cliente']['fornecimento']} de {inputs['dados_cliente']['disjuntor_geral']} A, com curva \
direta de atuação C, e o Gerador Fotovoltaico terá a sua proteção realizada por um disjuntor \
{inputs['inversor']['numero_fases']} de {inputs['inversor']['protecao']} A, curva de atuação B. A seletividade é garantida observando o valor \
maior de corrente nominal do disjuntor principal em relação ao disjuntor para proteção do \
cabo do inversor, e suas curvas de atuação."
def texto_sinalizacao():
    return "No padrão de entrada será instalada placa de sinalização, confeccionada em \
PVC 2,0 mm com tratamento anti-UV, conforme Figura a seguir, fixada de acordo \
com o desenho D010.01 dá NT Br-010 R-01, sem que haja a perfuração da caixa para \
fixação da sinalização. "