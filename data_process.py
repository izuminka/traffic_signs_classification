import os
import skimage
import random # for random.seed sampling of the images

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
    for label in group_labels:
        file_paths_group = [f"{data_dir}/{label}/{f}" for f in
                            os.listdir(f"{data_dir}/{label}") if f.endswith(".ppm")]
        for image_file in file_paths_group:
            images.append(skimage.data.imread(image_file))
            labels.append(int(label))
    return images, labels

def resize_images(images, size):
    """Resize a list of images to the same lenth and width

    Args:
        images (list): each image (numpy.ndarray) of ndim 3, various l,w
        size (type): Description of parameter `size`.

    Returns:
        list: each image (numpy.ndarray) of ndim 3 with l=w=size

    """
    return [skimage.transform.resize(img, (size, size)) for img in images]

if __name__ == '__main__':
    from data_analysis import get_sample_images
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))
    train_work_dir = f"{ROOT_PATH}/data/training"
    test_work_dir = f"{ROOT_PATH}/data/testing"
    images, labels = load_data(train_work_dir)

    random.seed(0)
    get_sample_images(5, images)

    random.seed(0)
    NEW_IM_SIZE = 28
    images_28_28 = resize_images(images, NEW_IM_SIZE)
    get_sample_images(5, images_28_28)
