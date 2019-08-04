import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.externals import joblib
import os

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
model = VGG16(weights='imagenet', include_top=False)


# Load from the kmeans model
joblib_file = "joblib_model.pkl"  
kmeans = joblib.load(joblib_file)

cap = cv.VideoCapture("output2.mp4")
ret, frame1 = cap.read()
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
im_size = 128
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
    contours, hierarchy = cv.findContours(mask,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
    # contours,hierarchy,_ = cv.findContours(mask,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    mask = np.repeat(mask[:, :, np.newaxis], 3, axis=2)
    # print(hierarchy)

    for cnt,hier in zip(contours,hierarchy[0]):
        area = cv.contourArea(cnt)
        if area>2000 and hier[3]==-1:
            x,y,w,h = cv.boundingRect(cnt)
            image = cv.resize(frame2[y:y+h,x:x+w,:], (im_size, im_size))
            vgg16_feature = model.predict(np.reshape(image,(1,im_size,im_size,3))).flatten()
            c=kmeans.predict([vgg16_feature])
	    if c==0:
		caption='person'
        	cv.rectangle(frame2,(x,y),(x+w,y+h),(255,0,0))  
		cv.putText(frame2,caption, (x,y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0))	    
	    elif c==1:
		caption='vehicle'          
        	cv.rectangle(frame2,(x,y),(x+w,y+h),(0,0,255))  
		cv.putText(frame2,caption, (x,y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))	    
    #cv.imwrite('out/'+str(idx)+'.png',frame2)
    idx+=1
    cv.imshow('frame1',frame2)     
    k = cv.waitKey(1)
    if k == 27:
        break

    prvs = next
    frameidx+=1

cap.release()
cv.destroyAllWindows()
