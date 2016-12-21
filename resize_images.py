import numpy as np
import glob
import re
import cv2
import os

# get list of image files
source_image_dir = '/data/users/rklee/the_simplest_hand_classifier_v1/training_data'
save_directory = '/data/users/rklee/the_simplest_hand_classifier_v1/training_data_resized/'

#source_image_dir = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/cropped_images'
#save_directory = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/resized/'

target_image_size = (512, 512)

def resize_images():
    idx = 0
    os.chdir(source_image_dir)

    image_files = glob.glob('*.*')

    if not os.path.exists(save_directory):
        os.mkdir(save_directory)

    for filename in image_files:
        #match = re.search(".png", filename)
        match = re.search(".jpg", filename)
        match2 = re.search(".JPG", filename)
        match3 = re.search(".jpeg", filename)
        match4 = re.search(".JPEG", filename)
        match5 = re.search(".png", filename)
        match6 = re.search(".PNG", filename)

        if match or match2 or match3 or match4 or match5 or match6:
            img = cv2.imread(filename, cv2.IMREAD_COLOR)

            if (type(img) is not np.ndarray):
                idx = idx + 1
                print 'skip this jpg file. continue.'
                continue

            new_image = cv2.resize(img, target_image_size, interpolation=cv2.INTER_CUBIC)
            new_filename = 'resized_' + filename
            #new_filename = filename

            if idx % 100 == 0:
                print str(idx) + 'th file. name = ' + new_filename

            cv2.imwrite(save_directory + new_filename, new_image)

            idx = idx + 1

resize_images()