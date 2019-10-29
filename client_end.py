import base64
import eel
from socket import *
from api import load_image_file
from api import face_encodings

eel.init('C:\\Users\\86139\\PycharmProjects\\untitled')


@eel.expose
def img_to_vector(base64_data):
    base64_data = base64_data.split(',')[1]
    base64_data = str.encode(base64_data)
    data = base64.b64decode(base64_data)
    file = open('prtsc.png', 'wb')
    file.write(data)
    file.close()
    photo = load_image_file('prtsc.png')
    face_vectors = face_encodings(photo)
    face = face_vectors[0]
    print(face)
    # addr = ('localhost', 21567)
    # sock = socket(AF_INET, SOCK_DGRAM)
    # sock.sendto(face, //addr)
    # sock.close()


eel.start('home.html', size=(1000, 1000))
