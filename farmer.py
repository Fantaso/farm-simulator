from land import Land
from datetime import date
from time import ctime
from utility import Utility

class Farmer():
	''' This class creates a amount of plants to Farmer as a batch or groups of plants '''
	farmerLandRid 	= 0
	farmerRid 		= 1

	def __init__(self):
		self.farmerRid 		= Farmer.farmerRid
		Farmer.farmerRid 	+= 1
		self.lands  		= {}

	def __str__(self):
		return 'Farmer(Plum): {}/{}/{}/{}'.format(self.batchRid, self.batchPlantName, self.batchDate, self.batch)
	def __repr__(self):
		return '{}()'.format(self.__class__.__name__)

	# BEHAVIORS  
	def make_plan(self, landArea, plantName, productionBatches=1):
		pass

	def prepare_crop(self, landArea, plantName, productionBatches=1):
		land = { '{}'.format( plantName ): Land(landArea, plantName, productionBatches) for oneFarm in range( 1 ) } # reduce line with func
		self.lands.update(land)
		print( self.info() )
		print('\n\n')



	def land_info(self, land):
		return self.lands[land].info()
	def batch_info(self, land, batch):
		return self.lands[land].bacthes[batch].info()
	def info(self):
		return 'FarmerID:{} - LandLIST: {}'.format(self.farmerRid, self.list())
	def list(self):
		return list( self.lands.keys() )

	def get_land_list(self):
		return list( self.lands.keys() )
	def get_batch_list(self, landName):
		return self.lands[landName].list()
	def get_plant_list(self, landName, batchName):
		return self.lands[landName].batches[batchName].list()


	def land_data(self, cropName):
		landData = self.lands[cropName].batches_data()
		# print(landData)
		return landData

	# def get_batch_data_all(self):
	# 	batchesData = ()
	# 	for eachBatch in self.batches.keys():
	# 		batchesData += self.batches[eachBatch].report_data() 
	# 	return batchesData



	def sim_time(self, crop, qtyDays, mineralTag, mineralValue, water, hours):
		self.lands[crop].sim_land(qtyDays, mineralTag, mineralValue, water, hours)
	
	def calc_land_data(self, batchName):
		batchQty, plantAmountTotal, landArea, yieldBachesCurrent, yieldBachesProjected, cropName = 0,0,0,0,0,0
		for eachCrop in self.land_data(batchName):
			batchQty 				+= 1
			plantAmountTotal 		+= eachCrop['batchPlantAmount']
			landArea 				+= eachCrop['batchArea']
			yieldBachesCurrent 		+= eachCrop['batchYieldNow']
			yieldBachesProjected 	+= eachCrop['batchYieldProjected']
			cropName 				 = eachCrop['batchName']
		reportHead = dict( batchQty=batchQty, cropName=cropName, yieldBachesProjected=round(yieldBachesProjected,2), plantAmountTotal=plantAmountTotal, landArea=landArea , yieldBachesCurrent=round(yieldBachesCurrent,2) )
		print(reportHead)
		return reportHead

	def report(self, batchName):
		landData = self.land_data(batchName)
		reportHead = self.calc_land_data(batchName) # give data from all batches to compute land yields etc.
		print(self.report_head(**reportHead))
		for eachBatch in self.land_data(batchName):
			print(self.report_body(**eachBatch))
			print()

	def report_head(self, cropName, plantAmountTotal, landArea, batchQty, yieldBachesCurrent, yieldBachesProjected):
		return '''
				############################################################
										CROP REPORT
				############################################################
				
				{0} 								
				{1} plants 							YIELD 
				{2} m2 								Current: 	{4} kg
				{3} Batches							Projected: 	{5} kg
													
				'''.format(cropName,plantAmountTotal,landArea,batchQty,yieldBachesCurrent,yieldBachesProjected)

	def report_body(self, batchId, batchName, batchPlantAmount, batchArea, plantDensity, batchDaysHaverst, batchDaysGrowing, batchDaysCycle, batchYieldNow, batchYieldProjected):
		return '''
				####################
					BATCH REPORT
				####################
					Batch ID {0}

					{1}	 								TIME									YIELD 			
					{2} plants								{5} days to harvest						{8} kg of current yield
					Area of {3} m2							{6} days of current cultivation			{9} kg of projected yield
					Plant density of {4} m2				{7} days of cultivation
				'''.format(		batchId,
								batchName,
								batchPlantAmount,
								batchArea,
								plantDensity,
								batchDaysHaverst,
								batchDaysGrowing,
								batchDaysCycle,
								batchYieldNow,
								batchYieldProjected
							)

