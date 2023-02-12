
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def pontos (mm):
    return mm / 0.352777


pdf = canvas.Canvas ('./teste.pdf', pagesize=A4)

txttitulo = 'COMISSÃO MOTORISTA'
pdf.setFont('Helvetica-Oblique', 24)
pdf.drawString(pontos(90), pontos(270), txttitulo)

txttabela = 'COMISSÃO MOTORISTA'
pdf.setFont('Helvetica-Oblique', 24)
pdf.drawString(pontos(90), pontos(220), txttabela)

txtdespesas = 'COMISSÃO MOTORISTA'
pdf.setFont('Helvetica-Oblique', 24)
pdf.drawString(pontos(90), pontos(200), txtdespesas)

txtcomissao = 'COMISSÃO MOTORISTA'
pdf.setFont('Helvetica-Oblique', 24)
pdf.drawString(pontos(90), pontos(150), txtcomissao)


pdf.save()