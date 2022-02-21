import os

from .incv1_feats import gen_incv1_feats
from .incv1_probs import gen_incv1_probs
from .incv3_feats import gen_incv3_feats
from .color_hist import gen_color_hist_feats
from ..utils.wizards import select_feat_gen_params, select_rewrite, YES, NO
from ..settings.features_and_metrics import FEATURE_OPTIONS

def gen_feats(path_input, path_output, feat_opt_id):
    feat_type_opts = FEATURE_OPTIONS[feat_opt_id]
    # Generate feats. according to user's selected option
    # TODO: Pass path_input, path_output to functions (remember I/O can change)
    if feat_opt_id=='incv1latfeats': gen_incv1_feats(path_input, path_output, feat_opt_id)
    elif feat_opt_id=='incv3latfeats': gen_incv3_feats(path_input, path_output, feat_opt_id)
    elif feat_opt_id=='colorhist': gen_color_hist_feats(path_input, path_output, feat_opt_id)
    else: print('Feature option not supported yet!')

