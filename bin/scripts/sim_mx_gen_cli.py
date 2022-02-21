import os

from ..utils.wizards import select_sim_mx_and_feat_gen_params, select_rewrite, YES, NO
from ..utils.utils import get_feature_options, get_sim_options
from ..settings.folders import IMGS_FOLDER_PATH, MATRICES_FOLDER_PATH
from ..feat_gen import gen_feats
from ..sim_mx_gen import gen_sim_matrix

def gen_sim_matrix_using_cli():
    print('--- SIMILARITY MATRIX GENERATION WIZARD ---')
    sim_opt_id, feat_opt_id = select_sim_mx_and_feat_gen_params()
    sim_opts = get_sim_options(sim_opt_id)
    feat_opts = None if feat_opt_id == None else get_feature_options(feat_opts)
    # Craft sim. mx. file path for later use
    if feat_opt_id == None: sim_mx_file_path = sim_opts['output_file_path']
    else:
        # TODO: Take this code to utils
        feat_file_name = feat_opts['output_file_name']
        sim_mx_file_name = feat_file_name + '_' + sim_opts['output_file_name_suffix']
        sim_mx_file_path = os.path.join(MATRICES_FOLDER_PATH, sim_mx_file_name)
    # Ask user if sim. mx. gen. is to be repeated
    rewrite_sim_mx = select_rewrite(sim_mx_file_path, 'sim_mx_gen')
    if rewrite_sim_mx == NO:
        print('Sim. matrix will NOT be generated again')
        return
    else:
        # If features are involved in sim. mx. process, ask user if feat. gen. is to be repeated
        if feat_opt_id != None:
            rewrite_feats = select_rewrite(feat_opts['output_file_path'], 'feat_gen')
            if rewrite_feats == YES: gen_feats()
        # Generate matrix, according to if sim. option is based on images or features
        if sim_opts['type'] == 'feat_based': sim_mx_input_path = feat_opts['output_file_path']
        elif sim_opts['type'] == 'image_based': sim_mx_input_path = IMGS_FOLDER_PATH
        gen_sim_matrix(sim_mx_input_path, sim_mx_file_path, sim_opt_id)
