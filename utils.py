import os
import pandas as pd

from settings import IMGS_FOLDER_PATH

def setup_folder_structure():
    pass

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
