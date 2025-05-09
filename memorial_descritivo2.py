from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
import matplotlib.pyplot as plt
import io
import uuid
import json


# vem uma def Criar_memorial() quando os dados forem inseridos


