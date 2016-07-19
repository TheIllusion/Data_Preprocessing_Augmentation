import numpy as np
import glob
import re
import cv2
from matplotlib import pyplot as plt

# get list of list files
image_files = glob.glob('/Users/Illusion/Documents/Data/palm_data/NHN_palm_aligned/*')

for filename in image_files:
    match = re.search(".jpg", filename)
    if match:
        img = cv2.imread(filename)
        mask = np.zeros(img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        rect = (35, 120, 410, 580)
        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img = img * mask2[:, :, np.newaxis]
        plt.imshow(img), plt.colorbar(), plt.show()