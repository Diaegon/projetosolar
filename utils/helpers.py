from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
import matplotlib.pyplot as plt
from reportlab.lib.units import cm

data_de_hoje = datetime.now()
data_futura = data_de_hoje+relativedelta(months=1)
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
plt.rcParams['text.usetex'] = True # Ativar o uso do LaTeX real (MikTeX)


def linha_sumario(titulo, pagina, largura_pontilhado=80):
    """Retorna uma string formatada com pontilhado entre título e página"""
    max_linha = largura_pontilhado
    texto_base = f'{titulo} '
    dots = '.' * max(3, max_linha - len(texto_base) - len(str(pagina)))
    return f'{texto_base}{dots} {pagina}'
def add_page_number(canvas, doc):
    page_num = canvas.getPageNumber()
    text = f"Página {page_num}"
    canvas.setFont('Helvetica', 9)
    width, height = doc.pagesize
    canvas.drawCentredString(width / 2.0, 1.5 * cm, text)
