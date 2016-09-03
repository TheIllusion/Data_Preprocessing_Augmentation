import numpy as np
import glob
import re
import cv2
import os
import pylab
from matplotlib import pyplot as plt

# get list of image files
#source_image_dir = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted_skin_tone'
#save_directory = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted_skin_tone/cropped_images/'

source_image_dir = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512'
save_directory = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/cropped_images/'

os.chdir(source_image_dir)

image_files = glob.glob('*.*')

if not os.path.exists(save_directory):
    os.mkdir(save_directory)

for filename in image_files:
    #match = re.search(".png", filename)
    match = re.search(".jpg", filename)
    if match:
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

        crop_img = img[120:570, 15:465]

        new_filename = 'cropped_' + filename

        cv2.imwrite(save_directory + new_filename, crop_img)

        print new_filename

        #plt.imshow(crop_img, cmap=pylab.gray()), plt.colorbar(), plt.show()