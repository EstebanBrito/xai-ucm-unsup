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
    },
    'incv3feats': {
        'name': 'inceptionv3',
        'input_size': [1, 299, 299, 3],
        'output_size': [1, 2048],
        'handle': 'https://tfhub.dev/google/imagenet/inception_v3/feature_vector/5'
    }
}
IMAGENET_LABELS_URL = 'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'

# FOLDER STRUCTURE
IMGS_FOLDER_NAME = 'imgs'
FEATURES_FOLDER_NAME = 'features'
MATRICES_FOLDER_NAME = 'matrices'
IMGS_FOLDER_PATH = os.path.join('.', IMGS_FOLDER_NAME)
FEATURES_FOLDER_PATH = os.path.join('.', FEATURES_FOLDER_NAME)
MATRICES_FOLDER_PATH = os.path.join('.', MATRICES_FOLDER_NAME)

# ARTIFACT NAMES ("key to description" dictionaries)
FEATURES_NAMES = {
    'incv3latfeats': 'InceptionV3 Latent Features',
    'incv1latfeats': 'InceptionV1 Latent Features',
    'colorhist': 'Color Histogram',
    'pixels': 'Pixels (select for SSIM)'
}

SIM_METRICS_NAMES = {
    'euclid': 'Euclidian Distance',
    'cosine': 'Cosine Similarity',
    'ssim': 'Structural Similarity (SSIM)',
}

UNALLOWED_COMBINATIONS = (
    ('incv3latfeats', 'ssim'),
    ('incv1latfeats', 'ssim'),
    ('colorhist', 'ssim'),
    ('pixels', 'euclid'),
    ('pixels', 'cosine'),
    ('pixels', 'ssim'),
)