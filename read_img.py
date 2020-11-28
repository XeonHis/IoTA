import face_recognition
import numpy as np

facelist = list(np.load('/home/pi/ZYDEMO/iota/face_encoding.npy'))
namelist = list(np.load('/home/pi/ZYDEMO/iota/name_encoding.npy'))
# namelist = []
# facelist = []
image = face_recognition.load_image_file('/home/pi/ZYDEMO/iota/zcy.jpg')
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)
# global ecodinglist, namelist
facelist.append(face_encodings[0])
namelist.append('Zhang')
np.save('/home/pi/ZYDEMO/iota/face_encoding.npy', face_encodings)
np.save('/home/pi/ZYDEMO/iota/name_encoding.npy', namelist)
