import matplotlib.pylab as plt
import random

def get_sample_images(num_rand_samples, images):
    """Get a taste of the images in the data. Print out num_rand_samples images

    Args:
        num_rand_samples (int): Number of images to print
        images (list): with each image (numpy.ndarray)

    """
    inds_rand_im = random.sample(range(0, len(images)), num_rand_samples)
    for i, im_ind in enumerate(inds_rand_im):
        plt.subplot(1, num_rand_samples, i + 1) # disp a 1 row of images
        plt.subplots_adjust(wspace=0.3) # print out a bit of space btw images
        plt.axis("off") # no x,y axis
        plt.imshow(images[im_ind])

if __name__ == '__main__':
    from data_import import load_data
    ROOT_PATH = os.path.dirname(os.path.realpath("__file__"))
    train_work_dir = f"{ROOT_PATH}/data/training"
    test_work_dir = f"{ROOT_PATH}/data/testing"
    images, labels = load_data(train_work_dir)

# # Print out the hostorgram of the image labels
# NUM_CLASSES = 62
# plt.hist(labels, NUM_CLASSES)


# # Get a tast of the image for each label
# plt.figure(figsize=(15, 15))
# for i, lab in enumerate(set(labels)):
#     image = images[labels.index(lab)] # get first occured labled image in the list
#     plt.subplot(8, 8, i+1)
#     plt.title(f"Num: {str(labels.count(lab))}")
#     plt.imshow(image)
#     plt.axis("off")
