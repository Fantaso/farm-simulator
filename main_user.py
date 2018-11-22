################################################################
################################################################
################################################################
'''
A farm has:
	1- Farmer
	2- Manager
	3- Storage 	[ Seed, Fertilizer, Water ]
	4- Pump
	5- Agrimodule
	6- Sensors 	[ Radiation, pH,
				[ EC, Nutrients, K, N, Ca, P, Mg ], 
				[ Air, Temperature, Humidity ],
				[ Soil, Temperature, Humidity ] ]

	1. checks 3.storage, to give alerts and to see if tasks being handed are possible
	1. checks 5.agrimodule to fertigate efficiently
	2. ask 1.farmer for information to prepare reports for user
	2. checks agrimodule to prepera reports
	4. consumes water from 3.storage
	4. consumes energy from
	5. checks 6.sensors to irrigate efficiently
	5. turns on and off the 4.pump
	5. checks 3.water storage to give alerts if low rosource

'''
################################################################
################################################################
################################################################


from random import randint
from datetime import date
from time import ctime
from user_settings import UserSettings

from plant import Plant
from farm import Farm

class User(UserSettings):
	
	def __init__(self, name, location, email, birthday, mobile, emailRecovery):
		UserSettings.__init__(self, name, location, email, birthday, mobile, emailRecovery)
		self.farms		= {}
		self.farmRid 	= 1

	def __str__(self):
		return 'USER.ID {}	NAME {}'.format( self.userRid, self.username )
	def __repr__(self):
		return "{}( '{}', '{}', '{}', '{}', '{}', '{}' )".format(self.__class__.__name__, self.username, self.userLocation, self.userEmail, self.userBirthday, self.userMobile, self.userEmailRecovery)


	def farm_new(self, farmName, farmLocation):
		farm = { '{}'.format( farmName ): Farm( farmName, farmLocation ) for oneFarm in range( 1 ) }
		self.farms.update(farm)
		# print( self.info() )
	
	def info(self):
		return 'UserID:{} - Name:{} - UserLocation: {}'.format(self.userRid, self.username, self.userLocation)
	
	def get_farm_list(self):
		return list( self.farms.keys() )
	def farm_report(self, farmName):
		pass
	def crop_report(self, farmName, cropName):
		pass
	
	

####################################################################
####################################################################
####################################################################
####################################################################
#							 TESTS
####################################################################
####################################################################
####################################################################

#						GENERAL DATA
####################################################################
userData1 = {
				'name'			: 'Carlos',
				'location'		: 'Venezuela',
				'email'			: 'email1@hotmail.com',
				'birthday'		: '27-02-1986',
				'mobile'		: '+4917643503684',
				'emailRecovery'		: 'email2@gmail.com',
			}
userData2 = {
				'name'			: 'Viktor',
				'location'		: 'France',
				'email'			: 'viktoriano@hotmail.com',
				'birthday'		: '17-01-1988',
				'mobile'		: '+491764300000',
				'emailRecovery'		: 'Recovery@gmail.com',
			}
userData3 = {
				'name'			: 'Oscar',
				'location'		: 'Mexico',
				'email'			: 'email@hotmail.com',
				'birthday'		: '11-10-1986',
				'mobile'		: '+4917611111111',
				'emailRecovery'		: 'recovery2@gmail.com',
			}

simData = {
				'qtyDays' 		: 180,
				'mineralTag' 		: 'Mg',
				'mineralValue' 		: 3,
				'water' 		: 250,
				'hours' 		: 10,
			}
####################################################################
####################################################################
####################################################################
####################################################################
			# NEW USER
			# CARLOS
####################################################################
####################################################################
####################################################################

# CREATING USER NAMED "carlos"
####################################################################
print('CREATING USER CARLOS:')
carlos = User(**userData1)
print( repr(carlos) )
print( carlos )
print( carlos.user_report() )



# CREATING FARM NAMED "AQUAPONIC"
####################################################################
print('\nCREATING FARM AQUAPONIC:')
carlos.farm_new('AQUAPONIC', 'Indonesia')
print(carlos.farms['AQUAPONIC'].info())

print('\nPRINTING A FARM AQ OBJECTS\n')
(carlos.farms['AQUAPONIC'].farmer.prepare_crop( 10,	'Plum', 5))
# (carlos.farms['AQUAPONIC'].farmer.prepare_crop( 1,	'Cherry', 1))
# (carlos.farms['AQUAPONIC'].farmer.prepare_crop( 0.5,'Parchita',	  2))

print('\nSIMULATING TIME - AQUAPONIC/CROPS:')
(carlos.farms['AQUAPONIC'].farmer.sim_time('Plum',**simData))
# (carlos.farms['AQUAPONIC'].farmer.sim_time('Cherry',**simData))
# (carlos.farms['AQUAPONIC'].farmer.sim_time('Parchita',**simData))
print('\n\n')



# CREATING FARM NAMED "HYDROPONIC"
####################################################################

# print('\nCREATING FARM HYDROPONIC:')
# carlos.farm_new('HYDROPONIC', 'India')
# print(carlos.farms['HYDROPONIC'].info())

# (carlos.farms['HYDROPONIC'].farmer.prepare_crop( 10, 'Chayota', 1))
# (carlos.farms['HYDROPONIC'].farmer.prepare_crop( 10, 'Peyote', 2))

