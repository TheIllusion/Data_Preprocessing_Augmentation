import os
import re, glob
import shutil
import cv2
import numpy as np

IMAGE_PATH = '/Users/Illusion/Documents/Data/hair_semantic_segmentation/official_training_set/test/'
DEST_IMAGE_PATH = '/Users/Illusion/Documents/Data/hair_semantic_segmentation/official_training_set/original_all_flipped/'

os.chdir(IMAGE_PATH)
jpg_files = glob.glob('*.jpg')
max_test_index = len(jpg_files)

for idx in xrange(max_test_index):
    filename_temp = jpg_files[idx]

    match_1 = re.search(".jpg", filename_temp)
    if match_1:
        end_index = match_1.end()
        filename = filename_temp[0:end_index]

    match_2 = re.search(".JPG", filename_temp)
    if match_2:
        end_index = match_2.end()
        filename = filename_temp[0:end_index]

    if (not match_1) and (not match_2):
        continue

    image = cv2.imread(IMAGE_PATH + filename, cv2.IMREAD_COLOR)
    if type(image) is not np.ndarray:
        print 'cannot open file ' + filename
        continue

    # flip around y-axis
    flipped_image = cv2.flip(image, 1)
    if type(flipped_image) is not np.ndarray:
        print 'cannot flip the image ' + filename
        continue

    cv2.imwrite(DEST_IMAGE_PATH + filename, flipped_image)
