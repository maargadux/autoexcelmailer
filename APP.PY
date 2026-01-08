import smtplib
from email.message import EmailMessage
from openpyxl import load_workbook
from datetime import datetime

# config esperta p nao se perder
arquivo_exc = 'planilhas.xlsx'  # nome do arquivo da planilha
aba = 'Folha1'                  # aba que aparece na planilha
arq_txt = 'contas.txt'          # nome do seu bloco de notas

# informações dos emails
eme_rem = 'seuemail@gmail.com'
senha_apps = 'senhaapp'
eme_desti = 'clienteemail@email.com'

# abre o arquivo
wb = load_workbook(arquivo_exc)
ws = wb[aba]

# data atual
data_atual = datetime.now().strftime('%d/%m/%Y')

# coloca os dados no excel
with open(arq_txt, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(',')
        if len(dados) == 2:
            ws.append([data_atual, dados[0], float(dados[1])])

wb.save(arquivo_exc)

# envia para o email
msg = EmailMessage()
msg['Subject'] = 'Relatório atualizado'
msg['From'] = eme_rem
msg['To'] = eme_desti
msg.set_content('Segue em anexo a planilha atualizada automaticamente.')

with open(arquivo_exc, 'rb') as f:
    msg.add_attachment(
        f.read(),
        maintype='application',
        subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        filename=arquivo_exc
    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(eme_rem, senha_apps)
    smtp.send_message(msg)

print("Excel atualizado e enviado por e-mail com sucesso.")
