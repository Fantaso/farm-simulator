# from user 		import User
# from plum 		import Plum
from farmer 	import Farmer
# from report 	import Report



class Farm():
	
	farmRid 	= 1
	# cropRid 	= 1

	def __init__(self, farmName = 'HydroponicFarm', farmLocation = 'Venezuela'):
		self.farmName 		= farmName
		self.farmLocation 	= farmLocation
		self.farmer 		= Farmer()
		self.farmRid 		= Farm.farmRid
		Farm.farmRid 		+= 1

	def __str__(self):
		return 'i am a farm string'
	def __repr__(self):
		return "{}( '{}', '{}' )".format(self.__class__.__name__, self.farmName, self.farmLocation)

	def info(self):
		return 'FarmID:{} - FarmNAME: {} - FarmLocation: {}'.format(self.farmRid, self.farmName, self.farmLocation)




# farm1 = Farm('aq','ve')



