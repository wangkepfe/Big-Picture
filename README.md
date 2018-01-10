# Computer-Vision-Project-2
### final project for UCSC CMPE264 Computer Vision 17 Fall
1. Camera Calibration
   * Chestboard corners detection
   * Calibration: find camera intrinsic matrix and distortion factor
   * Image undistortion process
2. Homography
   * find homographies bwtween each images
   * calculate chain-multiplication of homographies
   * warp images into first image's camera perspective
   * merge images into one big image
3. Image Rotation
   * rotate the image by a homography

raw images:

![alt text](https://github.com/wangkepfe/Computer-Vision-Project-2/blob/master/source/p1.JPG "Title")
![alt text](https://github.com/wangkepfe/Computer-Vision-Project-2/blob/master/source/p2.JPG "Title")
![alt text](https://github.com/wangkepfe/Computer-Vision-Project-2/blob/master/source/p3.JPG "Title")
![alt text](https://github.com/wangkepfe/Computer-Vision-Project-2/blob/master/source/p4.JPG "Title")
![alt text](https://github.com/wangkepfe/Computer-Vision-Project-2/blob/master/source/p5.JPG "Title")

homography matching:

![alt text](https://github.com/wangkepfe/Computer-Vision-Project-2/blob/master/match/match_1_2.jpg "Title")

result:

![alt text](https://github.com/wangkepfe/Computer-Vision-Project-2/blob/master/result.jpg "Title")

