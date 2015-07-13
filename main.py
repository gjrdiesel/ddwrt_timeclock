import re,requests,json

class ExternalSettings:
	@staticmethod
	def get(setting):
		f = open('settings.json','r')
		file_string = f.read()
		oSettings = json.loads(file_string)
		return oSettings[setting]

class ReportManager:
	def __init__(self):
		self.POST_URL = ExternalSettings.get(setting="post_url")
		self.oParser = DDWRTInfoParser(bShowActiveOnly = False)
		clients = self.oParser.getClientCount()
		print "Found (",clients,") active clients, sending report..."
		response = self.sendReport()
		print response
		print "Sent!"
	def sendReport(self):
		data = json.dumps(self.oParser.getClients())
		dataJson = {"data":data}
		post = requests.post(self.POST_URL,data=dataJson)
		return post.content

class DDWRTInfoParser:
	""" Parses router info page to find active clients to tattle on ;) """

	def __init__(self, bShowActiveOnly = True ):
		self.bShowActiveOnly = bShowActiveOnly
		self.Clients = {}
		self.USE_EXAMPLE_JSON = ExternalSettings.get(setting="use_example_json")

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
			f = open( ExternalSettings.get(setting="example_file") ,'r')
			return f.read()
		else:
			router_ip = ExternalSettings.get(setting="router_ip")
			r = requests.get("http://"+router_ip+"/Info.live.htm")
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
