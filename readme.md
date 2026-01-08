# 📊 AutoExcelMailer – Automatize seus relatórios 💌

Um **script Python inteligente** que atualiza automaticamente suas planilhas Excel a partir de um arquivo `.txt` e envia o relatório por e-mail em um clique! 🚀

---

## 🔹 Funcionalidades

- ✅ Atualiza automaticamente planilhas Excel (`.xlsx`) com novos dados  
- ✅ Lê dados de um arquivo `.txt` organizado  
- ✅ Adiciona a data atual de forma automática  
- ✅ Envia a planilha atualizada por e-mail com **anexo**  
- ✅ Configuração simples e personalizável

---

## ⚙️ Como usar

1. Clone este repositório:
```bash``
git clone https://github.com/maargadux/autoexcelmailer

    - Instale as dependências:

pip install openpyxl

    - Configure suas variáveis no script autoexcelmailer.py:

ARQUIVO_EXCEL = 'planilhas.xlsx'
ABA = 'Folha1'
ARQUIVO_TXT = 'contas.txt'
EMAIL_REMETENTE = 'seuemail@gmail.com'
SENHA_APP = 'SUA_SENHA_DE_APP'
EMAIL_DESTINO = 'cliente@email.com'

    - 💡 Dica: Crie uma senha de app no Gmail para maior segurança.

    - Execute o script:

python autoexcelmailer.py

## 🖌️ Exemplo de arquivo .txt

- Luz,120.50
- Água,80.00
- Internet,150.00


O script vai adicionar automaticamente a data atual e os valores na sua planilha Excel.

## 📈 Resultado

   - Planilha atualizada automaticamente
   - E-mail enviado com anexo em poucos segundos
   - Nada de trabalho manual repetitivo! 💪

## 💻 Tecnologias usadas

   - Python 🐍
   - openpyxl 📑
   - smtplib 📧
   - EmailMessage ✉️

## 🚀 Próximos passos

   - Adicionar interface gráfica
   - Automatizar envio recorrente com cron jobs / agendador do Windows
   - Integração com Google Sheets


Feito com por Mali

