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

def craft_sim_mx_output_file_path(sim_opt_id, feat_opt_id):
    sim_opts = get_sim_options(sim_opt_id)
    if feat_opt_id == None: return sim_opts['output_file_path']
    else:
        sim_file_name_suffix = sim_opts['output_file_name_suffix']
        feat_file_name_preffix = get_feature_options(feat_opt_id)['output_file_name']
        sim_file_name = feat_file_name_preffix + '_' + sim_file_name_suffix
        return os.path.join(MATRICES_FOLDER_PATH, sim_file_name)

def get_sim_mx_input_path(sim_opt_id, feat_opt_id):
    sim_type = get_sim_options(sim_opt_id)['type']
    if sim_type == 'feat-based': return get_feature_options(feat_opt_id)['output_file_path']
    elif sim_type == 'image-based': return IMGS_FOLDER_PATH
    else: print('Unknown sim. metric type')

