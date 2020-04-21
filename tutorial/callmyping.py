
from myping import myping



ips = [
"www.google.com",
"www.apple.com",
"www.deloitte.com",
"localhost",
"127.0.0.1",
"www.donaldtrumpnarendramodisoniagandhi.com"
]


for ip in ips:
	if myping(ip) == True:
		print("{} is up".format(ip))
	else:
		print("{} is down".format(ip))
