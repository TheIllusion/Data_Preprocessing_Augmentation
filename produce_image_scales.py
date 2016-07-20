import numpy as np
import glob
import re
import cv2
import os
import pylab
from matplotlib import pyplot as plt

# get list of image files
source_image_dir = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted/histogram_equalized_images'
save_directory = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted/image_pyramids/'

os.chdir(source_image_dir)

image_files = glob.glob('*.*')

if not os.path.exists(save_directory):
    os.mkdir(save_directory)

for filename in image_files:
    match = re.search(".png", filename)
    if match:
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

        newx, newy = img.shape[1] / 4, img.shape[0] / 4  # new size (w,h)
        new_image = cv2.resize(img, (newx, newy))

        new_filename = 'histo_equalized_' + filename

        #cv2.imwrite(save_directory + new_filename, equalized_img)

        print new_filename

        plt.imshow(new_image, cmap=pylab.gray()), plt.colorbar(), plt.show()