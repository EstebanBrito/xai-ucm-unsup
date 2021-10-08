import os
import pandas as pd
import numpy as np

from settings import IMGS_FOLDER_PATH, FEATURES_FOLDER_PATH, MATRICES_FOLDER_PATH

def setup_folder_structure():
    if not os.path.isdir(IMGS_FOLDER_PATH):
        os.mkdir(IMGS_FOLDER_PATH)
    if not os.path.isdir(FEATURES_FOLDER_PATH):
        os.mkdir(FEATURES_FOLDER_PATH)
    if not os.path.isdir(MATRICES_FOLDER_PATH):
        os.mkdir(MATRICES_FOLDER_PATH)

def craft_path_to_curr_dir(name):
    return os.path.join('.', name)

def file_is_image(img_name):
    return img_name.split('.')[-1]=='jpeg' or img_name.split('.')[-1]=='jpg'

def load_images_paths(folder_path=IMGS_FOLDER_PATH):
    img_paths = {img_name: os.path.join(folder_path, img_name) for img_name in os.listdir(folder_path) if file_is_image(img_name)}
    return img_paths

def save_features_to_file(values, row_labels, col_labels, file_path):
    dataframe = pd.DataFrame(data=values, index=row_labels, columns=col_labels)
    dataframe.to_csv(file_path)
    return dataframe

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
