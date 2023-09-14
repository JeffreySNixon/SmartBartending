import face_recognition

def encodeFaces(image):
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file(image[0])
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Load a second sample picture and learn how to recognize it.
    biden_image = face_recognition.load_image_file(image[1])
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
    known_face_encodings = [
     obama_face_encoding,
     biden_face_encoding
    #upload this to a databate to compare to and use with the known faces
    ]
    return known_face_encodings

def knownFace(names):
    known_face_names = [
        names[0],
        names[1]
    ]
    return known_face_names