# feedData = {
# 				'qtyDays' 		: 110,
# 				'mineralTag' 	: 'Mg',
# 				'mineralValue' 	: 3,
# 				'water' 		: 250,
# 				'hours' 		: 10,
# 			}

# TEST 1
# farmer1 = Farmer()
# farmer2 = Farmer()
# farmer3 = Farmer()
# farmer4 = Farmer()

# farmer1.prepare_crop(3, 'Cherry', 6)
# print()
# farmer3.prepare_crop(2, 'Pl', 3)
# print()
# farmer2.prepare_crop(2, 'Pl', 2)
# print()
# farmer4.prepare_crop(2, 'Pl', 2)
# print()
# farmer1.sim_time('Cherry',**feedData)
# print('\nLandLIST')
# print( farmer1.get_land_list() )
# print('\nbatchLIST')
# print( farmer1.get_batch_list('Cherry') )
# print('\nplantLIST')
# print( farmer1.get_plant_list('Cherry', 'Cherry1') )
# print('\nplantLIST')
# print( farmer1.get_plant_list('Cherry', 'Cherry2') )
# loco = farmer1.lands['Cherry'].list()
# # loco1 = farmer1.lands['Cherry'].batches['Cherry0'].batch
# loco2 = farmer1.lands['Cherry'].batches['Cherry1'].list()
# print(loco)
# # print(loco1)
# print(loco2)


# print('\n\n')
# print('LAND DATA')
# # for eachBatch in farmer1.land_data('Cherry'):
# # 	print('\nBATCH DATA')
# # 	print((eachBatch))
# # print( farmer1.land_data('Cherry') )

# farmer1.report('Cherry')



# TEST 2
# farmer1 = Farmer('Plum',10)
# farmer1.make_batch()
# print(farmer1.batch)
# farmer1.age_batch(170)
# print()
# print('START GROWING')
# days = 70
# for i in range(days):
# 	farmer1.grow_batch()
# print ('growing for {} days'.format(days))
# print('STOP GROWING..\n')
# print('batch_id')
# print(farmer1.batch_id())
# print(farmer1.yield_projected())
# # print('')
# # print('batch_age')
# print(farmer1.batch_age())
# print('')
# print('batch_fruiting')
# print(farmer1.batch_fruiting())
# print('')
# print('batch_yield')
# print(farmer1.batch_yield())
# print('')
# print('yield_projected')
# print(farmer1.yield_projected())
# print('')
# print('yield_current')
# print(farmer1.yield_current())
# print('')
# print('batch_duration')
# print(farmer1.batch_duration())
# print('')
# print('batch_duration_current')
# print(farmer1.batch_duration_current())
# print('')
# print('batch_duration_left')
# print(farmer1.batch_duration_left())
# print('')
# # print('make_batch')
# # print(farmer1.make_batch())
# # print('')
# print('grow_batch')
# print(farmer1.grow_batch())
# print('')
# print('age_batch')
# print(farmer1.age_batch(days = 0))
# print('')
# print('batch_fruiting')
# print(farmer1.batch_fruiting())
# print('')
# print('plant_area')
# print(farmer1.plant_area())
# print('')
# print('plant_density')
# print(farmer1.plant_density())
# print('')
# print('plant_num_per_area')
# print(farmer1.plant_num_per_area())
# print('')
