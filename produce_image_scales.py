import numpy as np
import glob
import re
import cv2
import os
import pylab
from matplotlib import pyplot as plt

# get list of image files
source_image_dir = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted_skin_tone/histogram_equalized_images'
save_directory = '/Users/Illusion/Documents/Data/palm_data/NHN_palms/background_subtracted_skin_tone/image_pyramids/'

os.chdir(source_image_dir)

image_files = glob.glob('*.*')

if not os.path.exists(save_directory):
    os.mkdir(save_directory)

target_image_size = (450, 450)

scale_factors = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]

for filename in image_files:
    match = re.search(".png", filename)
    if match:
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

        height, width = img.shape

        for scale_factor in scale_factors:

            if scale_factor <= 1:
                temp_image = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

                calculated_margin = int((450 - 450 * scale_factor) / 2)
                new_image = cv2.copyMakeBorder(temp_image,
                                               calculated_margin,
                                               calculated_margin,
                                               calculated_margin,
                                               calculated_margin,
                                               cv2.BORDER_CONSTANT,
                                               value=[0,0,0])
                new_image = cv2.resize(new_image, target_image_size, interpolation=cv2.INTER_CUBIC)

            elif scale_factor == 1.0:
                new_image = img

            else:
                crop_margin = 0.5 * (width - width * (1 / scale_factor))
                new_image = img[crop_margin : height-crop_margin, crop_margin : width-crop_margin]
                new_image = cv2.resize(new_image, target_image_size, interpolation=cv2.INTER_CUBIC)

            new_filename = str(scale_factor) + 'x_scaled_' + filename

            print new_filename

            cv2.imwrite(save_directory + new_filename, new_image)

            #plt.imshow(new_image, cmap=pylab.gray()), plt.colorbar(), plt.show()