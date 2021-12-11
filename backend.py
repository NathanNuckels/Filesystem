import os

class Filesystem:
	def __init__(self,folder,disp=True,root=True):
		self.dir=folder
		self.displayDir=folder
		self.folders=[]
		self.files=[]
		self.subSystems=[]
		self.root=root
		if not os.path.exists(self.dir):
			os.makedirs(self.dir)
		os.chdir(os.path.join(os.getcwd(),self.dir))
		if len(os.listdir(os.getcwd()))==0:
			self.index()
		if disp:
			print("[FS] ["+self.dir+"] Created")
		
		
	def index(self,recursive=True):
		print("[FS] ["+self.dir+"] Indexing...")
		ls=os.listdir(os.getcwd())
		for discriptor in ls:
			if os.path.isdir():
				self.folders.append(Filesystem(discriptor))
				self.subSystems.append(Filesystem(discriptor,False))
				self.subSystems[len(self.subSystems)-1].displayDir = self.dir + "/" + self.subSystems[len(self.subSystems)-1].dir
				print("[FS] ["+self.dir+"/"+discriptor+"] Created")
				self.subSystems[len(self.Subsystems)-1].index()
			elif os.path.isfile(discriptor):
				self.files.append(discriptor)
			else:
				print("[FS] Unknown type:"+discriptor)
	def generateKey(self):
		pass
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
fs=Filesystem("testFolder")
fs.index()
