import cv2
import numpy as np
import os
import glob
import re

# produce color variations for data augmentation purposes

'''
source_image_dir = '/home/nhnent/H1/users/rklee/Data/gender_recognition/categorized/male'
fancyPCA_save_directory = '/home/nhnent/H1/users/mskang/temp/feasible_test/fancyPCA/'
random_save_directory = '/home/nhnent/H1/users/mskang/temp/feasible_test/random/'
'''

source_image_dir = '/Users/Illusion/Documents/Data/palm_data/hand_classifier/From_SVCs/nonhand_candidates_svc_refined'
fancyPCA_save_directory = '/Users/Illusion/Documents/Data/palm_data/hand_classifier/From_SVCs/nonhand_fancyPCA/'
random_save_directory = '/Users/Illusion/Documents/Data/palm_data/hand_classifier/From_SVCs/nonhand_random/'

'''
    source_image_dir = '/home/nhnent/H1/users/rklee/Data/gender_recognition'
    fancyPCA_save_directory = '/home/nhnent/H1/users/rklee/Data/gender_recognition/fancyPCA/'
    random_save_directory = '/home/nhnent/H1/users/rklee/Data/gender_recognition/random/'
'''


def fancyPCA(imagePath):
    im = cv2.imread(imagePath, -1)
    imd = im / 255.0

    upperThreshold = 1.0
    lowerThreshold = 0.0

    while_flag = True

    result = np.zeros(shape=im.shape)

    while while_flag == True:

        m = len(imd)
        # print m
        n = len(imd[0])
        # print n

        im1 = np.reshape(imd[:, :, 0], [1, m * n])
        im2 = np.reshape(imd[:, :, 1], [1, m * n])
        im3 = np.reshape(imd[:, :, 2], [1, m * n])

        m1 = np.mean(im1)
        m2 = np.mean(im2)
        m3 = np.mean(im3)

        d1 = im1 - m1
        d2 = im2 - m2
        d3 = im3 - m3

        data = np.hstack((d1.T, d2.T, d3.T))
        datat = data.T

        d, v = np.linalg.eig(np.dot(data.T, data))

        if d.any() < 0:
            print 'd is minus!', str(d)

        dv = np.reshape(np.sqrt(d), [3, 1])

        val = np.dot(v, np.multiply(0.1 * np.random.rand(3, 1), dv))

        # print val
        # print val[0]/255.0
        # print val[1]/255.0
        # print val[2]/255.0

        b, g, r = cv2.split(imd)

        b = b + 4.5 * (val[0] / 255.0)
        g = g + 4.5 * (val[1] / 255.0)
        r = r + 4.5 * (val[2] / 255.0)

        if b.any() < 0:
            print 'b is minus!', str(b)
        if g.any() < 0:
            print 'g is minus!', str(g)
        if r.any() < 0:
            print 'r is minus!', str(r)

        result = cv2.merge((b, g, r))

        if (np.mean(result) < lowerThreshold) | (np.mean(result) > upperThreshold):
            print np.mean(result)
        else:
            # print np.mean(result)
            while_flag = False
            return result

    return result


def random(imagePath):
    im = cv2.imread(imagePath, -1)
    imd = im / 255.0

    b, g, r = cv2.split(imd)

    b = b + 0.06 * np.random.standard_normal()
    g = g + 0.06 * np.random.standard_normal()
    r = r + 0.06 * np.random.standard_normal()

    if b.any() < 0:
        print 'b is minus!', str(b)
    if g.any() < 0:
        print 'g is minus!', str(g)
    if r.any() < 0:
        print 'r is minus!', str(r)

    result = cv2.merge((b, g, r))
    # print np.random.standard_normal()

    return result


os.chdir(source_image_dir)

image_files = glob.glob('*.jpg')

if not os.path.exists(fancyPCA_save_directory):
    os.mkdir(fancyPCA_save_directory)

if not os.path.exists(random_save_directory):
    os.mkdir(random_save_directory)

file_idx = 0

for filename in image_files:
    # match = re.search(".png", filename)
    match = re.search(".jpg", filename)
    if match:
        for i in range(1, 2):
            result_img = fancyPCA(filename)
            cv2.imwrite(fancyPCA_save_directory + 'fancyPCA_' + str(i) + '_' + filename, result_img * 255.0)

            result_img = random(filename)
            cv2.imwrite(random_save_directory + 'random_' + str(i) + '_' + filename, result_img * 255.0)

        # print str(i)+'th process done.'
        if file_idx % 100 == 0:
            print str(file_idx) + 'th file done.'
        file_idx = file_idx + 1

print 'finished!'
# cv2.waitKey()
