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
