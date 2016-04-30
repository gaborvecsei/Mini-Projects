"""*************************************
Created By Vecsei Gabor
Blog: https://gaborvecsei.wordpress.com/
Email: vecseigabor.x@gmail.com
https://bitbucket.org/gaborvecsei/
*************************************"""

"""**************SUMMARY****************
With this program you can capture an image from
your webcamera and upload it to your Google Drive.

You'll need a client_secrets.json file from Google Drive API
Get it from here: https://console.developers.google.com
Create a project -> Enable it -> Download json -> Rename it to: client_secrets.json

To run this: python Capture_Img_To_Drive.python
*************************************"""

import requests as req
import numpy as np
import cv2
import time
import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

"""
The main loop
"""

def main():
	print 'Welcome Adventurer!'
	print "Capturing photo...(Press 'q' for capturing)\n"

	capturedImageName = CaptureImage()
	print 'The captured image name is: ' + capturedImageName

	question = '\nUpload image to your Google Drive?(y/n)\n'
	answer = raw_input(question)
	if answer == 'y':
		UploadToDrive(capturedImageName)
	else:
		print 'Image is not uploaded :('

"""
Captures an image from your webcamera
and returns the captured image's name
"""
def CaptureImage():
	imageName = 'DontCare.jpg' #Just a random string
	cap = cv2.VideoCapture(0)
	while(True):
	    # Capture frame-by-frame
	    ret, frame = cap.read()

	    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #For capture image in monochrome
	    rgbImage = frame #For capture the image in RGB color space

	    # Display the resulting frame
	    cv2.imshow('Webcam',rgbImage)
	    #Wait to press 'q' key for capturing
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        #Set the image name to the date it was captured
	        imageName = str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg'
	        #Save the image
	        cv2.imwrite(imageName, rgbImage)
	        break
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
	#Returns the captured image's name
	return imageName

def UploadToDrive(imageName):
	#We can upload it, HOOORAY!
    print 'Authentication Started\n'
    #Google Drive authentication
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    upload_folder = 'PythonAppImages' #Name of the folder where I'd like to upload images
    upload_folder_id = None #Id of the folder where I'd like to upload images

    #Check if folder exists. If not than create one with the given name
    #Check the files and folers in the root foled
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file_folder in file_list:
        if file_folder['title'] == upload_folder:
            upload_folder_id = file_folder['id'] #Get the matching folder id
            print 'Image is uploaded to EXISTING folder: ' + file_folder['title']
            break #We need to leave this if it's done
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

    print 'Download URL: ' + file_image['webContentLink'] #This is the download URL of the file


if __name__ == "__main__":
	main()