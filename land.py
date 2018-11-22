from plum import Plum
from utility import Utility
from batch import Batch
from math import ceil

class Land():
	'''This is the land where the plants are cultivated:
	Each land has: Pump, Agrimodule, Sensors and Batches of plants'''

	landRid = 1

	def __init__(self, landArea, plantName, productionBatches = 1):
		self.area  				= landArea
		self.plantName 			= plantName
		self.prodBatches		= productionBatches
		self.batches  			= {}
		self.plantQtyPerBatch 	= self.plant_qty_per_batch()
		self.landRid 			= Land.landRid
		Land.landRid 			+= 1
		# Soil plants input containers
		self.soilWater 			= []
		self.soilNutrients 		= {}
		# Soil sensors containers
		self.soilpH 			= []
		self.soilHumidity 		= []
		self.soilTemperature 	= []

		self.batch_decision()

	def __str__(self):
		return 'Land(Batch): {}/{}/{}/{}'.format(self.landRid, self.plantName, self.area, self.prodBatches)
	def __repr__(self):
		return "{}({},'{}',{})".format(self.__class__.__name__, self.area, self.plantName, self.prodBatches)


	def batch_decision(self):
		if self.prodBatches == 1:
			self.batch_make( self.plant_qty_per_batch(), self.prodBatches, self.batch_area() )
		else:
			stagnatedPlantQty = self.plant_qty_per_batch() # call function to determine quantity of plants
			self.batch_make( stagnatedPlantQty, self.prodBatches, self.batch_area() )

	def batch_make(self, plantAmount, batchQty, batchArea):
		batch = { '{}{}'.format( self.plantName, batchNum ): Batch( self.plantName, plantAmount, batchArea ) for batchNum in range( 1,(batchQty + 1) ) }
		self.batches.update(batch)
		print( self.info() )

	def info(self):
		return '\nLandID:{} - AREA: {} - BATCHES#: {} - TotalPlants: {} - Crop: {}'.format(self.landRid, self.area, self.prodBatches, self.plant_qty_per_total(), self.plantName)
	def list(self):
		return list( self.batches.keys() )
	def rid(self):
		return self.landRid
	def sim_land(self, qtyDays, mineralTag, mineralValue, water, hours):
		for eachBatch in self.list():
			self.batches[eachBatch].sim_batch(qtyDays, mineralTag, mineralValue, water, hours)
########################################################################################
########################################################################################
	# THIS CODE SHOULD GO TO BATCH.py
	# TOMATO PLUM
	def plant_area(self):
		plantArea = Plum.STAGES_AREA
		return ( Utility.cm2_to_m2( plantArea[3] ** 2 ) ) # gets plant area in cm2 
	def plant_density(self): # return number of plants per m2
		print (self.plant_area())
		return ( 1 / self.plant_area() )
	def plant_qty_per_batch(self):
		return round( ( self.area * self.plant_density() ) / self.prodBatches )
	def plant_qty_per_total(self):
		return ( ( self.plant_qty_per_batch() * self.prodBatches ) )
########################################################################################
	def land_id(self):
		return self.landRid
	def batch_area(self):
		return ( (self.area / self.prodBatches) )
	
	def batch_data(self, batchName):
		batchData = self.batches[batchName].report_data()
		return batchData

	def batches_data(self):
		batchesData = ()
		for eachBatch in self.batches.keys():
			batchesData += self.batches[eachBatch].report_data() 
		return batchesData

	# def batches_data_unpack(self, batchesData):
	# 	for eachBatch in batchesData:
	# 		print('\nBATCH DATA')
	# 		print(type(eachBatch))


# feedData = {
# 				'qtyDays' 		: 110,
# 				'mineralTag' 	: 'Mg',
# 				'mineralValue' 	: 3,
# 				'water' 		: 250,
# 				'hours' 		: 10,
# 			}

###### TEST
# print('\nLAND1')
# land = Land(10, 'Plum', 5)
# land.sim_land(**feedData)
# print( land.list() )
# print( land.batch_data('Plum1') )
# print( land.batches_data() )

# print('\nLAND2')
# land2 = Land(20, 'Plum2', 2)
# print('\nLAND3')
# land3 = Land(20, 'Plum3', 4)
# print('\nLAND4')
# land4 = Land(10, 'Plum4', 5)
# land1.report('')



