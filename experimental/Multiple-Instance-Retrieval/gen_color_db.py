import cv2
import numpy as np
import scipy
from scipy.misc import imread
import cPickle as pickle
import random
import os
import matplotlib.pyplot as plt

trainPath = '/train new'
dirPathList=[f for f in os.listdir(os.getcwd()+trainPath)]
dirPathList.sort()

# Feature extractor
def extract_features(image_path, vector_size=32):

    image = imread(image_path, mode="RGB")
    try:
        hist = cv2.calcHist(images=[image], channels=[0, 1, 2], mask=None,
                            histSize=[16, 16, 16], ranges=[0, 256] * 3)
        dsc = hist.flatten().astype(np.uint8)
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print 'Error: ', e
        return None

    return dsc


def batch_extractor(pickled_db_path="features.pck"):
    imgIndex = 0
    result = {}
    for dirindex in dirPathList:
        fileLoc = os.getcwd() + trainPath + '/' + dirindex
        imagePathList = [f for f in os.listdir(fileLoc)]
        imagePathList.sort()
        # N += len(imagePathList)
        for imagePath in imagePathList:
            try:
                f=os.path.join(fileLoc, imagePath)
                print 'Extracting features from image %s' % f
                name = dirindex + '_' +imagePath
                result[name] = extract_features(f)
            except Exception, e:
                print e
                print imagePath
    with open(pickled_db_path, 'w') as fp:
        pickle.dump(result, fp)

class Matcher(object):

    def __init__(self, pickled_db_path="features.pck"):
        with open(pickled_db_path) as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.iteritems():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        # getting cosine distance between search image and images database
        v = vector.reshape(1, -1)
        return scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1)

    def match(self, image_path, topn=5):
        features = extract_features(image_path)
        img_distances = self.cos_cdist(features)
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()

        return nearest_img_paths, img_distances[nearest_ids].tolist()

def show_img(path):
    img = imread(path, mode="RGB")
    plt.imshow(img)
    plt.show()
    

batch_extractor()
print('Color histogram database generated.')





