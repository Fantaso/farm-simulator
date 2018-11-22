# from plant import Plant
from tomato import Tomato
# from cultivate import Cultivate

class Plum(Tomato):
    
	"""A tomato grown by the farmer"""

	######################################################## 														CLASS VARIABLES    
	# Plum Tomato ID
	plumRid		= 1
	# Plum Tomato Characteristics
	PLUM_NAME 		= 'Plum'
	PLUM_SIZE 		= 80													# Size of the product of the plant in milimeters
	PLUM_WEIGHT		= 62													# Weigh of product of the plant in grams
	PLUM_QTY		= 46													# Quantity of products (fruits...) derive from plant per plamt
	# PLUM_DENSITY	= 4.94

	STAGES_DURATION = [10, 90, 35, 45]		# Duration per each stage of plant growing in days
	STAGES_AREA		= [10, 30, 45, 45]		# Physical space required by the plant for growth in centimeters


	# Inputs required by the plant for a heatlhy lifespan
	STAGES_WATER		= [100, 200, 300, 350]	# Amount of water needed for plant growth in mililiters

	STAGES_FOOD			= {	'K':(4, 6, 9.5, 13),
							'N':(5, 3, 6, 11),
							'Ca':(3, 3, 4, 5),
							'P':(2, 2.5, 3, 4),
							'Mg':(2, 2.5, 3, 3)
							}	# Minerals in grams required by tomato for growth. Nitrogen, Phosphorous, Kpotasium, Calcium, Mgnesium
	
	STAGES_RADIATION	= [14, 13, 12, 10]	# 1st. HOURS/DAY 2nd. Amount of sun irradiation required by plant for growth in kw/m2

	######################################################## 														INTERNAL METHODS
	def __init__(self):
		Tomato.__init__(self, Plum.PLUM_NAME, Plum.PLUM_QTY)
		self.plumRid 	= Plum.plumRid
		Plum.plumRid	+= 1

	def __str__(self):
		return 'Plum(class) ID:{}/{}/{}/{}/{}/{}/{}/{}'.format(self.plantRid, self.tomatoRid, self.plumRid, self.name, self.family, self.variety, self.birthday, self.get_age())

	def __repr__(self):
		return "{}()".format(self.__class__.__name__)
	######################################################## 														VALIDATION METHODS

	def grow_cycle(self, mineralTag, mineralValue, water, hours):
		print( 'PLANT STAGE: {} Num: {}'.format( self.stage, self.stageIndex ) )
		print( 'PLANT AGE: {}'.format(self.age))
		self.agex()

		self.plant_condition_checker()
		
		self.eaten 	= self.eat(mineralTag, mineralValue)
		self.drunk  = self.drink(water)
		self.tanned	= self.tan(hours)

		print( 'FACTORS: {} {} {}'.format( round(self.eaten,2), round(self.drunk,2), round(self.tanned,2) ) )

		self.grow( self.eaten, self.drunk, self.tanned )
		self.already_fruiting()

		# save data into DB and the reset_var()
		self.plant_reset_var()
		print( 'FACTORS: {} {} {}'.format( self.eaten, self.drunk, self.tanned ) )
		print('\n')
	
	def agex(self, qtyDays = 1): # makes the tomato age x days
		self.age += qtyDays
		return self.age

	def plant_condition_checker(self):
		try:
			if 		( self.get_age() <= Plum.STAGES_DURATION[0] ):
				self.stageIndex, self.stage = self.get_stage()
			elif 	( self.get_age() <= sum(i for i in Plum.STAGES_DURATION[:2]) ):
				self.stageIndex, self.stage = self.get_stage()
			elif 	( self.get_age() <= sum(i for i in Plum.STAGES_DURATION[:3]) ):
				self.stageIndex, self.stage = self.get_stage()
			elif 	( self.get_age() <= sum(i for i in Plum.STAGES_DURATION) ):
				self.stageIndex, self.stage = self.get_stage()
			else:
				return 'plant condition checker!!'
		except Exception as e:
			print('plant_condition_checker() ERROR: {}'.format(e))
		
	def eat(self, mineralTag, mineralValue):
		# print( type( self.stageIndex ) )
		mineralRequired = Plum.STAGES_FOOD.get(mineralTag)[self.stageIndex]
		print('MineralRequired: {} of {} given {}'.format(mineralRequired, mineralTag, mineralValue))
		self.eatList.append(mineralValue)
		return ( mineralValue / mineralRequired )

	def drink(self, water):
		waterRequired = Plum.STAGES_WATER[self.stageIndex]
		self.drinkList.append(water)
		print('WaterRequired: {} given {}'.format(waterRequired, water))
		return ( water / waterRequired )

	def tan(self, hours):
		hoursRequired = Plum.STAGES_RADIATION[self.stageIndex]
		print('hoursRequired: {} given {}'.format(hoursRequired, hours))
		self.tanList.append(hours)
		return ( hours / hoursRequired )
	
	def grow(self, eatFactor, drinkFactor, tanFactor):
		# when growing. the plant its self dones grow here. only the fruit
		growthFactor = eatFactor * drinkFactor * tanFactor
		print('GrowthFactor: {}'.format(round(growthFactor,2)))
		try:	
		 	if self.get_age() > sum( i for i in Plum.STAGES_DURATION[:2] ): 	# Checks when is from stage 3 and on, since there is when the tomato starts growi
		 		if not self.get_age() > sum( i for i in Plum.STAGES_DURATION ):			# Checks is the tomato has reach all its 4 stages, since it can not grow anymore
			 	 	# print('Weight:  {} Size:  {}'.format(self.weight, self.size))
			 	 	weightRatePerDay = ( Plum.PLUM_WEIGHT 	/ sum(i for i in Plum.STAGES_DURATION[2:]) )
			 	 	growthRatePerDay = ( Plum.PLUM_SIZE		/ sum(i for i in Plum.STAGES_DURATION[2:]) )
			 	 	self.weight 	+= ( weightRatePerDay * growthFactor )
			 	 	self.size 		+= ( growthRatePerDay * growthFactor )
			 	 	print('WeightR: {} SizeR: {}'.format(round(weightRatePerDay,2), round(growthRatePerDay,2)))
			 	 	print('Weight:  {} Size:  {}'.format(round(self.weight,2), round(self.size,2)))
			 	else:
			 		pass
			 		# print( 'CAN NOT GROW ANY MORE' )
		 	else:
		 		pass
		 		# print ( 'It has not past {} days'.format( sum (i for i in Plum.STAGES_DURATION[:2])) )	
		 		# raise ('go')
		except Exception as e:
			print(e, '--GROW ERROR')
		finally:
			return ('Weight:  {} Size:  {}'.format(self.weight, self.size))
	
	def plant_reset_var(self):
		self.eaten = 0
		self.drunk = 0
		self.tanned = 0

	def get_stage(self): #returns stage and stage index
		try:
			if 		( self.get_age() <= Plum.STAGES_DURATION[0] ):
				return 0, self.get_tomato_stages()[0]
			elif 	( self.get_age() <= sum(i for i in Plum.STAGES_DURATION[:2]) ):
				return 1, self.get_tomato_stages()[1]
			elif 	( self.get_age() <= sum(i for i in Plum.STAGES_DURATION[:3]) ):
				return 2, self.get_tomato_stages()[2]
			elif 	( self.get_age() <= sum(i for i in Plum.STAGES_DURATION) ):
				return 3, self.get_tomato_stages()[3]
			else:
				return 'Must be HARVESTED NOW!!'
		except Exception as e:
			print('get_stage() ERROR: {}'.format(e))
		else:
			pass
		finally:
			pass

	
	######################################################## 														SETTER METHODS


	######################################################## 														GETTER METHODS OR PROCEDURES
	

	######################################################## 														SPECIAL METHODS
	def already_fruiting(self):
		try:
			if not self.qtyFlag:
				if 		( self.get_age() > sum( i for i in Plum.STAGES_DURATION ) ):			# Checks is the tomato has reach all its 4 stages, since it can not grow anymore
					print('You must be harvested ALREADY!')
				elif 	( self.get_age() > sum( i for i in Plum.STAGES_DURATION[:2] ) ): 	# Checks when is from stage 3 and on, since there is when the tomato starts growi
					self.qtyFlag = True
					return self.qtyFlag
				else:
					self.qtyFlag = False
					return self.qtyFlag
			else:
				return self.qtyFlag
		except Exception as e:
			print(e)
	
	

	def speak(self, msg = ''):
		# return (Plant.speak(self, ', more specifically a {} tomato {}'.format(self.name, msg)))
		return (super().speak(', a very delicious {} tomato {}'.format(self.name, msg)))
	# def fruity_type(self):
	# 	""""Return a string representing the type of vehicle this is."""
	# 	return '''	{},{},{},{},{},
	# 				{},{},{},{},{},
	# 				{},{},{},{},{},
	# 				{},{},{},{},{},
	# 				{},{},{}       
 #        		'''.format(
 #        					# Plant characteristics
 #        					self.size,
 #        					self.weight,
	# 					    self.qty,    
	# 					    self.stage1, self.stage2, self.stage3, self.stage4,
	# 					  	self.space1, self.space2, self.space3, self.space4,
	# 					  	# Inputs required by the plant for a heatlhy lifespan
	# 						self.water1, self.water2, self.water3, self.water4,
	# 					  	self.food1, self.food2, self.food3, self.food4,
	# 					  	self.radiation1, self.radiation2, self.radiation3, self.radiation4
 #        					)

######################################################## 															TESTS
######################################################## 															TESTS
######################################################## 															TESTS

# plumData = {
# 				'mineralTag' 	: 'N',
# 				'mineralValue' 	: 4.5,
# 				'water' 		: 95,
# 				'hours' 		: 13,
# 			}

# t1 = Plum()
# print (t1)
# # t2 = Plum()
# # t1.eat('K', 1)
# t1.eat('N', 2)
# # t1.eat('Ca', 2)
# # t1.eat('P', 2)
# # t1.eat('Mg', 3)
# print(plumData)
# t1.grow_cycle(**plumData)

# print(t1.stageIndex)
# print(type(t1.stageIndex))
# print(t1.stage)
# print(type(t1.stage))