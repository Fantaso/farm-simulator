from utility import Utility
from datetime import date
from time import ctime


class UserSettings(object):
	
	userRid = 1


	def __init__(self, name, location, email, birthday, mobile, emailRecovery):
		
		self.username 			= name
		self.userLocation 		= location
		self.userEmail 			= email
		
		self.userBirthday 		= Utility.birthday_format(birthday)
		self.userMobile 		= mobile
		self.userEmailRecovery	= emailRecovery

		self.userDateStamp		= date.today() # ctime()   # THIS IS NOT A STRING VARIABLE DUE TO date.today()
		self.userTimeStamp 		= ctime().split(' ')[-2]
		self.userRid 			= UserSettings.userRid
		UserSettings.userRid 	+= 1

	def __str__(self):
		return '{}/{}'.format( self.userRid, self.username )



	def user_report(self):
		return '''
				###########################
						USER REPORT
				###########################
				
				Username: 		{1}
				City:			{2}
				Email:			{3}						User ID:		{0}
				Birthday:		{4}									Date Created: 	{7}
				Mobile:			{5}								Time Created:	{8}
				Recovery Email: {6}
				'''.format(self.userRid, self.username, self.userLocation, self.userEmail, self.userBirthday, self.userMobile, self.userEmailRecovery, self.userDateStamp, self.userTimeStamp)