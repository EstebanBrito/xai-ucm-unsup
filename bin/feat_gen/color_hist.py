import numpy as np
import os
from skimage.io import imread

from ..utils.utils import load_images_paths, save_features_to_file, get_feature_options
from ..settings.folders import FEATURES_FOLDER_PATH

def comp_color_hist(img):
    freqs_global = np.zeros((256*3), dtype='uint32')
    for k in range(img.shape[2]):
        freqs_comp = np.zeros((256), dtype='uint32')
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                value = img[i,j,k]
                freqs_comp[value] += 1
        start, end = k*256, (k+1)*256
        freqs_global[start:end] = freqs_comp
    return freqs_global 

def gen_color_hist_feats(path_input, path_output, feat_opt_id):
    feat_opts = get_feature_options(feat_opt_id)
    # Load images paths
    images_paths = load_images_paths(path_input)
    # Create features array
    features = np.zeros(shape=(len(images_paths), 256*3), dtype='uint32')
    # For each image path...
    i = 0
    for image_name, image_path in images_paths.items():
        # ... read the image and gen. features from it
        image = imread(image_path)
        hist = comp_color_hist(image)
        print(image_name) # DEBUG
        # Store features in features array
        features[i] = hist
        i += 1
    # Save features to file
    # file_path = os.path.join(FEATURES_FOLDER_PATH, 'color_hist.csv')
    save_features_to_file(features, images_paths.keys(), range(256*3), path_output)