# Relation Network
[![MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/kritiksoman/Relation-Network/blob/master/LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kritiksoman/Relation-Network/)

## Overview
IPython Notebook showing pytorch implementation of Google DeepMind paper on Relation Network [1] for Sort-of-Clevr dataset.

## Dependencies
```
numpy 
torch
os
pickle
matplotlib
sklearn
cv2
argparse
```

## Result 
[1] Screenshots<br/>

| Relational | Non-Relational|
| ------------- |:-------------:| 
|![image1](https://github.com/kritiksoman/Relation-Network/blob/master/results/r1.png)| ![image2](https://github.com/kritiksoman/Relation-Network/blob/master/results/r2.png) |

[2] Test Accuracy :<br/>
Relational: 92% , Non-relational: 99%

## Saved model and dataset
Google Drive Link : https://drive.google.com/drive/folders/1fdCrT2Ro3dHQk-s_Ql7zNqmDuJaUtvZd?usp=sharing <br/>
[1] Unzip data.zip into a folder "data" in the root directory of project. <br/>
[2] Put "trained_model.pth" into a folder "model" in the root directory of project.

## Note
Network parameters and architecture were taken from the supplementary material[2].

## Reference
[1] Santoro, Adam, et al. "A simple neural network module for relational reasoning." 
Advances in neural information processing systems. 2017. <br/>
[2] https://papers.nips.cc/paper/7082-a-simple-neural-network-module-for-relational-reasoning-supplemental.zip

