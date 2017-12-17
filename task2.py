import numpy as np
import cv2
import glob

#########################################  filename interface  #######################################

targetimages = glob.glob('source/*.jpg')

######################################################################################################

# method 1

for Iname in targetimages:
    img = cv2.imread(Iname)
    h,  w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist,(w,h), 1,(w,h))

    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    # crop the image
    x,y,w,h = roi
    dst = dst[y:y+h, x:x+w]
    #cv2.imwrite('undis1\\' + Iname[7:],dst)
    cv2.imwrite('undis2\\' + Iname[9:],dst)
    
    
# method 2
#
#for Iname in targetimages:
#    img = cv2.imread(Iname)
#    h,  w = img.shape[:2]
#    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
#
#    # undistort
#    mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
#    dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
#
#    # crop the image
#    x,y,w,h = roi
#    dst = dst[y:y+h, x:x+w]
#    cv2.imwrite('undis1\\' + Iname[7:],dst)