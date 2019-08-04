from selectivesearch import *
from scipy import misc
import warnings
import cv2
from utils import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
warnings.filterwarnings("ignore")#surpress warnings from selective search


# testFileName='easy_multi_2.jpg'

testPath = '/sample_test'
testImgList=[f for f in os.listdir(os.getcwd()+testPath)]
testImgList.sort()

for testFileName in testImgList:
	print(testFileName)
	img = misc.imread('sample_test/'+testFileName)
	# img=cv2.imread('hard_single_2.jpg')
	# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	#Run selective search first
	print('1. Running Selective Search ...')
	img_lbl, regions=selective_search(img, scale=500,sigma=0.9, min_size=100)
	# print(type(regions))

	b=np.array([regions[i]["rect"] for i in range(len(regions))])
	regions = np.unique(b, axis=0)

	#convert to xmin,ymin,xmax,ymax format
	ymax=regions[:,3]+regions[:,1]
	xmax=regions[:,2]+regions[:,0]
	regions[:,2]=xmax
	regions[:,3]=ymax

	# Create figure and axes
	# fig,ax = plt.subplots(1)
	# ax.imshow(img)

	# Find ranking of all images for every bb
	print('2. Finding ranking for every bounding box ...')
	hist = cv2.calcHist([img], [0, 1, 2], None, [16, 16, 16], [0, 256, 0, 256,0, 256])
	#hist = np.concatenate([hist, np.zeros(3)]).reshape(-1,1)
	# hist = cv2.normalize(hist, hist).flatten()
	hist = hist.flatten().astype(np.uint8)
	ma = Matcher('features.pck')

	fnames=[]
	N=len(regions)#no. of bb
	finalScore = np.zeros((3456,N))
	for i in range(len(regions)):
		b=regions[i]
		subimg=img[b[1]:b[3],b[0]:b[2],:]
		names, finalScore[:,i] = ma.match(subimg)#for current bb find rank of all files in DB
		fnames=names

	rank=np.nanmin(finalScore,axis=1)
	index=np.argsort(rank)

	#Print the final rankings
	print('3. Saving the result to text file ...')
	file = open('res/'+testFileName[:-4]+'.txt','w')  
	for i in index:
		# print(fnames[i])
		if i==index[-1]:
			file.write(fnames[i]) 
		else:
			file.write(fnames[i]+'\n') 
	file.close() 




# plt.show()

