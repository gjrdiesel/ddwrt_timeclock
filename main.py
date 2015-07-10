import re,requests,json

class ReportManager:
	def __init__(self):
		self.POST_URL = "http://localhost"
		self.oParser = DDWRTInfoParser()
		clients = self.oParser.getClientCount()
		print "Found (",clients,") active clients, sending report...",
		response = self.sendReport()
		print "Sent!"
	def sendReport(self):
		# json.dumps(x.getClients())
		data = json.dumps(self.oParser.getClients())
		dataJson = {"data":data}
		post = requests.post(self.POST_URL,data=dataJson)
		return post.content

class DDWRTInfoParser:
	""" Parses router info page to find active clients to tattle on ;) """

	def __init__(self, bShowActiveOnly = True ):
		self.bShowActiveOnly = bShowActiveOnly
		self.Clients = {}
		self.USE_EXAMPLE_JSON = True

		ActivePattern= re.compile(ur'{active_wireless::(.*)}')
		DHCP_Pattern = re.compile(ur'{dhcp_leases::.*}')
		QuotePattern = re.compile(ur'\'([^\']*)\'')

		str = self.getRouterInfo()

		active = re.findall(ActivePattern, str)
		activeClients = re.findall(QuotePattern, active[0])
		activeClients = self.getActiveClientsInfo( activeClients )

		leases = re.findall(DHCP_Pattern, str)
		clientLeases = re.findall(QuotePattern, leases[0])
		clientLeases = self.getLeasesInfo( clientLeases, activeClients )
		self.Clients = clientLeases

	def getClientCount(self):
		return len(self.Clients)

	def getClients(self):
		return self.Clients

	def getRouterInfo(self):
		if self.USE_EXAMPLE_JSON:
			f = open('example.json','r')
			return f.read()
		else:
			r = requests.get("http://192.168.1.1/Info.live.htm")
			return r.contents

	def getLeasesInfo( self, matches, activeLeases ):
		count = 0
		clientNum=1
		clients = []
		while ( count < len(matches) ):
			count = count + 5
			info = {}
			info['id'] = matches[count-1]
			info['lease'] = matches[count-2]
			info['mac'] = matches[count-3]
			info['ip'] = matches[count-4]
			info['hostname'] = matches[count-5]
			info['active'] = False

			for x in activeLeases:
				if info['mac'] == x['mac']:
					info['active'] = True

			if self.bShowActiveOnly and info['active'] == False:
				"""Do nothing -_0 """
			else:
				clients.append(info)

		return clients

	def getActiveClientsInfo( self, matches ):
		count = 0
		clientNum=1
		clients = []
		while ( count < len(matches) ):
			count = count + 9
			info = {}
			info['mac'] = matches[count-9] # Could pull out more data, like signal strength, but not for now
			clients.append(info)
		return clients

oReport = ReportManager()
