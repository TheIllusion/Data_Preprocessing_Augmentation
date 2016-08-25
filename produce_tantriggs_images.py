import glob
import re
import os
from subprocess import call

source_image_dir = '/Users/Illusion/Documents/Data/palm_data/tan_triggs_LTP/resized'

os.chdir(source_image_dir)

image_files = glob.glob('*.*')

for filename in image_files:
    #match = re.search(".png", filename)
    match = re.search(".jpg", filename)
    if match:
        call(["/Users/Illusion/Documents/Data/palm_data/tan_triggs_LTP/Preprocessing", filename])
