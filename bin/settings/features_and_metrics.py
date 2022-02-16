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