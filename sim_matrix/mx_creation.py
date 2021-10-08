import numpy as np
import pandas as pd

from .sim_funcs import choose_sim_function

def gen_matrix(path_features, path_to_save, label_col=0, sim_function_name='euclidean_distance'):
    features = pd.read_csv(path_features, index_col=label_col)
    matrix_df = create_matrix(features.values, features.index, sim_function_name)
    matrix_df.to_csv(path_to_save)
    return

def create_matrix(values, labels, sim_function_name):
    sim_function = choose_sim_function(sim_function_name)
    matrix = calc_matrix(values, sim_function)
    matrix_df = pd.DataFrame(matrix, labels, labels)
    return matrix_df

def calc_matrix(values, sim_function):
    length = values.shape[0]
    sim_matrix = np.zeros(shape=(length, length))
    # Gen sim scores
    count = 0
    for i in range(length):
        for j in range(i, length):
            sim_score = sim_function(values[i], values[j], i==j)
            # Store into matrix
            sim_matrix[i][j] = sim_score
            sim_matrix[j][i] = sim_score
    return sim_matrix


