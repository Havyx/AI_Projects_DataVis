from imutils import face_utils
from scipy.spatial import distance as dist
import time
    
def innerMouthAspectRatio(imouth):
    A = dist.euclidean(imouth[1], imouth[5])
    B = dist.euclidean(imouth[2], imouth[4])
    C = dist.euclidean(imouth[3], imouth[3])
    D = dist.euclidean(imouth[0], imouth[4])
    imar = (A + B + C) / (3.0 * D)
    return imar

def getIMAR(shape):
    start = time.time()
    (imStart, imEnd) = face_utils.FACIAL_LANDMARKS_IDXS["inner_mouth"]
    innerMouth =  shape[imStart:imEnd]
    IMAR = innerMouthAspectRatio(innerMouth)
    et = time.time() - start
    return IMAR