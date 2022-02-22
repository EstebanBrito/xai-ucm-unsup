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
    # For each instance to instance permutation...
    total_ops, op_count = ((length * length) + length) // 2, 0
    total_ops_10_pct = total_ops // 10
    for i in range(length):
        for j in range(i, length):
            # Calc. similarity between instances and store result into matrix
            sim_score = sim_function(values[i], values[j], i==j)
            sim_matrix[i][j] = sim_score
            sim_matrix[j][i] = sim_score
            # Display progress
            op_count += 1
            if op_count % total_ops_10_pct == 0: print(f'{(op_count // total_ops_10_pct) * 10}% completed')
    return sim_matrix