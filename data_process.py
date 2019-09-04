import os
import skimage
# import random # for random.seed sampling of the images
import numpy as np

def load_data(data_dir):
    """Load images and labels

    Args:
        data_dir (str): path to the data

    Returns:
        tuple: images (list) of image (numpy.ndarray) of ndim 3, various l,w
               labels (list) of lable (int)

    """
    group_labels = [d for d in os.listdir(data_dir) if
                    os.path.isdir(f"{data_dir}/{d}")]

    images, labels = [], []
    # TODO add more image extensions
    image_ext = (".ppm", ".jpeg", ".jpg")
    for label in group_labels:
        file_paths_group = [f"{data_dir}/{label}/{f}" for f in
                            os.listdir(f"{data_dir}/{label}") if f.endswith(image_ext)]
        for image_file in file_paths_group:
            images.append(skimage.data.imread(image_file))
            labels.append(int(label))
    return np.array(images), np.array(labels).astype(int)

def resize_images(images, size):
    #TODO implement skimage.transform.resize on the entire np.array instead of
          #converting to list and then back to np.array
    """Resize a list of images to the same lenth and width

    Args:
        images (numpy.ndarray): each image with var shape (w, l, 3)
        size (type): Description of parameter `size`.

    Returns:
        numpy.ndarray: each image (numpy.ndarray) with shape (size, size, 3)

    """
    return np.array([skimage.transform.resize(img, (size, size)) for img in images])


def scaled_gray_data_load(file_name):
    """Quick loading and processing of the data for easier training and testing
            of the NN

    Args:
        file_name (str): Name of the data directory, ex: training, testing, new_images_set1

    Returns:
        tuple: images, lables
           images (numpy.ndarray):
           each item is image of shape (new_im_size, new_im_size)
           lables (numpy.ndarray):
           each item is int label (name of the directory within file_name)

    """
    new_im_size = 28
    root_path = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))
    dir_type = f"{root_path}/data/{file_name}"
    images, labels = load_data(dir_type) # same l and w
    # resize all images to the the same l and w
    images_28_28 = resize_images(images, new_im_size) #shape (?, 28, 28, 3)
    # gray out all resized images, now shape (?, 28, 28)
    images_28_28_gray = skimage.color.rgb2gray(images_28_28)
    return images_28_28_gray, labels

# def get_gray_train_test():
#     """Quick loading and processing of the data for easier training and testing
#         of the NN
#
#     Returns:
#         tuple: images_train, lables_train, images_test, lables_test
#                images_* (numpy.ndarray): each item is image of shape (new_im_size, new_im_size)
#                lables_* (numpy.ndarray): each item is int label
#
#     """
#     new_im_size = 28
#     root_path = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))
#     train_work_dir = f"{root_path}/data/training"
#     test_work_dir = f"{root_path}/data/testing"
#     train_test = []
#     for dir_type in [train_work_dir, test_work_dir]:
#         # load raw images
#         images, labels = load_data(dir_type) # same l and w
#         # resize all images to the the same l and w
#         images_28_28 = resize_images(images, new_im_size) #shape (?, 28, 28, 3)
#         # gray out all resized images, now shape (?, 28, 28)
#         images_28_28_gray = skimage.color.rgb2gray(images_28_28)
#         train_test.append([images_28_28_gray, labels])
#             # images_train, lables_train, images_test, lables_test
#     return train_test[0][0], train_test[0][1], train_test[1][0], train_test[1][1]

# images_train, lables_train, images_test, lables_test = get_gray_train_test()
# print((lables_train[0]))
