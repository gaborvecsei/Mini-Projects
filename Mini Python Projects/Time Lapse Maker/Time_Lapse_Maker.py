"""*************************************
Created By Vecsei Gabor
Blog: https://gaborvecsei.wordpress.com/
Email: vecseigabor.x@gmail.com
https://bitbucket.org/gaborvecsei/
*************************************"""

"""**************SUMMARY****************
The program captures an image from your webcam time
to time and uploads it to your Google Drive.
(you can specify the folder where you'd like to upload it)

You'll need a client_secrets.json file from Google Drive API
Get it from here: https://console.developers.google.com
Create a project -> Enable it -> Download json -> Rename it to: client_secrets.json

To run this: python Time_Lapse_Maker.py
*************************************"""

import cv2
import sys
import os
import time
import requests as req
import numpy as np
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


"""
Captures an image and returns
with the name of the captured image
"""
def CaptureImage(camera):
	#Just a random string
	imageName = 'DontCare.jpg'
	# Capture frame
	ret, frame = camera.read()
	rgbImage = frame
	imageName = str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg'
	#Save the image
	cv2.imwrite(imageName, rgbImage)
	#Returns the captured image's name
	return imageName

"""
Google Drive Authentication
It should be done once
"""
def DriveAuth():
    print 'Authentication Started'
    #Google Drive authentication
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    print 'Authentication completed!'
    return gauth

"""
Uploads an image to Google Drive
"""
def UploadToDrive(gauth,imageName):
    drive = GoogleDrive(gauth)

    #Name of the folder where I'd like to upload images
    upload_folder = 'TimeLapse_TEST'
    #Id of the folder where I'd like to upload images
    upload_folder_id = None

    #Check if folder exists. If not than create one with the given name
    #Check the files and folers in the root foled
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file_folder in file_list:
        if file_folder['title'] == upload_folder:
        	#Get the matching folder id
            upload_folder_id = file_folder['id']
            print 'Image is uploaded to EXISTING folder: ' + file_folder['title']
            #We need to leave this if it's done
            break
        else:
            #If there is no mathing folder, create a new one
            file_new_folder = drive.CreateFile({'title': upload_folder,
                "mimeType": "application/vnd.google-apps.folder"})
            file_new_folder.Upload() #Upload the folder to the drive
            print 'New folder created: ' + file_new_folder['title']
            upload_folder_id = file_new_folder['id'] #Get the folder id
            print 'Image is uploaded to the NEW folder: ' + file_new_folder['title']
            break #We need to leave this if it's done

    #Create new file in the upload_folder
    file_image = drive.CreateFile({"parents":  [{"kind": "drive#fileLink","id": upload_folder_id}]})
    file_image.SetContentFile(imageName) #Set the content to the taken image
    file_image.Upload() # Upload it


"""
Countdown to wait between captures
"""
def Countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '\r{:02d}:{:02d}'.format(mins, secs)
     	sys.stdout.write(timeformat)
     	sys.stdout.flush()
        time.sleep(1)
        t -= 1


def main():
	print 'Welcome Adventurer!'
	gDriveAuth = DriveAuth()
	seconds = input('Time between capturing (in seconds): ')
	cap = cv2.VideoCapture(0)
	while(True):
		Countdown(seconds)
        #Capture the image
		capturedImageName = CaptureImage(cap)
		print 'The captured image name is: ' + capturedImageName
        #Uploads to Google Drive
		UploadToDrive(gDriveAuth,capturedImageName)
        #Delete the captured image after it was uploaded
		os.remove(capturedImageName)

	# When everything done, release the capture
	cap.release()

if __name__ == "__main__":
	main()