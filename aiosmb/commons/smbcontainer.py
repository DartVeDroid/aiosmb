

class SMBShare:
	def __init__(self, name = None, type = None, remark = None, fullpath = None):
		self.fullpath = fullpath
		self.name = name
		self.type = type
		self.remark = remark
		self.flags = None
		self.capabilities = None
		self.maximal_access = None
		self.tree_id = None
		
		self.files = {}
		self.subdirs = {}
		
	def __str__(self):
		t = '===== SHARE =====\r\n'
		for k in self.__dict__:
			if isinstance(self.__dict__[k], list):
				for item in self.__dict__[k]:
					t += '%s : %s\r\n' % (k, item)
			elif isinstance(self.__dict__[k], dict):
				for ks in self.__dict__[k]:
					t += '%s : %s\r\n' % (ks, self.__dict__[k][ks])
			else:
				t += '%s : %s\r\n' % (k, self.__dict__[k])
		
		return t
		
class SMBDirectory:
	def __init__(self):
		self.parent_share = None
		self.fullpath = None
		self.parent_dir = None
		self.name = None
		self.creation_time = None
		self.last_access_time = None
		self.last_write_time = None
		self.change_time = None
		self.allocation_size = None
		self.attributes = None
		self.file_id = None
		self.sid = None
		
		self.files = {}
		self.subdirs = {}
		
	def __str__(self):
		t = '===== DIRECTORY =====\r\n'
		for k in self.__dict__:
			if k.startswith('parent_'):
				continue
			if isinstance(self.__dict__[k], list):
				for item in self.__dict__[k]:
					t += '%s : %s\r\n' % (k, item)
			elif isinstance(self.__dict__[k], dict):
				for ks in self.__dict__[k]:
					t += '%s : %s\r\n' % (ks, self.__dict__[k][ks])
			else:
				t += '%s : %s\r\n' % (k, self.__dict__[k])
		
		return t
		
class SMBFile:
	def __init__(self):
		self.parent_share = None
		self.parent_dir = None
		self.fullpath = None
		self.name = None
		self.size = None
		self.creation_time = None
		self.last_access_time = None
		self.last_write_time = None
		self.change_time = None
		self.allocation_size = None
		self.attributes = None
		self.file_id = None
		self.sid = None
		
	def __str__(self):
		t = '===== FILE =====\r\n'
		for k in self.__dict__:
			if k.startswith('parent_'):
				continue
			t += '%s : %s\r\n' % (k, self.__dict__[k])
		
		return t
		
class SMBUserSession:
	def __init__(self, username = None, ip_addr = None):
		self.username = username
		self.ip_addr = ip_addr
		
class SMBLocalGroup:
	def __init__(self, name = None, sid = None, members = {}):
		self.name = name
		self.sid = sid
		self.members = members
		
class SMBDomain:
	def __init__(self):
		self.name = None
		self.sid = None
		
class SMBHostInfo:
	def __init__(self):
		self.sessions = []
		self.domains = []
		self.groups = []
		self.shares = []