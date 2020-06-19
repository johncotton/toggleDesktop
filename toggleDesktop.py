import os

def main():
	user = os.getlogin()
	if os.path.exists("/Users/" + user + "/.toggle"):
		os.system("rm /Users/" + user + "/.toggle")
	os.system("defaults read com.apple.finder CreateDesktop >> /Users/" + user + "/.toggle")
	try:
		f = open("/Users/" + user + "/.toggle")
		content= str(f.read()).strip()
		f.close()
		print(content)
	except:
		raise NameError('No toggle file detected.')
	if content == 'false':
		on()
	else:
		off()


def on():
	print('on')
	os.system("defaults write com.apple.finder CreateDesktop true")
	os.system("killall Finder")

def off():
	print('off')
	os.system("defaults write com.apple.finder CreateDesktop false")
	os.system("killall Finder")

if __name__ == "__main__":
	main()