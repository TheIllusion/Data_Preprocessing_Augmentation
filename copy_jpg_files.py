import os
import re
import shutil

FILE_LIST_PATH = '/data_ssd/users/rklee/palm/sm/extracted_result/right_hand_training_list.txt'
IMAGE_PATH = '/data_ssd/users/rklee/palm/sm/original/'
DEST_IMAGE_PATH = '/data_ssd/users/rklee/data/palm/hand_classifier/right_hand/'

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

    shutil.copyfile(IMAGE_PATH + filename, DEST_IMAGE_PATH + filename)
