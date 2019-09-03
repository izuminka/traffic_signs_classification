import os
import skimage

import random # for random.seed sampling of the images
import numpy as np

from data_analysis import get_sample_images
from data_process import load_data, resize_images


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))
train_work_dir = f"{ROOT_PATH}/data/training"
test_work_dir = f"{ROOT_PATH}/data/testing"

# load raw images
images, labels = load_data(train_work_dir)
# print(images_28_28.shape) #(4575,)
random.seed(1)
get_sample_images(5, images)

# resize all images to the the same l and w
NEW_IM_SIZE = 28
images_28_28 = resize_images(images, NEW_IM_SIZE)
# print(images_28_28.shape) #(4575, 28, 28, 3)
random.seed(1)
get_sample_images(5, images_28_28)

# gray out all resized images
images_28_28_gray = skimage.color.rgb2gray(images_28_28)
# print(t.shape) #(4575, 28, 28)
random.seed(1)
get_sample_images(5, images_28_28_gray)
