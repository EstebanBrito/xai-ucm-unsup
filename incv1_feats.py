import tensorflow as tf
import numpy as np
import os

from models import load_model, load_imagenet_labels, fetch_model_specs, logits_to_probs
from utils import load_images_paths, save_features_to_file, setup_folder_structure
from image_utils import read_image_tf, preproc_image_incv1
from settings import FEATURES_FOLDER_PATH

# Create neccesary folders
setup_folder_structure()
# Load model, model specs and labels
model = load_model('incv1feats')
model_specs = fetch_model_specs('incv1feats')
# Load images paths
images_paths = load_images_paths()
# Create features array
output_size = model_specs['output_size']
features = np.zeros(shape=(len(images_paths), output_size[1]))
# For each image path...
i = 0
for image_name, image_path in images_paths.items():
    # ... read the image and gen. features from it
    image = read_image_tf(image_path)
    image = preproc_image_incv1(image)
    feats = model(image)
    # DEBUG
    feats.shape
    # Store features in features array
    features[i] = feats.numpy()
    i += 1
# Save features to file
file_path = os.path.join(FEATURES_FOLDER_PATH, 'incv1_feats.csv')
save_features_to_file(features, images_paths.keys(), range(1024), file_path)