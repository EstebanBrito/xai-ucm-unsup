import os

# FOLDER NAMES
IMGS_FOLDER_NAME = 'imgs'
RESULTS_FOLDER_NAME = 'results'
FEATURES_FOLDER_NAME = 'features'
MATRICES_FOLDER_NAME = 'matrices'
# FOLDER STRUCTURE
ABSOLUTE_PATH = os.path.abspath('.')
ROOT_FOLDER_PATH = ABSOLUTE_PATH
IMGS_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, IMGS_FOLDER_NAME)
RESULTS_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, RESULTS_FOLDER_NAME)
FEATURES_FOLDER_PATH = os.path.join(RESULTS_FOLDER_PATH, FEATURES_FOLDER_NAME)
MATRICES_FOLDER_PATH = os.path.join(RESULTS_FOLDER_PATH, MATRICES_FOLDER_NAME)