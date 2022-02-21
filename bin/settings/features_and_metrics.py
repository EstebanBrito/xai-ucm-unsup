import os

from .folders import FEATURES_FOLDER_PATH, MATRICES_FOLDER_PATH

# TODO: Make sure output_file_name and output_file_path always match
# If I make these options objects, I can create output_file_path on initialization...
FEATURE_OPTIONS = {
    'incv1latfeats': {
        'description': 'InceptionV1 Latent Features',
        'type': 'model-based',
        'model_id': 'incv1feats',
        'output_file_name': 'incv1_feats',
        'output_file_path': os.path.join(FEATURES_FOLDER_PATH, 'incv1_feats.csv'),
    },
    'incv3latfeats': {
        'description': 'InceptionV3 Latent Features',
        'type': 'model-based',
        'model_id': 'incv3feats',
        'output_file_name': 'incv3_feats',
        'output_file_path': os.path.join(FEATURES_FOLDER_PATH, 'incv3_feats.csv')
    },
    'colorhist': {
        'description': 'Color Histograms',
        'type': 'image-based',
        'output_file_name': 'color_hist',
        'output_file_path': os.path.join(FEATURES_FOLDER_PATH, 'color_hist.csv')
    }
}

# feat_based sim. options must have a 'output_file_name_suffix' property
# all other sim. options must have a 'output_file_path' property
SIM_OPTIONS = {
    'euclid': {
        'description': 'Euclidian Distance',
        'type': 'feat-based',
        'output_file_name_suffix': 'euclid_sim_matrix.csv'
    },
    'cosine': {
        'description': 'Cosine Distance',
        'type': 'feat-based',
        'output_file_name_suffix': 'cosine_sim_matrix.csv'
    },
    'class_sim': {
        'description': 'Class Similarity',
        'type': 'feat-based',
        'output_file_name_suffix': 'class_sim_matrix.csv'
    },
    'ssim': {
        'description': 'Structural Similarity (SSIM)',
        'type': 'image-based',
        'output_file_path': os.path.join(MATRICES_FOLDER_PATH, 'ssim_matrix.csv')
    },
}