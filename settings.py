import os

# MODELS SETTINGS
MODELS_SPECS = {
    'incv1probs' : {
        'name': 'inceptionv1',
        'input_size': [1, 224, 224, 3],
        'output_size': [1, 1001],
        'handle': 'https://tfhub.dev/google/imagenet/inception_v1/classification/4'
    },
    'incv1feats' : {
        'name': 'inceptionv1',
        'input_size': [1, 224, 224, 3],
        'output_size': [1, 1024],
        'handle': 'https://tfhub.dev/google/imagenet/inception_v1/feature_vector/4'
    }
}
IMAGENET_LABELS_URL = 'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'

# FOLDER STRUCTURE
IMGS_FOLDER_NAME = 'imgs'
FEATURES_FOLDER_NAME = 'features'
IMGS_FOLDER_PATH = os.path.join('.', IMGS_FOLDER_NAME)
FEATURES_FOLDER_PATH = os.path.join('.', FEATURES_FOLDER_NAME)