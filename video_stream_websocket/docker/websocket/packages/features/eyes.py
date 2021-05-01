from imutils import face_utils
from scipy.spatial import distance as dist
import time
import cv2

def extrai_coordenadas(shape):
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    return leftEye, rightEye

def eyeAspectRatio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def getLeftEAR(shape, frame):       
    start = time.time()
    leftEye, rightEye = extrai_coordenadas(shape)
    leftEAR = eyeAspectRatio(leftEye)
    #leftEyeHull = cv2.convexHull(leftEye)
    #cv2.drawContours(frame, [leftEyeHull], -1, (52, 164, 235), 1)
    et = time.time() - start    
    return leftEAR, frame

def getRightEAR(shape, frame):        
    start = time.time()
    leftEye, rightEye = extrai_coordenadas(shape)
    rightEAR = eyeAspectRatio(rightEye)
    #rightEyeHull = cv2.convexHull(rightEye)
    #cv2.drawContours(frame, [rightEyeHull], -1, (52, 164, 235), 1)
    et = time.time() - start    
    return rightEAR, frame