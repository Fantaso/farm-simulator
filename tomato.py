from plant import Plant

class Tomato(Plant):

	'This is the class that represents the tomato, being a child of class Tomato():'

	######################################################## 														CLASS VARIABLES
	TOMATO_STAGES 	= ['Seedling','Growing','Flowering','Fruiting']
	tomatoRid		= 1
	TOMATO_VARIETY 	= 'Fruit'
	TOMATO_FAMILY 	= 'Tomato'
	######################################################## 														INTERNAL METHODS
	def __init__(self, tomatoName, tomatoPerPlant):
		# Plant.__init__(self, variety, family)	# the same as 'super().__init__(variety, family)'
		Plant.__init__(self, Tomato.TOMATO_VARIETY, Tomato.TOMATO_FAMILY, tomatoName)

		# VARIABLES IN CLASS Plum():
		self.size  			= 0
		self.weight 		= 0
		self.qty 			= tomatoPerPlant
		self.qtyFlag 		= False
		self._yield			= 0
		self.tomatoRid 		= Tomato.tomatoRid
		Tomato.tomatoRid	+= 1

		self.stage 			= Tomato.TOMATO_STAGES[0]
		self.stageIndex 	= 0
		self.eaten			= 0
		self.eatList 		= []
		self.drunk			= 0
		self.drinkList 		= []
		self.tanned			= 0
		self.tanList 		= []
		# self.grew			= 0

	def __str__(self):
		return 'Tomato() ID:{}/{}/{}/{}/{}/{}'.format(self.tomatoRid, self.name, self.family, self.variety, self.birthday, self.get_age())
	def __repr__(self):
		return "{}('{}',{})".format(self.__class__.__name__, self.name, self.qty)
	######################################################## 														VALIDATION METHODS


	######################################################## 														SETTER METHODS


	######################################################## 														GETTER METHODS OR PROCEDURES
	def get_tomato_stages(self):
		return Tomato.TOMATO_STAGES

	def get_weight(self):
		return self.weight

	def get_size(self):
		return self.size

	def get_qty(self):
		return self.qty

	def get_yield(self):
		try:
			if self.qtyFlag:
				# print('getyield from if')
				return ( self.weight * self.qty )
			else:
				# print('getyield from else')
				return self._yield
		except Exception as e:
			print(e)
		else:
			pass
		finally:
			pass
			# print('finnaly I function..')

	def get_qty_flag(self):
		return self.qtyFlag

	######################################################## 														SPECIAL METHODS

	def speak(self, msg = ''):
		# return (Plant.speak(self, ', more specifically a {} tomato {}'.format(self.name, msg)))
		return (super().speak(', more specifically a {} tomato {}'.format(self.name, msg)))

######################################################## 															TESTS
######################################################## 															TESTS
######################################################## 															TESTS
# t1 = Tomato('Cherry1','24')
# # print(t1)
# t2 = Tomato('Cherry2','24')
# t3 = Tomato('Cherry3','24')
# t4 = Tomato('Cherry4','24')
# t5 = Tomato('Cherry5','24')
# t6 = Tomato('Cherry6','24')
# t7 = Tomato('Cherry7','24')
# t8 = Tomato('Cherry8','24')
# t9 = Tomato('Cherry9','24')
# t0 = Tomato('Cherry0','24')

# tAll = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t0]

# for t in tAll:
	# print(str(t))


# print(t0.speak())

# print(Plant.speak(t0, 'self.name'))

# print(Plant.__bases__)