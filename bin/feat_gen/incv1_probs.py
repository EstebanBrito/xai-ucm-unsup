import numpy as np
import os

from ..utils.models import load_model, load_imagenet_labels, fetch_model_specs, logits_to_probs
from ..utils.utils import load_images_paths, save_features_to_file, get_feature_options
from ..utils.image_utils import read_image_tf, preproc_image_incv1
from ..settings.folders import FEATURES_FOLDER_PATH

def gen_incv1_probs(path_input, path_output, feat_opt_id):
    feat_opts = get_feature_options(feat_opt_id)
    # Load model, model specs and labels
    model = load_model(feat_opts['model_id'])
    labels = load_imagenet_labels()
    model_specs = fetch_model_specs(feat_opts['model_id'])
    # Load images paths
    images_paths = load_images_paths(path_input)
    # Create features array
    output_size = model_specs['output_size']
    features = np.zeros(shape=(len(images_paths), output_size[1]), dtype='float32')
    # For each image path...
    i = 0
    for image_name, image_path in images_paths.items():
        # ... read the image and gen. features from it
        image = read_image_tf(image_path)
        image = preproc_image_incv1(image)
        preds = model(image)
        probs = logits_to_probs(preds)
        top = probs.numpy().argmax()
        print(image_name, labels[top]) # DEBUG
        # Store features in features array
        features[i] = probs
        i += 1
    # Save features to file
    # file_path = os.path.join(FEATURES_FOLDER_PATH, path_output)
    save_features_to_file(features, images_paths.keys(), labels, path_output)
