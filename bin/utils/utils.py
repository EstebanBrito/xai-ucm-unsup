import os
import pandas as pd
import numpy as np

from ..settings.folders import IMGS_FOLDER_PATH, FEATURES_FOLDER_PATH, MATRICES_FOLDER_PATH
from ..settings.features_and_metrics import FEATURE_OPTIONS, SIM_OPTIONS

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

def get_feature_options(feat_opt_id): return FEATURE_OPTIONS[feat_opt_id].copy()

def get_sim_options(sim_opt_id): return SIM_OPTIONS[sim_opt_id].copy()
