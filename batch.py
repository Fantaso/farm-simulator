################################################################
################################################################
################################################################
'''
A batch:
	1- age and grows based on a event (datetime.date)

'''
################################################################
################################################################
################################################################

from plum import Plum
from datetime import date
from time import ctime
from utility import Utility

class Batch():
	''' This class creates a amount of plants to Batch as a batch or groups of plants '''

	PLANT_CLASS_DB 	= {'Plum': Plum()}
	batchRid 		= 1

	def __init__(self, plantName, plantQty, batchArea): #batchAR
		self.plantQty 		= plantQty
		self.batchPlantName = plantName
		self.batch 			= {}
		self.batchArea 		= batchArea
		self.batchDate 		= date.today()
		self.batchTime 		= ctime().split(' ')[-2]
		self.batchRid 		= Batch.batchRid
		Batch.batchRid 		+= 1
		self.batch_new()

	def __str__(self):
		return 'Batch(Plum): {}/{}/{}/{}'.format(self.batchRid, self.batchPlantName, self.batchDate, self.batch)
	def __repr__(self):
		return "{}('{}',{})".format(self.__class__.__name__, self.batchPlantName, self.batchArea)

	# BEHAVIORS
	def batch_new(self):
		self.batch = { 'plum{}'.format( plantNum ): Plum() for plantNum in range( 1, 1 + self.plantQty ) } # reduce line with func
		print( self.info() )

	def info(self):
		return 'BatchID:{} - #Plants:{} - BatchLIST: {}'.format( self.rid(), self.plantQty, self.list() )
	def list(self):
		return list( self.batch.keys() )
	def rid(self):
		return self.batchRid
	
	def sim_batch(self, qtyDays, mineralTag, mineralValue, water, hours):
		for plant in self.batch.keys():
			for eachDay in range(qtyDays):
				self.batch[plant].grow_cycle(mineralTag, mineralValue, water, hours)
	
	def report_data(self):
		return ({
					'batchId'				: self.batch_id(),
					'batchName'				: self.batch_name(),
					'batchPlantAmount'		: self.plant_per_batch(),
					'batchArea'				: round( self.batch_area(), 2 ),
					'plantDensity'			: round( self.plant_density(), 2 ),
					'batchDaysHaverst'		: self.batch_duration_left(),
					'batchDaysGrowing'		: self.batch_duration_current(),
					'batchDaysCycle'		: self.batch_duration(),
					'batchYieldNow'			: round( self.batch_yield_current(), 2 ),
					'batchYieldProjected'	: round( self.batch_yield_projected(), 2 )
		},)


	def report(self):
		return '''
				####################
					BATCH REPORT
				####################
					Batch ID {0}

					{1}	 								TIME									YIELD 			
					{2} plants								{5} days to harvest						{8} kg of current yield
					Area of {3} m2							{6} days of current cultivation			{9} kg of projected yield
					Plant density of {4} m2				{7} days of cultivation
				'''.format(	
					self.batch_id(),
					self.batch_name(),
					self.plant_per_batch(),
					self.batch_area(),
					round( self.plant_density(), 2 ),
					self.batch_duration_left(),
					self.batch_duration_current(),
					self.batch_duration(),
					round( self.batch_yield_current(), 2 ),
					round( self.batch_yield_projected(), 2 )
					)

###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
	# PLANT
	def plant_area(self):
		plantArea = Plum.STAGES_AREA
		return ( Utility.cm2_to_m2( plantArea[3] ** 2 ) ) # gets plant area in cm2 
	def plant_density(self): # return number of plants per m2
		return ( 1 / self.plant_area() )
	def plant_per_batch(self):
		return self.plantQty
	# ID
	def batch_id(self):
		return self.batchRid
	def batch_name(self):
		return self.batchPlantName
	def batch_area(self):
		return self.batchArea
	# AGE
	def batch_age(self):
		plant = next ( iter( self.batch.keys() ) ) # gets object from first plant to get eveybone age. is the same
		return self.batch[plant].get_age() 			# from Plant():
	def batch_age_print(self):
		for plant in self.batch.keys():
			print( self.batch[plant].get_age() )	# from Plant():
	# YIELD
	def batch_yield_current(self):
		batchYield = 0
		for plant in self.batch.keys():
			batchYield += self.batch[plant].get_yield() # from Tomato(Plant):
		return Utility.gr_to_kg( batchYield )
	def batch_yield_projected(self):
		fruitPerPlant = Plum.PLUM_QTY
		gramsPerFruit = Plum.PLUM_WEIGHT
		return Utility.gr_to_kg( ( self.plant_per_batch() * fruitPerPlant * gramsPerFruit ) )
	# DURATION
	def batch_duration(self):
		daysToMaturity = Plum.STAGES_DURATION
		return sum( daysToMaturity )
	def batch_duration_current(self):
		return self.batch_age() # From Farmer():
	def batch_duration_left(self):
		return ( self.batch_duration() - self.batch_duration_current() )



# feedData = {
# 				'qtyDays' 		: 180,
# 				'mineralTag' 	: 'Mg',
# 				'mineralValue' 	: 9,
# 				'water' 		: 250,
# 				'hours' 		: 13,
# 			}




# TEST
# batch_1 = Batch( 'Plum', 2, 12 )
# batch_2 = Batch( 'Plum', 4, 12 )
# batch_3 = Batch( 'Plum', 6, 12 )
# batch_4 = Batch( 'Plum', 8, 12 )
# def test():
# 	batch_1.sim_batch(**feedData)
# 	print( batch_1.batch_duration() )
# 	print( batch_1.report() )


# test()



# # TEST 1
# batch1 = Batch('Plum',1)
# batch1.batch_new()
# batch1.sim_cultivation_less(**feedData)



# # # TEST 2
# # batch1 = Batch('Plum',10)
# # batch1.batch_new()
# # print(batch1.batch)
# # batch1.age_batch(170)
# # print()
# # print('START GROWING')
# # days = 70
# # for i in range(days):
# # 	batch1.grow_batch()
# # print ('growing for {} days'.format(days))
# # print('STOP GROWING..\n')
# # print('batch_id')
# # print(batch1.batch_id())
# # print(batch1.batch_yield_projected())
# # print('')
# # print('batch_age')
# print(batch1.batch_age())
# print('')
# # print('batch_fruiting')
# # print(batch1.batch_fruiting())
# print('')
# print('batch_yield')
# print(batch1.batch_yield())
# print('')
# print('batch_yield_projected')
# print(batch1.batch_yield_projected())
# print('')
# print('batch_yield_current')
# print(batch1.batch_yield_current())
# print('')
# print('batch_duration')
# print(batch1.batch_duration())
# print('')
# print('batch_duration_current')
# print(batch1.batch_duration_current())
# print('')
# print('batch_duration_left')
# print(batch1.batch_duration_left())
# print('')
# # print('batch_new')
# # print(batch1.batch_new())
# # print('')
# print('grow_batch')
# print(batch1.grow_batch())
# print('')
# print('age_batch')
# print(batch1.age_batch(days = 0))
# print('')
# print('batch_fruiting')
# print(batch1.batch_fruiting())
# print('')
# print('plant_area')
# print(batch1.plant_area())
# print('')
# print('plant_density')
# print(batch1.plant_density())
# print('')
# print('plant_num_per_area')
# print(batch1.plant_num_per_area())
# print('')
