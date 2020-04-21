import os

ips = [
"www.google.com",
"www.apple.com",
"www.deloitte.com",
"localhost",
"127.0.0.1",
"www.donaldtrumpnarendramodisoniagandhi.com"
]
def myping(ip):
	command = "ping -n 1  {} > NUL".format(ip)
	respose = os.system(command)
	if respose == 0:
		return True
	else:
		return False

for ip in ips:
	if myping(ip) == True:
		print("{} is up".format(ip))
	else:
		print("{} is down".format(ip))
