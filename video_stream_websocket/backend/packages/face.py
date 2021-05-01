#WINDOWS: pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f
import io
import cv2
import dlib
import numpy as np
from PIL import Image
from imutils import face_utils, resize
from packages.features.mouth import getIMAR
from packages.features.eyes import getLeftEAR
from packages.features.eyes import getRightEAR
from packages.features.faceV import getFaceVertical
from packages.features.faceH import getFaceHorizontal
from packages.models.mongodb import HandleDB

###########################################################################################################################################

def main():
    detect = dlib.get_frontal_face_detector()
    predict = dlib.shape_predictor("packages/shape_predictor_68_face_landmarks.dat")
    handleDB = HandleDB()
    print('Modulo carregado com sucesso!')
    return detect, predict, handleDB

###########################################################################################################################################

def desenhaRetanguloTexto(face, frame):

    bottomLeftCornerOfText = (face.left(),face.bottom())
    fontScale = 0.6
    fontColor = (52, 164, 235)
    lineType = 2
    font = cv2.FONT_HERSHEY_SIMPLEX
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.putText(frame,'$admin', bottomLeftCornerOfText, font, fontScale, fontColor, lineType)#frame = frame[y-50:y+h+50, x-50:x+w+50]
    return frame

###########################################################################################################################################

def getFeatures(frame, shape, countFrames, flag):
    limiar = 40
    rightEAR, frame = getRightEAR(shape, frame)
    leftEAR, frame = getLeftEAR(shape, frame)
    if ((rightEAR + leftEAR)/2) > limiar:
        flag += 1
    else: 
        flag -= 1
    if flag == 0:
        flag = 1
    if flag == 50:
        flag = 49
    print('flag{}'.format(flag))
    faceVertical = getFaceVertical(shape)
    faceHorizontal = getFaceHorizontal(shape)
    IMAR = getIMAR(shape)
    countFrames +=1
    data_dict = {'frame': countFrames , 'flag': flag, 'leftEAR': leftEAR, 'rightEAR': rightEAR, 'faceVertical': faceVertical, 'faceHorizontal': faceHorizontal, 'IMAR': IMAR}
    handleDB.atualiza(data_dict)#print(data_dict)
    return frame, countFrames, flag

##########################################################################################################################################

def reconhecimentoFacial(message, countFrames, flag):
    frame = np.array(Image.open(io.BytesIO(message)))
    frame = resize(frame, width=360)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect(gray, 0) #detecta faces no frame gray.
    for face in faces:
        shape = predict(gray, face) #determina as landmarks facias para a região do rosto.
        shape = face_utils.shape_to_np(shape) #converte as coordenadas das landmarks faciais (x, y) em NumPy array.
        frame, countFrames, flag = getFeatures(frame, shape, countFrames, flag)
        frame = desenhaRetanguloTexto(face, frame)
        cv2.imshow("Frame", frame)
        return frame, countFrames, flag

##########################################################################################################################################

if __name__ == "__main__":
    print('Esse código deveria ser importado como package')
else:
    print('Importando modulo de reconhecimento facial...')
    detect, predict, handleDB  = main()
