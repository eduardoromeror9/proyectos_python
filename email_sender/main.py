from email.message import EmailMessage
from password import password
import ssl
import smtplib

email_sender = 'email@email.com'  # email que envia el correo
email_password = password # contraseña del email que envia el correo importada desde el archivo password.py
email_receiver = 'email@email.com' # email que recibe el correo
asunto = 'Mi app de Python3' 
mensaje = 'Hola, este es un mensaje de prueba para enviar un correo desde mi app de Python3'

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['Subject'] = asunto
email.set_content(mensaje) # set_content() es un metodo de la clase EmailMessage que permite establecer el contenido del correo


context = ssl.create_default_context() # crea un contexto seguro para la conexion con el servidor de correo
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: # crea una conexion segura con el servidor de correo de gmail y la cierra al terminar el bloque with, el 465 es el puerto de gmail
    smtp.login(email_sender, email_password) # inicia sesion en el servidor de correo
    smtp.sendmail(email_sender, email_receiver, email.as_string()) # envia el correo
    print('Correo enviado')