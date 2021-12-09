inport os
def format(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)
	elif os.listdir(dir):
		print("directory is not empty")
		return
	os.chdir(os.path.join(os.getcwd(),dir)
	os.mkdirs("_9k")
	

def refresh(dir):
	blocks=os.listdir(dir)
	
