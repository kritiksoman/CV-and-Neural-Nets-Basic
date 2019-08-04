from __future__ import division
import os
import numpy as np
import csv
import sys

rows=[]
with open(os.path.join('instances.csv'), 'r') as csvfile: 
	csvreader = csv.reader(csvfile) 
	for row in csvreader:
		rows.append(row)

APList=[]

K=0
if int(sys.argv[1])!=0:
	K=int(sys.argv[1])

for i in range(len(rows)):	
	row=rows[i]
	labels = row[1:]
	fname = row[0]
	f = open("res/"+fname[0:-4]+'.txt', "r")

	p=[]
	correct=0
	index=0
	if K==0:
		for x in f:
			index+=1
			for label in labels:
				if label in x:
					correct+=1
					p.append(correct/index)
					break
	else:
		for x in f:
			index+=1
			if index<=K:
				for label in labels:
					if label in x:
						correct+=1
						p.append(correct/index)
						break	
	if not p:
		AP=0
	else:
		AP = np.average(p)
	APList.append(AP)

# print APList
print 'mAP = '+ str(np.average(APList))
# print f[0]
