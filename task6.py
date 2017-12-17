# stitch images into one large image

result = np.zeros((targetSize[1],targetSize[0],3), np.uint8)

for i in range(int(targetSize[1] / 500)):
    for j in range(int(targetSize[0] / 500)):
        for ii in range(500):
            for jj in range(500):
                x = i * 500 + ii
                y = j * 500 + jj
                mark = []
                for k in range(5):
                    if warppedImages[k][x,y,0] != 0 or warppedImages[k][x,y,1] != 0 or warppedImages[k][x,y,2] != 0:
                        result[x,y] = warppedImages[k][x,y]
                        mark.append(k)
                if len(mark) == 2:
                    r1 =  warppedImages[mark[0]][x,y,0]
                    g1 =  warppedImages[mark[0]][x,y,1]
                    b1 =  warppedImages[mark[0]][x,y,2]
                    r2 =  warppedImages[mark[1]][x,y,0]
                    g2 =  warppedImages[mark[1]][x,y,1]
                    b2 =  warppedImages[mark[1]][x,y,2]
                    
                    if r1 > r2:
                        r = r2 + (r1 - r2) / 2
                    else:
                        r = r1 + (r2 - r1) / 2
                        
                    if g1 > g2:
                        g = g2 + (g1 - g2) / 2
                    else:
                        g = g1 + (g2 - g1) / 2
                        
                    if b1 > b2:
                        b = b2 + (b1 - b2) / 2
                    else:
                        b = b1 + (b2 - b1) / 2
                        
                    result[x,y] = np.asarray([r,g,b])
        cv2.imwrite('result.jpg',result)