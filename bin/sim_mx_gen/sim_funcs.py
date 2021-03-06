import numpy as np
from math import sqrt

def euclidean_distance(a, b, is_same_vector=False):
    if is_same_vector: return 0.0
    else: return np.linalg.norm(a-b)

def class_similarity(a, b, is_same_vector=False):
    if is_same_vector: return 2.0
    res = a + b
    return  sqrt(np.sum(res*res))

def cosine_similarity(a, b, is_same_vector=False):
    # Cosine similarity is defined in [0,1] where bigger values reflect more similarirty
    # To follow a "less is closer" rule, a complement (1) is substracted from each real cosine distance
    if is_same_vector: return 0.0
    else:
        real_cos_sim = np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b))
        return 1.0 - real_cos_sim

# TODO: Mkae sure that keys in this dict. always match keys in settings.features_and_metrics.SIM_OPTIONS
sim_functions = {
    'euclid': euclidean_distance,
    'class_sim': class_similarity,
    'cosine': cosine_similarity
}

def choose_sim_function(choice):
    options = list(sim_functions.keys())
    if choice in options:
        return sim_functions[choice]
    else:
        raise ValueError("Supported values for sim. functions are:", options)