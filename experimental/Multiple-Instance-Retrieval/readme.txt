-------------------------READ-ME------------------------
Files:
assign1.py: Gives ranking for all images in train (saved as txt in res folder)
gen_color_db.py: Creates a features.pck which contains color histogram descriptor for all train images
mAP.py: Finds mean average precision
selectivesearch.py: It gives bounding boxes for probable objects in test image.
utils.py: Contains functions to cosine similarity between features
convert_to_csv: Converts the test labels into .csv format for running mAP.py

Steps to run:
1. Put the test images in sample_test folder.
2. Run assign1.py to get ranking for all training images with respect to test image.
3. Run mAP.py (ex: python mAP.py 50 for finding mAP on the first 50 ranks). 

Commands:
1. python assign1.py
2. python mAP.py 10 (If you want to find mAP on entire dataset, then run the following: python mAP.py 0)