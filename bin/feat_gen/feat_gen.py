import os

from .incv1_feats import gen_incv1_feats
from .incv1_probs import gen_incv1_probs
from .incv3_feats import gen_incv3_feats
from .color_hist import gen_color_hist_feats
from ..utils.wizards import select_feat_gen_params, select_rewrite, YES, NO
from ..settings.features_and_metrics import FEATURE_OPTIONS

def gen_feats():
    feat_type_id = select_feat_gen_params()
    feat_type_opts = FEATURE_OPTIONS[feat_type_id]
    #  Ask if user wants to rewrite prev. file if it exists
    if os.path.exists(feat_type_opts['output_file_path']):
        if select_rewrite()==NO:
            print('File will NOT be rewrited')
            return
        else: print('File WILL BE rewrited')
    # Generate feats. according to user's selected option
    if feat_type_id=='incv1latfeats': gen_incv1_feats()
    elif feat_type_id=='incv3latfeats': gen_incv3_feats()
    elif feat_type_id=='colorhist': gen_color_hist_feats()
    else: print('Option not supported yet!')

