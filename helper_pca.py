import os
from skimage.io import imread
import numpy as np

def load_images(main_folder_path):
    images_per_folder, test_images_per_folder = {}, {}
    folder_names = os.listdir(main_folder_path)
    for folder_name in folder_names:
        folder_path = os.path.join(main_folder_path, folder_name)
        image_names = os.listdir(folder_path)
        # Load and store "train" images
        images_per_image_name = {}
        for image_name in image_names:
            image_path = os.path.join(folder_path, image_name)
            image = imread(image_path)
            images_per_image_name[image_name] = image
        images_per_folder[folder_name] = images_per_image_name
        # Load and store "test" images
        test_images_per_image_name = {}
        for image_name in image_names[-1:]:
            image_path = os.path.join(folder_path, image_name)
            image = imread(image_path)
            test_images_per_image_name[image_name] = image
        test_images_per_folder[folder_name] = test_images_per_image_name
    return images_per_folder, test_images_per_folder

def get_pca_input(images):
    pca_per_class = {}
    img_data_per_class = {}
    for image_class, image_name_pairs  in images.items():
        # Get image data array from class
        images_data = []
        for _, image in image_name_pairs.items():
            images_data.append(np.reshape(image, newshape=-1))
        images_data = np.array(images_data)
        # print(image_class, '-', images_data.shape)
        # Apply PCA and store results
        # pca = PCA() # THIS WILL FAIL IF NO. OF SAMPLES IS < 5 (for sklearn's PCA)
        '''
        new_images_data = pca.fit_transform(images_data)
        pca_per_class[image_class] = {
            'pca_object' : pca,
            'projections' : new_images_data
        }
        '''
        img_data_per_class[image_class] = images_data
    return pca_per_class, img_data_per_class