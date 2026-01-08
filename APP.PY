import smtplib
from email.message import EmailMessage
from openpyxl import load_workbook
from datetime import datetime

# config esperta p nao se perder
ARQUIVO_EXCEL = 'planilhas.xlsx'
ABA = 'Folha1'
ARQUIVO_TXT = 'contas.txt'
#informacao dos emails
EMAIL_REMETENTE = 'seuemail@gmail.com'
SENHA_APP = 'SUA_SENHA_DE_APP'
EMAIL_DESTINO = 'cliente@email.com'

# abre o arq q ta na pasta
wb = load_workbook(ARQUIVO_EXCEL)
ws = wb[ABA]

# data agr
data_atual = datetime.now().strftime('%d/%m/%Y')

# coloca os dados no exc
with open(ARQUIVO_TXT, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(',')
        if len(dados) == 2:
            ws.append([data_atual, dados[0], float(dados[1])])

wb.save(ARQUIVO_EXCEL)

# envia para o email
msg = EmailMessage()
msg['Subject'] = 'Relatório atualizado'
msg['From'] = EMAIL_REMETENTE
msg['To'] = EMAIL_DESTINO
msg.set_content('Segue em anexo a planilha atualizada automaticamente.')

with open(ARQUIVO_EXCEL, 'rb') as f:
    msg.add_attachment(
        f.read(),
        maintype='application',
        subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        filename=ARQUIVO_EXCEL
    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_REMETENTE, SENHA_APP)
    smtp.send_message(msg)

print("Excel atualizado e enviado por e-mail com sucesso.")
