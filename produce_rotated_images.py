import numpy as np
import glob
import re
import cv2
import os
import pylab
from matplotlib import pyplot as plt

# get list of image files
source_image_dir = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/Saengmyoung/resized'
save_directory = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/Saengmyoung/rotated/'

#source_image_dir = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/resized'
#save_directory = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/rotated/'

os.chdir(source_image_dir)

image_files = glob.glob('*.*')

if not os.path.exists(save_directory):
    os.mkdir(save_directory)

rotate_degrees = [10, 20, 30, 0, 330, 340, 350]

idx = 0
for filename in image_files:
    #match = re.search(".png", filename)
    match = re.search(".jpg", filename)
    if match:
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

        if not (img == None):

            rows = img.shape[0]
            cols = img.shape[1]

            for rotate_degree in rotate_degrees:
                if rotate_degree == 0:
                    new_image = img
                else :
                    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), rotate_degree, 1)
                    new_image = cv2.warpAffine(img, M, (cols, rows))

                new_filename = str(rotate_degree) + '_' + filename

                cv2.imwrite(save_directory + new_filename, new_image)

                #print new_filename

                if idx % 1000 == 0:
                    print 'idx = ', idx
                idx = idx + 1

                #plt.imshow(new_image, cmap=pylab.gray()), plt.colorbar(), plt.show()