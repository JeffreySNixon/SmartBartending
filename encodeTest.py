# import face_recognition
# import numpy as np
# # Load a sample picture and learn how to recognize it.
# obama_image = face_recognition.load_image_file("obama.jpg")
# obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

#     # Load a second sample picture and learn how to recognize it.
# biden_image = face_recognition.load_image_file("biden.jpg")
# biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# # Create arrays of known face encodings and their names
# known_face_encodings = [
#      obama_face_encoding,
#      biden_face_encoding
#     #upload this to a databate to compare to and use with the known faces
#     ]

# myString = map(str,biden_face_encoding)
# myString = ' '.join(myString)
# print(biden_face_encoding)
# print("-----------------------------------------------------------------------------------------")
# print((myString))

# myList = list(myString.split(" "))
# myArr = np.array(map(int,myList))

# print("-----------------------------------------------------------------------------------------")
# print(myArr)

try:
    import os
    import sys
    import datetime
    import time
    import boto3
    import threading
    from boto3.dynamodb.conditions import *
    print("All Modules Loaded ...... ")
except Exception as e:
    print("Error {}".format(e))

s3 = boto3.resource('s3')
bucket = s3.Bucket('smartbartendingbucket')
# Iterates through all the objects, doing the pagination for you. Each obj
# is an ObjectSummary, so it doesn't contain the body. You'll need to call
# get to get the whole body.
# for obj in bucket.objects.all():
#     key = obj.key
#     body = obj.get()['Body'].read()

# print(body)

import cv2
import numpy as np
from io import BytesIO

def read_s3_image(file_name):
    obj = bucket.Object(file_name)
    response = obj.get()
    file_stream = response['Body']
    img = np.asarray(bytearray(file_stream.read()), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img


# img = read_s3_image('biden.jpg')
# # cv2.imshow('Image', img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# print(img)



