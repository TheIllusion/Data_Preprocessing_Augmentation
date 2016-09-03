import numpy as np
import glob
import re
import cv2
import os

# get list of image files
source_image_dir = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/Saengmyoung/cropped_images'
save_directory = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/Saengmyoung/resized/'

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
        if match:
            img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            new_image = cv2.resize(img, target_image_size, interpolation=cv2.INTER_CUBIC)
            new_filename = 'resized_' + filename

            if idx % 100 == 0:
                print str(idx) + 'th file. name = ' + new_filename

            cv2.imwrite(save_directory + new_filename, new_image)

            idx = idx + 1

resize_images()