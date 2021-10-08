import numpy as np

def choose_sim_function(choice):
    options = list(sim_functions.keys())
    if choice in options:
        return sim_functions[choice]
    else:
        raise ValueError("Supported values for sim. functions are:", options)

def euclidean_distance(a, b, is_same_vector=False):
    if is_same_vector: return 0
    else: return np.linalg.norm(a-b)

sim_functions = {
    'euclidean_distance': euclidean_distance
}