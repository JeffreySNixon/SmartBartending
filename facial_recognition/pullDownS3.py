# importing the zipfile module 
from zipfile import ZipFile
import os
from imutils import paths
import boto3
import zipfile

obj = boto3.client("s3")

obj.download_file(
    Filename="SmartBartending/facial_recognition/dataset.zip",	# directory + name where to download .zip
    Bucket="smartbartending-faces",				# desired s3 bucket
    Key="dataset.zip"					# name assigned to .zip in the s3 bucket
)
with ZipFile('SmartBartending/facial_recognition/dataset.zip') as zObject: 
  
    # Extracting all the members of the zip  
    # into a specific location. 
        zObject.extractall( 
        path='SmartBartending/facial_recognition/dataset') 
knownNames = []
imagePaths = list(paths.list_images('SmartBartending/facial_recognition/dataset'))
#print(imagePaths)
# loading the temp.zip and creating a zip object 
for (i, imagePath) in enumerate(imagePaths):
	# extract the person name from the image path
    #if imagePath.endswith('.zip'):
    name = imagePath.split(os.path.sep)[-2]
    knownNames.append(name)

	    # loop over the encodings
	    

     
print(knownNames)
# for(i,names) in enumerate(knownNames):
#     with ZipFile('SmartBartending/facial_recognition/dataset/' +names) as zObject: 
  
#     # Extracting all the members of the zip  
#     # into a specific location. 
#         zObject.extractall( 
#         path='SmartBartending/facial_recognition/dataset/') 	
    
	

	


