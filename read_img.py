import face_recognition
import numpy as np

encodinglist = list(np.load('/home/pi/ZYDEMO/iota/ecodinglist.npy'))
image = face_recognition.load_image_file('/home/pi/ZYDEMO/iota/IMG_0133.PNG')
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)
# global ecodinglist, namelist
encodinglist.append(face_encodings[0])
# namelist.append(name)
np.save('ecodinglist.npy', face_encodings)
# np.save('resources/namelist.npy', namelist)
