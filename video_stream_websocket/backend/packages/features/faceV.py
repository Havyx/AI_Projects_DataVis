from imutils import face_utils
from scipy.spatial import distance as dist
import time
import numpy as np
import math

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def getFaceVertical(shape):        
    start = time.time()
    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    # compute the center of mass for each eye
    leftEyeCenter = leftEye.mean(axis=0).astype('int')
    rightEyeCenter = rightEye.mean(axis=0).astype('int')
    # compute the center of mass for mouth
    (mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
    Mouth = shape[mStart:mEnd]
    MouthCenter = Mouth.mean(axis=0).astype('int')
    # compute the angle between opposite side and hypotenuse
    dHy = leftEyeCenter[0] - rightEyeCenter[0]
    dOS = MouthCenter[1] - (rightEyeCenter[1] + leftEyeCenter[1])/2        
    if dHy >= dOS:
        x = 1 - dOS/dHy
    else:
        x = - (1 - dHy/dOS)
    faceVertical = math.degrees(math.asin(x))
    et = time.time() - start
    return faceVertical

    # compute the angle between the eye centroids
    #dY = rightEyeCenter[1] - leftEyeCenter[1]
    #dX = rightEyeCenter[0] - leftEyeCenter[0]
    #angle = np.degrees(np.arctan2(dY, dX)) + 180
    #if ( 0 < angle <= 180):
    #    faceAlignment = - angle
    #else: 
    #    faceAlignment = - (angle - 360) 
    #et = time.time() - start
    #return {'name': 'faceAlignment', 'value': faceAlignment, 'cost': 1000 * et}