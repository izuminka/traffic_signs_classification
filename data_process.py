import os
import skimage

def load_data(data_dir):
    """Load images and labels

    Args:
        data_dir (str): path to the data

    Returns:
        tuple: images (list) of image (numpy.ndarray),
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

if __name__ == '__main__':
    from data_analysis import get_sample_images
    ROOT_PATH = os.path.dirname(os.path.realpath("__file__"))
    train_work_dir = f"{ROOT_PATH}/data/training"
    test_work_dir = f"{ROOT_PATH}/data/testing"
    images, labels = load_data(train_work_dir)

    images_28_28 = [skimage.transform.resize(img, (28,28)) for img in images]
    get_sample_images(5, images_28_28)
