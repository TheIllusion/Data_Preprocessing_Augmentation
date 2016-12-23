import numpy as np
import glob
import re
import cv2
import os
import pylab
from matplotlib import pyplot as plt

# get list of image files
source_image_dir = '/Users/Illusion/Documents/Data/palm_data/hand_classifier/From_SVCs/nonhand_candidates_svc_refined'
save_directory = '/Users/Illusion/Documents/Data/palm_data/hand_classifier/From_SVCs/nonhand_image_shifted/'

#source_image_dir = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/Saengmyoung/rotated'
#save_directory = '/media/illusion/ML_DATA_M550_SSD/palm_data/experiment9_512_512/Saengmyoung/shifted/'

os.chdir(source_image_dir)

image_files = glob.glob('*.jpg')

if not os.path.exists(save_directory):
    os.mkdir(save_directory)

horizontal_shift_factors = [50, 50]
vertical_shift_factors = [-50, 50]

idx = 0
for filename in image_files:
    #match = re.search(".png", filename)
    match = re.search(".jpg", filename)
    if match:
        #img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.imread(filename, cv2.IMREAD_COLOR)

        if not (img == None):

            rows = img.shape[0]
            cols = img.shape[1]

            for horizontal_shift_factor in horizontal_shift_factors:
                for vertical_shift_factor in vertical_shift_factors:
                    if (horizontal_shift_factor == 0) and (vertical_shift_factor == 0):
                        new_image = img
                        new_filename = '0_0_shifted_' + filename
                    else :
                        M = np.float32([[1, 0, horizontal_shift_factor], [0, 1, vertical_shift_factor]])
                        new_image = cv2.warpAffine(img, M, (cols, rows))
                        new_filename = str(horizontal_shift_factor) + '_' + str(vertical_shift_factor) + '_' + filename

                    #print new_filename

                    cv2.imwrite(save_directory + new_filename, new_image)

                    #plt.imshow(new_image, cmap=pylab.gray()), plt.colorbar(), plt.show()

                    idx = idx + 1
                    if idx % 1000 == 0:
                        print 'idx = ', idx