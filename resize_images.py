import numpy as np
import glob
import re
import cv2
import os

# get list of image files
#source_image_dir = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted_skin_tone/shifted'
#save_directory = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted_skin_tone/resized/'

source_image_dir = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/NHN_palm_aligned_Marking_Result/Result_Saengmyoung/shifted'
save_directory = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/NHN_palm_aligned_Marking_Result/Result_Saengmyoung/resized/'

target_image_size = (128, 128)

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