import time
from imutils import face_utils
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
import numpy as np

def getFaceHorizontal(shape):        
        start = time.time()
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        # compute the center of mass for each eye
        leftEyeCenter = leftEye.mean(axis=0).astype('int')
        rightEyeCenter = rightEye.mean(axis=0).astype('int')
        # compute the angle between the eye centroids
        dY = rightEyeCenter[1] - leftEyeCenter[1]
        dX = rightEyeCenter[0] - leftEyeCenter[0]
        angle = np.degrees(np.arctan2(dY, dX)) + 180
        if ( 0 < angle <= 180):
            faceHorizontal = - angle
        else: 
            faceHorizontal = - (angle - 360) 
        et = time.time() - start
        return faceHorizontal
