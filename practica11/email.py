from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import getpass
from email.mime.base import MIMEBase
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Ingresa su nombre de usuario").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
usuario= input("Ingrese su nombre de usuario:")
root = Tk()
frm = ttk.Frame(root, padding=1)
frm.grid()
ttk.Label(frm, text="Ingrese su contraseña").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
root.mainloop()
contraseña=getpass.getpass("Ingrese su  contraseña:")
root = Tk()
frm = ttk.Frame(root, padding=1)
frm.grid()
ttk.Label(frm, text="Ingrese el correo del destinatario").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
destinatario = input("Ingrese el correo del destinatario: ")
root = Tk()
frm = ttk.Frame(root, padding=1)
frm.grid()
ttk.Label(frm, text="Ingrese el asunto").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
asunto = input("Ingrese el asunto:")
root = Tk()
frm = ttk.Frame(root, padding=1)
frm.grid()
ttk.Label(frm, text="Ingrese el mensaje a mandar").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
mensaje=input("Ingrese el mensaje a mandar:")
mensaje="Subject: {}\n\n{}".format(asunto,mensaje)
# create and setup the parameters of the message
email_msg = MIMEMultipart()
email_msg["From"] =usuario
email_msg["To"] = destinatario
email_msg["Subject"] = asunto


email_msg.attach(MIMEText(asunto, "plain"))
# add in the message body
email_msg.attach(MIMEText(mensaje, "plain"))

# create server
server = smtplib.SMTP("smtp.office365.com:587")
server.starttls()
# Login Credentials for sending the mail
server.login(usuario,contraseña)


# send the message via the server.
server.sendmail(usuario,destinatario,mensaje)
server.quit()
print("successfully sent email to %s:" % (email_msg["To"]))