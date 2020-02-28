
#
#
#
#
#
#


import enum
import asyncio
import ipaddress

from aiosmb import logger
from aiosmb.commons.exceptions import *

from asysocks.client import SOCKSClient
from asysocks.common.comms import SocksQueueComms


class SocksProxyConnection:
	"""
	Generic asynchronous TCP socket class, nothing SMB related.
	Creates the connection and channels incoming/outgoing bytes via asynchonous queues.
	"""
	def __init__(self, target = None, socket = None):
		self.target = target
		self.socket = socket #for future, if we want a custom soscket
		
		self.client = None
		self.proxy_task = None

		self.out_queue = None#asyncio.Queue()
		self.in_queue = None#asyncio.Queue()
		
	async def disconnect(self):
		"""
		Disconnects from the socket.
		Stops the reader and writer streams.
		"""
		self.proxy_task.cancel()		
		
	async def connect(self):
		"""
		
		"""
		
		self.out_queue = asyncio.Queue()
		self.in_queue = asyncio.Queue()
		comms = SocksQueueComms(self.out_queue, self.in_queue)

		self.target.proxy.target.endpoint_ip = self.target.ip
		self.target.proxy.target.endpoint_port = int(self.target.port)

		print(str(self.target))
		print(str(self.target.proxy.target))
		
		self.client = SOCKSClient(comms, self.target.proxy.target, self.target.proxy.auth)
		self.proxy_task = asyncio.create_task(self.client.run())
		return

			

			


			