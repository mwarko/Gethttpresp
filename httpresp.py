import urllib.request
import urllib.parse
import tkinter
import smtplib
pref = 'http://www.'
addr = 'google.fr/sweg'
src = ''
dest = ''
pwd = ''
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def getresp(url):
	try:
		req = urllib.request.Request(url, headers = {'User-Agent' : 'Mozilla/5.0'})
		print(urllib.request.urlopen(req).getcode())
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

getresp(pref + addr)


