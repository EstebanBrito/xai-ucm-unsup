import os

from .folders import FEATURES_FOLDER_PATH

# ARTIFACT NAMES ("key to description" dictionaries)
FEATURES_NAMES = {
    'incv3latfeats': 'InceptionV3 Latent Features',
    'incv1latfeats': 'InceptionV1 Latent Features',
    'colorhist': 'Color Histogram',
    'pixels': 'Pixels (select for SSIM)'
}

FEATURE_OPTIONS = {
    'incv1latfeats': {
        'description': 'InceptionV1 Latent Features',
        'type': 'model-based',
        'model_id': 'incv1feats',
        'output_file_path': os.path.join(FEATURES_FOLDER_PATH, 'incv1_feats.csv')
    },
    'incv3latfeats': {
        'description': 'InceptionV3 Latent Features',
        'type': 'model-based',
        'model_id': 'incv3feats',
        'output_file_path': os.path.join(FEATURES_FOLDER_PATH, 'incv3_feats.csv')
    },
    'colorhist': {
        'description': 'Description',
        'type': 'hist-based',
        'output_file_path': os.path.join(FEATURES_FOLDER_PATH, 'color_hist.csv')
    }
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