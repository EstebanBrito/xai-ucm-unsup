from .feat_based_sim_mx import gen_feat_based_matrix
from ..utils.utils import get_sim_options

def gen_sim_matrix(path_input, path_output, sim_opt_id):
    sim_opts = get_sim_options[sim_opt_id]
    sim_type = sim_opts['type']
    if sim_type == 'feat_based': gen_feat_based_matrix(path_input, path_output, sim_opt_id)
    elif sim_type == 'image-based':
        print('Sim. metric type not supported yet...')
        # gen_image_based_matrix(path_input, path_output_ sim_opt_id)
    else: print('Unknown sim. metric type')
