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
