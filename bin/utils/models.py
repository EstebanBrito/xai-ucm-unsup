import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

from ..settings.models import MODELS_SPECS, IMAGENET_LABELS_URL

def fetch_model_specs(model_id):
    return MODELS_SPECS[model_id].copy()

def load_model(model_id):
    model_specs = MODELS_SPECS[model_id]
    model = tf.keras.Sequential([
        hub.KerasLayer(
            name=model_specs['name'],
            handle=model_specs['handle'],
            trainable=False
        )
    ])
    model.build(input_shape=model_specs['input_size'])
    return model

def logits_to_probs(logits):
    return tf.nn.softmax(logits, axis=1)

def load_imagenet_labels(file_path=IMAGENET_LABELS_URL):
    labels_file = tf.keras.utils.get_file('ImageNetLabels.txt', file_path)
    with open(labels_file) as reader:
        f = reader.read()
        labels = f.splitlines()
    return np.array(labels)