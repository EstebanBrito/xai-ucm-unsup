import numpy as np
import os
from skimage.io import imread

from utils import load_images_paths, save_features_to_file, setup_folder_structure, comp_color_hist
from settings import FEATURES_FOLDER_PATH

# Create neccesary folders
setup_folder_structure()
# Load images paths
images_paths = load_images_paths()
# Create features array
features = np.zeros(shape=(len(images_paths), 256*3), dtype='uint32')
# For each image path...
i = 0
for image_name, image_path in images_paths.items():
    # ... read the image and gen. features from it
    image = imread(image_path)
    hist = comp_color_hist(image)
    # Store features in features array
    features[i] = hist
    i += 1
# Save features to file
file_path = os.path.join(FEATURES_FOLDER_PATH, 'color_hist.csv')
save_features_to_file(features, images_paths.keys(), range(256*3), file_path)