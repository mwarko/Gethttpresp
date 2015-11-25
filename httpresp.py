import urllib.request
import urllib.parse
import tkinter
addr = "www.hakatecom.fr"

def getresp(url):
	try:
		req = urllib.request.Request(url, headers = {'User-Agent' : 'Mozilla/5.0'})
		print(urllib.request.urlopen(req).getcode())
	except urllib.request.HTTPError as e:
		print(e.getcode())


getresp("http://hakatelecom.fr")



