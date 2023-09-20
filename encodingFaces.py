import face_recognition
import encodeTest
import cv2
import numpy as np
from io import BytesIO
def encodeFaces():
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("obama.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    img = encodeTest.read_s3_image('biden.jpg')
    # Load a second sample picture and learn how to recognize it.
    biden_image = img
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
    known_face_encodings = [
     obama_face_encoding,
     biden_face_encoding
    #upload this to a databate to compare to and use with the known faces
    ]
    return known_face_encodings



def knownFace():
    known_face_names = [
        "Barack Obama",
        "Joe Biden"
    ]
    return known_face_names