import cv2
import numpy as np
import scipy
from scipy.misc import imread
import cPickle as pickle
import random
import os

def extract_features(image, vector_size=32):

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

    def match(self, image):
        features = extract_features(image)
        img_distances = self.cos_cdist(features)
        return self.names.tolist(),img_distances

