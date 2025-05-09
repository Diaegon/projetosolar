import json
from reportlab.platypus import Table, Paragraph, TableStyle
from utils.estilos import styles, estilotabela, estilotabelaloc, estilo_tabela_parametros
from utils.equacoes import (corrente_saida, tensao_queda, potenciaefetiva, energia_gerada)
caminho_absoluto = r"C:\Users\DIEGO\Desktop\code\projetosolar\inputs\input_solar.json"
with open(caminho_absoluto, 'r') as f:
    inputs = json.load(f)


dados = [[f"UC:{inputs['dados_cliente']['UC']}"], [f"Classe:{inputs['dados_cliente']['classeconsumo']}  {inputs['dados_cliente']['fornecimento']} "], [f"Nome do Cliente: {inputs['dados_cliente']['nome']}"],
         [f"Endereço: {inputs['endereco']['logradouro']}, {inputs['endereco']['numero_casa']}  {inputs['endereco']['complemento']}, {inputs['endereco']['municipio']}, {inputs['endereco']['estado']}."],
         [f"CEP:{inputs['endereco']['CEP']}"],
         [f"CPF/CNPJ: {inputs['dados_cliente']['CPF']}"]]
tabeladedados = Table(dados)
tabeladedados.setStyle(estilotabela)

loc_instalacao = [["COORDENADAS - coordenadas decimais - WGS 84 "],
                  [" Local de implantação do Gerador fotovoltaico",
                      "Lat: ", "Long: "],
                  ["", f"{inputs['endereco']['latitude']:.5f}", f"{inputs['endereco']['longitude']:.5f}"]]
tabela_localizacao = Table(loc_instalacao)
tabela_localizacao.setStyle(estilotabelaloc)

modulo_caracteristicas = [["Potência nominal máx. (Pmax) ", f"{inputs['painel']['potencia']} Wp"],
                          ["Tensão operacional opt. (Vmp) ", f"{inputs['painel']['vp']} V"],
                            ["Corrente operacional opt. (Imp)", f"{inputs['painel']['imp']} A"], 
                            ["Tensão circuito aberto (Voc) ", f"{inputs['painel']['voc']} V"], 
                            ["Corrente curto-circuito (Isc)", f"{inputs['painel']['isc']} A"]]
tabelapainel = Table(modulo_caracteristicas)
tabelapainel.setStyle(estilotabela)

parametros_tensao_inversor = [["Faixa de tensão no ponto de conexão [V]","Tempo de desconexão [s]"], ["TL > 231","0,2 s"], ["189 ≤ TL ≤ 231","Operação Normal"], ["TL < 195,5","0,2 s"]]
tabela_parametros_tensao_inversor = Table(parametros_tensao_inversor)
tabela_parametros_tensao_inversor.setStyle(estilo_tabela_parametros)

parametros_frequencia_inversor = [["Faixa de freqüência no ponto de conexão (Hz)","Tempo de desconexão [s]"], ["f ≤ 57,5","0,2"],["59,9 < f ≤ 60,1","Operação normal"],["f > 62,5","0,2"] ]
tabela_parametros_frequencia_inversor = Table(parametros_frequencia_inversor)
tabela_parametros_frequencia_inversor.setStyle(estilo_tabela_parametros)

parametros_fp_inversor = [["Potência Nominal (W) - Pn","Faixa de fator de potência","Fator de potência \nconfiguração em fábrica"], [f"{inputs['inversor']['potencia']}","0,95 indutivo – 0,95 capacitivo","1"]]
tabela_parametros_fp_inversor = Table(parametros_fp_inversor)
tabela_parametros_fp_inversor.setStyle(estilo_tabela_parametros)

queda_tensao = [["ρ  - resistividade do cobre","0,0173"], [Paragraph("L<sub>c</sub> - comprimento do condutor",styles["CorpoTexto"]),"10 m"], 
                [Paragraph("I<sub>c</sub> - corrente do condutor",styles["CorpoTexto"]),f"{corrente_saida:.2f} A"], ["Cosφ - fator de potencia","1"], [Paragraph("S<sub>c</sub> - Seção reta do condutor",styles["CorpoTexto"]), f"{inputs['inversor']['cabo']} mm²"], 
                [Paragraph("V <sub>f</sub> - tensão ", styles["CorpoTexto"]), f"{inputs['inversor']['tensao']}"]]
tabela_queda_tensao = Table(queda_tensao)
tabela_queda_tensao.setStyle(estilotabela)