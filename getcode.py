import urllib.request
import urllib.parse
import tkinter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from tkinter.messagebox import *
from tkinter import *
import sys

fenetre = tkinter.Tk()
fenetre.title('GETCODE By mwarKo for bettersec')
pref = 'http://www.'
addr = 'google.fr'
src = ''
dest = ''
pwd = ''
e = "code"


def getresp():
	addr = texte_addr.get()
	try:
		req = urllib.request.Request(pref + addr, headers = {'User-Agent' : 'Mozilla/5.0'})
		global e
		e = str(urllib.request.urlopen(req).getcode())
		print(e)
		lbl_code.configure(text='Le code de retour du site est : ' + e)
	except urllib.error.HTTPError as e:
		e = str(e.getcode())
		msg = MIMEMultipart()
		msg['From'] = 'MONITORING BETTERSEC'
		msg['Subject'] = 'erreur de type ' + e + ' chez ' + addr
		msg.attach(MIMEText('erreur de type ' + e + ' chez ' + addr))
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(src,pwd)
		server.sendmail(src, dest, str(msg))
		server.quit()
		lbl_code.configure(text='Le code de retour du site est : ' + e)

def exxit():
	if askyesno('Quitter ?', 'Êtes-vous sûr de vouloir quitter ?'):
		sys.exit()
	else :
		pass

tkinter.Label(fenetre, text='Rentrez une adresse de site internet que vous souhaitez tester (de type \"google.fr\"): ').pack()
texte_addr = tkinter.Entry(fenetre)
texte_addr.pack()
lbl_code = tkinter.Label(fenetre, text='Le code de retour du site est : ' + e)
lbl_code.pack()
tkinter.Button(fenetre, text='OK', command=getresp).pack()
tkinter.Button(fenetre, text='QUIT', command=exxit).pack()

fenetre.mainloop()


