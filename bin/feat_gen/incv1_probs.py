import numpy as np
import os

from ..utils.models import load_model, load_imagenet_labels, fetch_model_specs, logits_to_probs
from ..utils.utils import load_images_paths, save_features_to_file, setup_folder_structure
from ..utils.image_utils import read_image_tf, preproc_image_incv1
from ..settings.folders import FEATURES_FOLDER_PATH

def gen_incv1_probs():
    # Create neccesary folders
    # setup_folder_structure()
    # Load model, model specs and labels
    model = load_model('incv1probs')
    labels = load_imagenet_labels()
    model_specs = fetch_model_specs('incv1probs')
    # Load images paths
    images_paths = load_images_paths()
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
        # DEBUG
        top = probs.numpy().argmax()
        print(image_name, labels[top])
        # Store features in features array
        features[i] = probs
        i += 1
    # Save features to file
    file_path = os.path.join(FEATURES_FOLDER_PATH, 'incv1_probs.csv')
    save_features_to_file(features, images_paths.keys(), labels, file_path)
