import numpy as np
import glob
import re
import cv2
import os
import pylab
from matplotlib import pyplot as plt

# get list of image files
source_image_dir = '/Users/Illusion/Temp/female/'

#target_image_size = (512, 512)
#desired_width = 512
#desired_height = 512

# shifting factors
horizontal_shift_factors = [-50, 0, 50]
vertical_shift_factors = [-50, 0, 50]

# rotating factors
rotate_degrees = [10, 20, 0, 340, 350]

# zoom factors
# scale_factors = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
scale_factors = [0.95, 1.1, 1.2]

def augment_imgs_with_shifting(source_path):
    os.chdir(source_path)
    image_files = glob.glob('*.jpg')
    os.chdir('..')

    dest_path = os.path.join(os.getcwd(), "shifted/")

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    idx = 0
    for filename in image_files:
        # match = re.search(".png", filename)
        match = re.search(".jpg", filename)
        if match:
            # img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            img = cv2.imread(source_path + filename, cv2.IMREAD_COLOR)

            if type(img) is np.ndarray:

                rows = img.shape[0]
                cols = img.shape[1]

                for horizontal_shift_factor in horizontal_shift_factors:
                    for vertical_shift_factor in vertical_shift_factors:
                        if (horizontal_shift_factor == 0) and (vertical_shift_factor == 0):
                            new_image = img
                            new_filename = '0_0_shifted_' + filename
                        else:
                            M = np.float32([[1, 0, horizontal_shift_factor], [0, 1, vertical_shift_factor]])
                            new_image = cv2.warpAffine(img, M, (cols, rows))
                            new_filename = str(horizontal_shift_factor) + '_' + str(
                                vertical_shift_factor) + '_' + filename

                        # print new_filename

                        cv2.imwrite(dest_path + new_filename, new_image)

                        # plt.imshow(new_image, cmap=pylab.gray()), plt.colorbar(), plt.show()

                        idx = idx + 1
                        if idx % 1000 == 0:
                            print 'idx = ', idx
    return dest_path

def augment_imgs_with_rotating(source_path):

    os.chdir(source_path)
    image_files = glob.glob('*.jpg')
    os.chdir('..')

    dest_path = os.path.join(os.getcwd(), "rotated/")

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    idx = 0
    for filename in image_files:
        # match = re.search(".png", filename)
        match = re.search(".jpg", filename)
        if match:
            img = cv2.imread(source_path + filename, cv2.IMREAD_COLOR)

            if type(img) is np.ndarray:

                rows = img.shape[0]
                cols = img.shape[1]

                for rotate_degree in rotate_degrees:
                    if rotate_degree == 0:
                        new_image = img
                    else:
                        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), rotate_degree, 1)
                        new_image = cv2.warpAffine(img, M, (cols, rows))

                    new_filename = str(rotate_degree) + '_' + filename

                    cv2.imwrite(dest_path + new_filename, new_image)

                    # print new_filename

                    if idx % 1000 == 0:
                        print 'idx = ', idx
                    idx = idx + 1

    return dest_path

def augment_imgs_with_zoom(source_path):
    os.chdir(source_path)
    image_files = glob.glob('*.jpg')
    os.chdir('..')

    dest_path = os.path.join(os.getcwd(), "img_pyramids/")

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    idx = 0
    for filename in image_files:
        # match = re.search(".png", filename)
        match = re.search(".jpg", filename)
        if match:
            # img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            img = cv2.imread(source_path + filename, cv2.IMREAD_COLOR)

            height, width, channel = img.shape

            for scale_factor in scale_factors:

                if scale_factor <= 1:
                    temp_image = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

                    calculated_margin = int((width - width * scale_factor) / 2)
                    new_image = cv2.copyMakeBorder(temp_image,
                                                   calculated_margin,
                                                   calculated_margin,
                                                   calculated_margin,
                                                   calculated_margin,
                                                   cv2.BORDER_CONSTANT,
                                                   value=[0, 0, 0])
                    new_image = cv2.resize(new_image, (width, height), interpolation=cv2.INTER_CUBIC)

                elif scale_factor == 1.0:
                    new_image = img

                else:
                    crop_margin = int(0.5 * (width - width * (1 / scale_factor)))
                    new_image = img[crop_margin: height - crop_margin, crop_margin: width - crop_margin]
                    new_image = cv2.resize(new_image, (width, height), interpolation=cv2.INTER_CUBIC)

                new_filename = str(scale_factor) + 'x_scaled_' + filename

                idx = idx + 1
                if idx % 1000 == 0:
                    print new_filename
                    print str(idx)

                cv2.imwrite(dest_path + new_filename, new_image)

    return dest_path

if __name__ == "__main__":
    print 'augment images with shifting...'
    shifted_image_dir = augment_imgs_with_shifting(source_image_dir)

    print 'augment images with rotating...'
    rotated_image_dir = augment_imgs_with_rotating(shifted_image_dir)

    print 'augment images with zoom in/out...'
    augment_imgs_with_zoom(rotated_image_dir)