import os
import pandas as pd
import numpy as np

from ..settings.folders import IMGS_FOLDER_PATH, FEATURES_FOLDER_PATH, MATRICES_FOLDER_PATH
from ..settings.features_and_metrics import FEATURES_NAMES, SIM_METRICS_NAMES, UNALLOWED_COMBINATIONS

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

def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')

def select_option():
    try: opt = int(input('Enter a number: '))
    except Exception: return -1
    else: return opt   

def select_feat_type_params():
    selection_map = {i: feat_key for i, feat_key in enumerate(FEATURES_NAMES.keys())}
    print('Please, select what kind of features you want to use')
    print('to use in the process...')
    print()
    for opt_key, feat_key in selection_map.items():
        print(f'[ {opt_key} ] --- {FEATURES_NAMES[feat_key]}')
    while True:
        sel_opt_key = select_option()
        if sel_opt_key in selection_map.keys(): break
        else: print('   Unavailable option. Try again.')
    return selection_map[sel_opt_key]

def select_sim_metric_params():
    selection_map = {i: sim_key for i, sim_key in enumerate(SIM_METRICS_NAMES.keys())}
    print('Please, select what similirity metric you want')
    print('to use in the process...')
    print()
    for opt_key, sim_key in selection_map.items():
        print(f'[ {opt_key} ] --- {SIM_METRICS_NAMES[sim_key]}')
    while True:
        sel_opt_key = select_option()
        if sel_opt_key in selection_map.keys(): break
        else: print('   Unavailable option. Try again.')
    return selection_map[sel_opt_key]

def select_feat_generation_params():
    '''Asks the user what kind of features are needed and returns 
    feature generation parameters for other functions to use'''
    print('----SIMILARITY MATRIX GENERATION WIZARD----')
    sel_feat_key = select_feat_type_params()
    clear_screen()
    sel_sim_key = select_sim_metric_params()
    clear_screen()
    if (sel_feat_key, sel_sim_key) in UNALLOWED_COMBINATIONS:
        print('This combination of features is not allowed/supported:')
        print(f'- {FEATURES_NAMES[sel_feat_key]} with {SIM_METRICS_NAMES[sel_sim_key]}')
        print('Please, run the script again and choose avaliable options...')
        exit(0)
    return sel_feat_key, sel_sim_key