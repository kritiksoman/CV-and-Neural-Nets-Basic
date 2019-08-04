import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# from skimage import filter

cap = cv.VideoCapture("output4.mp4")
ret, frame1 = cap.read()
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
idx = 0 
frameidx=0
while(1):
    ret, frame2 = cap.read()
    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
    bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)

    mask = np.sum(bgr>50,axis=2)
    mask = mask.astype(np.uint8)*255
    # contours = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)[-2]
    image, contours, hierarchy = cv.findContours(mask,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    # contours,hierarchy,_ = cv.findContours(mask,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    mask = np.repeat(mask[:, :, np.newaxis], 3, axis=2)
    # print(hierarchy)

    for cnt,hier in zip(contours,hierarchy[0]):
    	
    	# print(cnt)
    	area = cv.contourArea(cnt)
    	if area>2000 and hier[3]==-1:
	    	# cv.drawContours(mask, cnt, -1, (0, 0, 255), 3)
	    	x,y,w,h = cv.boundingRect(cnt)
	    	cv.rectangle(bgr,(x,y),(x+w,y+h),(255,0,0))
	    	# cv.rectangle(frame2,(x,y),(x+w,y+h),(255,0,0))
	    	if frameidx%10==0:
	    		idx += 1
		    	cv.imwrite('data4/'+str(idx)+'.png',frame2[y:y+h,x:x+w,:])

    cv.imshow('frame2',bgr)
    k = cv.waitKey(30)
    if k == 27:
    	break
    prvs = next
    frameidx+=1
cap.release()
cv.destroyAllWindows()