import numpy as np
from math import sqrt

def choose_sim_function(choice):
    options = list(sim_functions.keys())
    if choice in options:
        return sim_functions[choice]
    else:
        raise ValueError("Supported values for sim. functions are:", options)

def euclidean_distance(a, b, is_same_vector=False):
    if is_same_vector: return 0.0
    else: return np.linalg.norm(a-b)

def class_similarity(a, b, is_same_vector=False):
    if is_same_vector: return 2.0
    res = a + b
    return  sqrt(np.sum(res*res))

def cosine_similarity(a, b, is_same_vector=False):
    if is_same_vector: return 1.0
    else: return np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b))

sim_functions = {
    'euclidean_distance': euclidean_distance,
    'class_similarity': class_similarity,
    'cosine_similarity': cosine_similarity
}