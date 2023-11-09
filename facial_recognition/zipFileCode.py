import boto3
import json
import zipfile

obj = boto3.client("s3")
#################################################################
############# Uploading a png file to S3 in         #############
############# 'yanntrialbucket' from desired folder #############
#################################################################

obj.upload_file(
	Filename="C:/Users/Yann/Downloads/zipTest.zip", # directory where the .zip is located
	Bucket="yanntrialbucket",			# destination s3 bucket
	Key="pictures.zip"				# name assigned to .zip in the s3 bucket
)

############################################################
############# Downloading a zip file           #############
############# from S3 bucket to desired folder #############
############################################################

obj.download_file(
    Filename="C:/Users/Yann/Downloads/NewPics.zip",	# directory + name where to download .zip
    Bucket="yanntrialbucket",				# desired s3 bucket
    Key="pictures.zip"					# name assigned to .zip in the s3 bucket
)

#############################################
############# Unzip file	#############
############# to desired folder #############
#############################################

with zipfile.ZipFile("C:/Users/Yann/Downloads/NewPics.zip", 'r') as zip_ref:	# directory of .zip to unzip
    zip_ref.extractall("C:/Users/Yann/Downloads/")				# directory where to unzip to