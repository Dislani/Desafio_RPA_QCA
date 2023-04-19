from selenium import webdriver                          
import smtplib                                          
import time                                             
from email.mime.multipart import MIMEMultipart          
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Configurando o diretório padrão para Download do arquivo bairro.csv
download_dir = "C:\\Users\\usuario\\Downloads"
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}
chrome_options.add_experimental_option("prefs", prefs)

driver_chrome = webdriver.Chrome()                                  # Abri o navegador Chrome

driver_chrome.get("http://dados.recife.pe.gov.br/organization")     # Entrando na página incial do portal de dados abertos do Recife


driver_chrome.find_element('xpath', '//*[@id="content"]/div[3]/div/article/div/ul/li[19]/a').click()    # Clicando no link de Secretaria de Infraestrura e Serviços Urbanos

driver_chrome.find_element('xpath', '//*[@id="content"]/div[3]/div/article/div/ul/li[1]/div/h3/a').click()  # Clicando no link de Área Urbana

driver_chrome.find_element('xpath', '//*[@id="dataset-resources"]/ul/li[1]/a').click()                      # Clicando em Bairros do Recife

driver_chrome.find_element('xpath', '//*[@id="content"]/div[3]/section/div/div[1]/ul/li[1]/div/a').click()      # Clicando no botão de Baixar o arquivo bairro.csv

time.sleep(10)  # Aguardando 10 segundos para o download do arquivo

# Criando um e-mail, com o Assunto, Remetente, Destinatário e Senha
remetente = 'email_remetente'
destinatario = 'email_destinatario'
senha = 'senha_email_remetente'
assunto = 'Assunto Desejado'

msg = MIMEMultipart()
msg['From'] = remetente
msg['To'] = destinatario
msg['Subject'] = assunto

# Abaixo, segue o corpo do e-mail a ser enviado
corpo = 'corpo do e-mail'
msg.attach(MIMEText(corpo))

# Adicionando o anexo bairro.csv ao e-mail
anexo = open('C:\\Users\\usuario\\Downloads\\bairro.csv', 'rb')                # Abrindo o arquivo bairro.csv, para anexá-lo ao e-mail
content_type = MIMEBase('application', 'octet-stream')                              # Informando o Content-Type (tipo do conteúdo) do arquivo
content_type.set_payload((anexo).read())                                        
encoders.encode_base64(content_type)                                                # Codificando o arquivo bairro.csv em Base64
content_type.add_header('Content-Disposition', "attachment; filename= bairro.csv")  # Adicionando o cabeçalho do arquivo bairro.csv
msg.attach(content_type)                                                            # Anexando o arquivo bairro.csv ao e-mail

# Conectando ao servidor SMTP do Outlook
smtp_server = smtplib.SMTP('smtp.office365.com', 587)                               # Conectando ao servidor SMTP do Outlook
smtp_server.starttls()                                                              # Iniciando a conexão com o servidor SMTP do Outlook

# Realizando login na conta do Outlook
smtp_server.login(remetente, senha)                                                        # Realizando login na conta do Outlook

# Enviando o e-mail
smtp_server.sendmail(remetente, destinatario, msg.as_string())                                     # Enviando o e-mail com o anexo bairro.csv

# Fechando a conexão com o servidor
smtp_server.quit()                                                                  # Fechando a conexão com o servidor SMTP do Outlook

driver_chrome.close()   # Fechando o navegador Chrome
