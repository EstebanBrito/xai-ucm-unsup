import os

from ..utils.wizards import select_sim_mx_and_feat_gen_params, select_rewrite, YES, NO
from ..utils.utils import get_feature_options, get_sim_options, craft_sim_mx_output_file_path, get_sim_mx_input_path
from ..settings.folders import IMGS_FOLDER_PATH, MATRICES_FOLDER_PATH
from ..feat_gen import gen_feats
from ..sim_mx_gen import gen_sim_matrix

def gen_sim_matrix_using_cli():
    # Ask for operation parameters
    print('--- SIMILARITY MATRIX GENERATION WIZARD ---')
    sim_opt_id, feat_opt_id = select_sim_mx_and_feat_gen_params()
    # Fetch details of selected options
    sim_opts = get_sim_options(sim_opt_id)
    feat_opts = None if feat_opt_id == None else get_feature_options(feat_opt_id)
    # Craft similarity matrix file path for later use
    sim_mx_file_path = craft_sim_mx_output_file_path(sim_opt_id, feat_opt_id)
    # Ask user if similarity matrix generation is to be repeated
    rewrite_sim_mx = select_rewrite(sim_mx_file_path, 'sim_mx_gen', sim_opt_id)
    if rewrite_sim_mx == YES:
        # If features are involved in sim. mx. gen. process, ask user if feat. gen. is to be repeated
        if feat_opt_id != None:
            rewrite_feats = select_rewrite(feat_opts['output_file_path'], 'feat_gen', feat_opt_id)
            if rewrite_feats == YES:
                # Generate feats. again if user wants to
                print('\nFeatures will be generated first!\n')
                gen_feats(IMGS_FOLDER_PATH, feat_opts['output_file_path'], feat_opt_id)
            else: print('\nFeatures will NOT be generated again!')
        # Define sim. mx. data input according to similarity type
        sim_mx_input_path = get_sim_mx_input_path(sim_opt_id, feat_opt_id)
        # Generate similarity matrix at the end
        print('\nNow sim. matrix WILL be generated!\n')
        gen_sim_matrix(sim_mx_input_path, sim_mx_file_path, sim_opt_id)
        print('\nSim. matrix generated. Process finished!\n')
    else:
        print('Sim. matrix will NOT be generated again')
