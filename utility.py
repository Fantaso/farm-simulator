from datetime import date
from time import ctime


class Utility():

	@staticmethod
	def birthday_format(birthday = ''):
		day		= int(birthday.split('-')[0])
		month	= int(birthday.split('-')[1])
		year 	= int(birthday.split('-')[2])
		# print ( day, month, year )
		return date(year, month, day)


	@staticmethod
	def cm2_to_m2(cm2):
		oneMtSqr = 10000 # cm2
		return ( cm2 / oneMtSqr )
	@staticmethod
	def gr_to_kg(grams):
		oneKg = 1000 # grams
		return ( grams / oneKg )

	@staticmethod
	def plants_per_area():
		pass

class LandPlanner():
	"""docstring for LandPlanner"""
	def function():
		pass



	# TOMATO PLUM
	def plant_area(self, plantClassName):
		plantArea = plantClassName.STAGES_AREA
		return ( Utility.cm2_to_m2( plantArea[3] ** 2 ) ) # gets plant area from last stage in cm2 and converts it in m2
	def plant_density(self): # return number of plants per m2
		return ( 1 / self.plant_area() )
	def plant_qty_per_batch(self, area, prodBatches):
		return round( ( area * self.plant_density() ) / prodBatches )
	def plant_qty_per_total(self):
		return ( ( self.plant_qty_per_batch() * prodBatches ) )


	# ID
	def batch_id(self):
		return self.batchRid
	def batch_name(self):
		return self.batchPlantName
	# AGE
	def batch_age(self):
		plant = next ( iter( self.batch.keys() ) ) # gets object from first plant to get eveybone age. is the same
		return self.batch[plant].get_age() 			# from Plant():
	def batch_age_print(self):
		for plant in self.batch.keys():
			print( self.batch[plant].get_age() )	# from Plant():
	# YIELD
	def batch_yield(self):
		batchYield = 0
		for plant in self.batch.keys():
			batchYield += self.batch[plant].get_yield() # from Tomato(Plant):
		return Utility.gr_to_kg( batchYield )

	def yield_projected(self):
		fruitPerPlant = Plum.PLUM_QTY
		gramsPerFruit = Plum.PLUM_WEIGHT
		return Utility.gr_to_kg( ( self.plant_num_per_area() * fruitPerPlant * gramsPerFruit ) )
	def yield_current(self):
		return self.batch_yield()

	# DURATION
	def batch_duration(self):
		daysToMaturity = Plum.STAGES_DURATION
		return sum( daysToMaturity )
	def batch_duration_current(self):
		return self.batch_age() # From Farmer():
	def batch_duration_left(self):
		return ( self.batch_duration() - self.batch_duration_current() )
	def batch_area(self):
		return self.batchArea