import numpy as np
import pandas as pd

from .sim_funcs import choose_sim_function

def gen_feat_based_matrix(path_features, path_to_save, sim_opt_id, label_col=0):
    features = pd.read_csv(path_features, index_col=label_col)
    matrix_df = create_matrix(features.values, features.index, sim_opt_id)
    matrix_df.to_csv(path_to_save)

def create_matrix(values, labels, sim_opt_id):
    sim_function = choose_sim_function(sim_opt_id)
    matrix_values = calc_matrix_values(values, sim_function)
    return pd.DataFrame(matrix_values, labels, labels)

def calc_matrix_values(values, sim_function):
    length = values.shape[0]
    sim_matrix = np.zeros(shape=(length, length))
    # Gen sim scores
    for i in range(length):
        for j in range(i, length):
            sim_score = sim_function(values[i], values[j], i==j)
            # Store into matrix
            sim_matrix[i][j] = sim_score
            sim_matrix[j][i] = sim_score
    return sim_matrix