"""*************************************
Created By Vecsei Gabor
Blog: https://gaborvecsei.wordpress.com/
Email: vecseigabor.x@gmail.com
https://bitbucket.org/gaborvecsei/
*************************************"""

"""**************SUMMARY****************
With this code you can update a Google spreadsheet.
This is pretty easy with
https://www.cloudstitch.com/
Just paste your MAGIC_FORM_URL and give name to
your columns. Like here I use 2: Time and Action
*************************************"""

import requests
import time

MAGIC_FORM_URL = '<your_magic_form_URL>'

def UpdateSpreadsheet():
	#This is what we'll send to the given URL
	data = {
		"Time": time.strftime("%Y-%m-%d %H:%M"), 
		"Action": 'This is a test'
	}
	#Print it to the console
	print 'Update Google spreadsheet with\n' + (str(data['Time']) + " " + str(data['Action']))
	#Send the data
	result = requests.post(MAGIC_FORM_URL, data)
	print 'Result of the POST:' + result

while True:
	button = input("Press ENTER to send data\n")
	UpdateSpreadsheet()
