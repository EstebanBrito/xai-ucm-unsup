from sim_matrix import gen_matrix
from settings import FEATURES_FOLDER_PATH, MATRICES_FOLDER_PATH
from utils import setup_folder_structure
import os

setup_folder_structure()
path_features = os.path.join(FEATURES_FOLDER_PATH, 'color_hist.csv')
path_to_save = os.path.join(MATRICES_FOLDER_PATH, 'color_hist_sim_matrix.csv')
gen_matrix(path_features, path_to_save, sim_function_name='euclidean_distance')

