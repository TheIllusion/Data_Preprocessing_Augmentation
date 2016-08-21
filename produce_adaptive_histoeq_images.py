import numpy as np
import glob
import re
import cv2
import os
import pylab
from matplotlib import pyplot as plt

# get list of image files
#source_image_dir = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted_skin_tone/cropped_images'
#save_directory = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted_skin_tone/histogram_equalized_images/'

source_image_dir = '/Users/Illusion/Temp/jpgs'
save_directory = '/Users/Illusion/Temp/jpgs/adaptive_histoeq_images/'

os.chdir(source_image_dir)

image_files = glob.glob('*.*')

if not os.path.exists(save_directory):
    os.mkdir(save_directory)

for filename in image_files:
    match = re.search(".png", filename)
    if match:
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

        # create a CLAHE object (Arguments are optional).
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        equalized_img = clahe.apply(img)

        new_filename = 'adap_histoeq_' + filename

        cv2.imwrite(save_directory + new_filename, equalized_img)

        print new_filename

        #plt.imshow(equalized_img, cmap=pylab.gray()), plt.colorbar(), plt.show()