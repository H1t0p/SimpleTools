import requests
import os
import time
from pyfiglet import Figlet

banner = Figlet(font='slant')
print(banner.renderText('U OK?'))
print('''
	@__JustGabe__
	
	Simple Tool to check if urls in a a file returns 200 OK

	''')
on = 0

path = ('/home/h1t0p/Desktop/H1/chargepoint/http_new_sub.txt')
with open(path) as n:
	lines = [l.rstrip() for l in n]
	for urls in lines:
		try:
			print(f'[*] Url: {urls}')
			req = requests.get(f'{urls}')
			if req.status_code == requests.codes.ok:
				end = os.system(f'echo {urls} >> response.txt')
				on += 1
			else:
				pass
		except:
			time.sleep(5)
			pass		

print(f'[*] 200 OK: {on}')
