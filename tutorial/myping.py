import os
def myping(ip):
	command = "ping -n 1  {} > NUL".format(ip)
	respose = os.system(command)
	if respose == 0:
		return True
	else:
		return False