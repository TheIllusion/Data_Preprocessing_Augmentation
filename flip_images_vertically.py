import os
import re
import shutil
import cv2
import numpy as np

FILE_LIST_PATH = '/data_ssd/users/rklee/palm/sm/extracted_result/right_hand_training_list.txt'
IMAGE_PATH = '/data_ssd/users/rklee/data/palm/hand_classifier/right_hand/'
DEST_IMAGE_PATH = '/data_ssd/users/rklee/data/palm/hand_classifier/left_hand/'

file_list_file = open(FILE_LIST_PATH)
file_list = file_list_file.readlines()
file_list_len = len(file_list)

for idx in xrange(file_list_len):
    filename_temp = file_list[idx]

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
