import numpy as np
import cv2
import glob

patch_x = 7
patch_y = 7
patch_size = (7  ,7)

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((patch_x * patch_y, 3), np.float32)
objp[:,:2] = np.mgrid[0:patch_y , 0:patch_x].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

#########################################  filename interface  #######################################

images = glob.glob('calib/*.jpg')

######################################################################################################

# find corners
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    print(fname)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray,
                                         patch_size,
                                         flags=cv2.CALIB_CB_ADAPTIVE_THRESH
                                             +cv2.CALIB_CB_NORMALIZE_IMAGE
                                             +cv2.CALIB_CB_FAST_CHECK)
    
    print(ret)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray, corners,(11,11),(-1,-1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cornerImage = cv2.drawChessboardCorners(img, patch_size, corners2, ret)
        cv2.imwrite('corner\\' + fname[6:], cornerImage)
        
        
# calibration        
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)