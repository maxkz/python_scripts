import ntplib, threading
from time import ctime

c = ntplib.NTPClient()

def load_ntp(l):
	while l < 10:
		try:
			r = c.request('IP-address', version=3)
			print(r.offset)
			l += 1
		
			
		except IOError as e:
			print('Could not connect to NTP server')
	
	

for i in range(0, 30):
	t = threading.Thread(target = load_ntp, args = (1,))
	print('this Thread with number %s' %i)
	#t.daemon = True
	t.start()

#load_ntp(100)

	