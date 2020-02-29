import sys, os
if sys.argv[1]=='install':
	print("[1] - Kali linux")
	print("[2] - Termux")
	yn = input("[>>>]: ")
	if yn == 1:
		try:
			os.system("apt-get install python")
			os.system("apt-get install pip")
			os.system("pip install colorama")
			os.system("pip install requests")
			os.system("pip install vk")
		except:
			print('')
	else:
		try:
			os.system("pkg install python")
			os.system("pkg install pip")
			os.system("pip install colorama")
			os.system("pip install requests")
			os.system("pip install vk")
		except:
			print('')
else:
	os.system("python3 rocketstart.pyc")
