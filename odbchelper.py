from UserDict import UserDict
class FileInfo(UserDict):
	"""store file metadata"""
	def _init_(self,filename=None):
		UserDict._init_(self)
		self["name"]=filename


