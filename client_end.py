import base64
import eel
import socket
import cv2
from api import load_image_file
from api import face_encodings

eel.init('')


@eel.expose
def takePhoto():
    camera = cv2.VideoCapture(0)
    cv2.namedWindow('MyCamera')
    while True:
        success, frame = camera.read()
        cv2.imshow('MyCamera', frame)
        cv2.imwrite('test.jpg', frame)
        if cv2.waitKey(1) & 0xff == ord(' '):
            break
    cv2.destroyWindow('MyCamera')
    camera.release()


@eel.expose
def sendVector(base64_data, id, status):
    base64_data = base64_data.split(',')[1]
    base64_data = str.encode(base64_data)
    data = base64.b64decode(base64_data)
    file = open('prtsc.png', 'wb')
    file.write(data)
    file.close()
    photo = load_image_file('prtsc.png')
    face_vectors = face_encodings(photo)
    face = face_vectors[0]
    face = 'data:' + str(face)
    function = 'function:' + str(status)
    userid = 'id:' + str(id)
    addr = ('122.51.26.166', 22222)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    msg = userid + '\r\n' + function + '\r\n' + face
    msg = str.encode(msg)
    print(msg)
    sock.send(msg)
    feedback = sock.recv(1024).decode()
    print(feedback)
    eel.alert_feedback(feedback)
    sock.close()


@eel.expose
def sendVector2(id, status):
    photo = load_image_file('test.jpg')
    face_vectors = face_encodings(photo)
    face = face_vectors[0]
    face = 'data:' + str(face)
    function = 'function:' + str(status)
    userid = 'id:' + str(id)
    addr = ('122.51.26.166', 22222)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    msg = userid + '\r\n' + function + '\r\n' + face
    msg = str.encode(msg)
    print(msg)
    sock.send(msg)
    feedback = sock.recv(1024).decode()
    print(feedback)
    eel.alert_feedback(feedback)
    sock.close()


eel.start('home.html', mode='chrome', size=(1000, 1000))