# print('\nSIMULATING TIME - HYDROPONIC/CROPS:')
# (carlos.farms['HYDROPONIC'].farmer.sim_time('Chayota',**simData))
# (carlos.farms['HYDROPONIC'].farmer.sim_time('Peyote',**simData))
# print('\n\n')



# CREATING FARM NAMED "TRADITIONAL"
####################################################################

# print('\nCREATING FARM TRADITIONAL:')
# carlos.farm_new('TRADITIONAL', 'Germany')
# print(carlos.farms['TRADITIONAL'].info())

# print('\nPLANTING CROP - TRADITIONAL:')
# (carlos.farms['TRADITIONAL'].farmer.prepare_crop( 30, 'Manzana'))
# (carlos.farms['TRADITIONAL'].farmer.prepare_crop( 20, 'Topocho', 4))
# (carlos.farms['TRADITIONAL'].farmer.prepare_crop( 5, 'Lentil', 2))
# (carlos.farms['TRADITIONAL'].farmer.prepare_crop( 4, 'Beans', 4))
# (carlos.farms['TRADITIONAL'].farmer.prepare_crop( 12, 'Anana', 8))
# (carlos.farms['TRADITIONAL'].farmer.prepare_crop( 17, 'DMT', 9))

# print('\nSIMULATING TIME - TRADITIONAL/CROPS:')
# (carlos.farms['TRADITIONAL'].farmer.sim_time('Manzana',**simData))
# (carlos.farms['TRADITIONAL'].farmer.sim_time('Topocho',**simData))
# (carlos.farms['TRADITIONAL'].farmer.sim_time('Lentil',**simData))
# (carlos.farms['TRADITIONAL'].farmer.sim_time('Beans',**simData))
# (carlos.farms['TRADITIONAL'].farmer.sim_time('Anana',**simData))
# (carlos.farms['TRADITIONAL'].farmer.sim_time('DMT',**simData))
# print('\n\n')




####################################################################
####################################################################
####################################################################
####################################################################
			# NEW USER
			# VIKTOR
####################################################################
####################################################################
####################################################################

# CREATING USER NAMED "viktor"
####################################################################

# print('CREATING USER viktor:')
# viktor = User(**userData2)
# print( repr(viktor) )
# print( viktor )
# print( viktor.user_report() )



# CREATING FARM NAMED "SOLAR_MINING"
####################################################################

# print('\nCREATING FARM SOLAR_MINING:')
# viktor.farm_new('SOLAR_MINING', 'Indonesia')
# print(viktor.farms['SOLAR_MINING'].info())

# print('\nPRINTING A FARM AQ OBJECTS\n')
# (viktor.farms['SOLAR_MINING'].farmer.prepare_crop( 10,  'Haze',	  5))
# (viktor.farms['SOLAR_MINING'].farmer.prepare_crop( 1.5, 'Blueberry',    1))
# (viktor.farms['SOLAR_MINING'].farmer.prepare_crop( 0.7, 'Tibetan',	  2))

# print('\nSIMULATING TIME - SOLAR_MINING/CROPS:')
# (viktor.farms['SOLAR_MINING'].farmer.sim_time('Haze',**simData))
# (viktor.farms['SOLAR_MINING'].farmer.sim_time('Blueberry',**simData))
# (viktor.farms['SOLAR_MINING'].farmer.sim_time('Tibetan',**simData))
# print('\n\n')




####################################################################
####################################################################
####################################################################
####################################################################
#							 REPORTS
####################################################################
####################################################################
####################################################################


#	 					CARLOS FARM REPORTS
####################################################################
print ( '\n\n PRINTING Carlos REPORTS' )
print ( '\n\n PRINTING Carlos REPORTS/AQUAPONIC' )
(carlos.farms['AQUAPONIC'].farmer.report('Plum'))
# (carlos.farms['AQUAPONIC'].farmer.report('Cherry'))

# print ( '\n\n PRINTING Carlos REPORTS/HYDROPONIC' )
# (carlos.farms['HYDROPONIC'].farmer.report('Chayota'))
# (carlos.farms['HYDROPONIC'].farmer.report('Peyote'))

# print ( '\n\n PRINTING Carlos REPORTS/TRADITIONAL' )
# (carlos.farms['TRADITIONAL'].farmer.report('Manzana'))
# (carlos.farms['TRADITIONAL'].farmer.report('Topocho'))
# (carlos.farms['TRADITIONAL'].farmer.report('Lentil'))
# (carlos.farms['TRADITIONAL'].farmer.report('Beans'))
# (carlos.farms['TRADITIONAL'].farmer.report('Anana'))
# (carlos.farms['TRADITIONAL'].farmer.report('DMT'))



#	 					VIKTOR FARM REPORTS
####################################################################

# print( '\n\n PRINTING Viktor REPORTS' )
# print ( '\n\n PRINTING Viktor REPORTS/SOLAR_MINING' )
# (viktor.farms['SOLAR_MINING'].farmer.report('Haze'))
# (viktor.farms['SOLAR_MINING'].farmer.report('Blueberry'))
# (viktor.farms['SOLAR_MINING'].farmer.report('Tibetan'))

print ('''

		END OF TEST

		''')

print( Plant.plantCounter )




