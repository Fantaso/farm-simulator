################################
# FIX
################################
'''
	- Birthday format
	- Validate inputs (family, variety, birthday, birthtime)
	- def get_all(): How to print all objects created here.
	- plantVarierties to tuple
'''
from time import ctime
from datetime import date

class Plant:

	'''This is the class Plant():, which is the parent of all classes related to any
	plant in the agricultural system'''

	######################################################## 														CLASS VARIABLES
	PLANT_VARIETIES 	= ['Fruit','Veggie','Legume','Grain']
	plantCounter 		= 0
	plantRid			= 1

	######################################################## 														INTERNAL METHODS
	def __init__(self, variety, family, name):
		self.age 			= 0
		self.name 			= name
		self.family 		= family
		self.variety 		= variety
		self.plantRid		= Plant.plantRid
		self.birthday		= date.today()# ctime()   # THIS IS NOT A STRING VARIABLE DUE TO date.today()
		self.birthtime 		= ctime().split(' ')[-2]
		Plant.plantCounter 	+= 1
		Plant.plantRid		+= 1
	
	def __str__(self):
		return 'Plant() ID:{}/{}/{}/{}'.format(self.plantRid, self.family, self.variety, self.birthday)
	
	def __repr__(self):
		return "{}('{}','{}','{}')".format(self.__class__.__name__, self.variety, self.family, self.name)

	######################################################## 														VALIDATION METHODS
	def validate_variety(self, variety):
		try:
			if variety == self.get_variety():
				print ('Plant OLD and NEW variety are the same!')
				return False
			elif variety in self.get_varieties():
				print ('Plant variety has been VALIDATED!')
				return True
			else:
				print ('Enter correct plant variety!!!')
				return False
		except:
			print ('Error VALIDATING self.variety : def validate_variety():')	

	######################################################## 														SETTER METHODS
	def set_family(self, family):
		self.family = family
		
	def set_variety(self, newVariety):
		if self.validate_variety(newVariety):	
			self.variety = newVariety
			print('Plant variety SUCCESSFULLY CHANGED!!')
		else:
			print ('Plant variety has NOT BEEN CHANGED!!')
	
	def set_birthday(self, year, month, day):
		# this should not be able to change
		self.birthday = date(year, month, day)

	######################################################## 														GETTER METHODS OR PROCEDURES
	def get_id(self):
		return 'V:{}/F:{}/N:{}'.format(self.plantRid, self.tomatoRid, self.plumRid)
	
	def get_plant_id(self):
		return self.plantRid
	
	def get_tomato_id(self):
		return self.tomatoRid
	
	def get_plum_id(self):
		return self.plumRid

	def get_name(self):
		return self.name

	def get_family(self):
		return self.family

	def get_variety(self):
		return self.variety

	def get_varieties(self):
		return Plant.PLANT_VARIETIES

	def get_birthday(self):
		return self.birthday

	def get_birthtime(self):
		return self.birthtime

	def get_full_birthday(self):
		return ' '.join([str(self.get_birthday()), self.get_birthtime()])

	# def get_age(self):
 #        # returns self's current age in days
	# 	if self.birthday == None:
	# 		raise ValueError
	# 	return (date.today() - self.birthday).days
	def get_age(self):
		return self.age
	def has_a_day_passed(self):
		pass
	

	def get_info(self):
		return '''			
		Name:			{5} 	Plant_ID:	{0}
		family: 		{4}		Name_ID: 	{2}
		Variety:		{3} 	Family_ID: 	{1}
		Full Birthday:	{6}
		Age:			{7}
		PlantAmount:	{8}
		Speak:			{9}
		'''.format(self.plantRid, self.tomatoRid, self.plumRid, self.variety, self.family, self.name, self.get_full_birthday(), self.get_age(), Plant.plantCounter, self.speak())
	def get_all():
		pass
	
	@staticmethod
	def get_amount():
		return Plant.plantCounter

	######################################################## 														SPECIAL METHODS
	def speak(self, msg = ''):
		return ('I am a {1} plant, from the family of {0} {2}'.format(self.get_family(), self.get_variety(), msg))
		# return ('I am a ' + self.family + ' ' + msg)
	
# VALIDATE DATA IN __init__ METHOD		
# if validate_variety(self, variety):	
# 	self.variety = variety
# else:
# 	print ('Plant variety has not been changed! "def __init__():')



######################################################## 															TESTS
######################################################## 															TESTS
######################################################## 															TESTS

def split(string):
	for str in string.split(' '):
		print (str)
#split(ctime())

def print_birthday():
	for p in pAll:
		print ((p.get_birthday()))
	print()

def print_full_birthday():
	for p in pAll:
		print ((p.get_full_birthday()))
	print()

def print_age():
	for p in pAll:
		print ((p.get_age()))
	print()

def print_birthtime():
	for p in pAll:
		print ((p.get_birthtime()))
	print()

def print_variety():
	for p in pAll:
		print ((p.get_variety()))
	print()

def print_object():
	for p in pAll:
		print ((p))
	print()

def print_speak():
	for p in pAll:
		print ((p.speak('Hi')))
	print()

def print_repr():
	for p in pAll:
		print (repr(p))
	print()

# p1 = Plant('Fruity','Tomato')
# p2 = Plant('Veggie','Lettuce')
# p3 = Plant('Legume','BlackBean')
# p4 = Plant('Grain','Corn')
# p5 = Plant('Fruit','Avocado')

# # p1 = Plant('F','Tomato')
# # p2 = Plant('V','Lettuce')
# # p3 = Plant('L','BlackBean')
# # p4 = Plant('G','Corn')
# # p5 = Plant('F','Avocado')

# pAll = [p1, p2, p3, p4, p5]


# print("\nPRINTING BIRTHDAYS")
# p1.set_birthday(2017,4,30)
# p2.set_birthday(2017,7,20)
# p3.set_birthday(2017,5,30)
# p4.set_birthday(2017,6,10)
# p5.set_birthday(2017,2,5)
# # print_birthday()

# print("\nPRINTING BIRTHTIMES")
# print_birthtime()

# print("\nPRINTING AGES")
# print_age()

# print("\nPRINTING FULL BIRTHDAYS")
# print_full_birthday()
# print(p2.get_full_birthday())
# print(type(p2.birthday))
# print(type(p2.birthtime))


# print("\nPRINTING VARIETIES")
# print_variety()
# p1.set_variety('Fruit')
# p2.set_variety('Veggie')
# p3.set_variety('Legume')
# p4.set_variety('Grain')
# p5.set_variety('Fruit')
# print_variety()

# print_speak()
# print(p3.get_info())
# print_object()
# print_repr()
# print(dir(p1))
# print(dir(p1.__module__))
# print()
# print(help(p1.__module__))
# print()