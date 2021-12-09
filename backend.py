inport os

ckass Filesystem:
	def __init__(self,folder):
		self.dir=folder
		self.folders=[]
		self.files=[]
		if not os.path.exists(self.dir):
			os.makedirs(self.dir)
		os.chdir(os.path.join(os.getcwd(),self.dir))
		if not len(os.listdir(os.getcwd())):
			self.index()
		#...
	
	def index(self):
		ls=os.listdir(os.getcwd())
		for discriptor in ls:
			if os.path.isdir():
				self.folders.append(Filesystem(discriptor))
			elif os.path.isfile(discriptor):
				self.files.append(discriptor)
			else:
				print("Unknown type:"+discriptor)
'''
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
	
'''
