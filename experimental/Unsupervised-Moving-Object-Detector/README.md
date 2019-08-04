## Overview
Python script showing unsupervised moving object detector. Method has been described in pdf report.

## Result 
![image1](https://github.com/kritiksoman/CV-and-Neural-Nets-Basic/blob/master/experimental/Unsupervised-Moving-Object-Detector/res/test_result_camera2.gif)<br/>
Red Bounding Box:  Vehicle<br/>
Blue Bounding Box: Person<br/>

## Saved model and test video
Google Drive Link : https://drive.google.com/open?id=1W1MuomPidhKBSgy-q8WmnDKHjx2nEOSi

## Files:
[1] assign4_vgg_kmeans_gen_model.ipynb: For fitting kmeans model on VGG embedding of cropped train images.<br/>
[2] gen_train_db.py: For cropping out moving objects in train videos and saving them.<br/>
[3] test.py: For running moving objection detection in test video.<br/>
