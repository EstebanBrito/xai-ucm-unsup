import os

from .incv1_feats import gen_incv1_feats
from .incv1_probs import gen_incv1_probs
from .incv3_feats import gen_incv3_feats
from .color_hist import gen_color_hist_feats
from ..utils.wizards import select_feat_gen_params
from ..settings.features_and_metrics import FEATURE_OPTIONS

def gen_feats():
    feat_type_id = select_feat_gen_params()
    # If user agrees, rewrite this
    if feat_type_id=='incv1latfeats': gen_incv1_feats()
    if feat_type_id=='incv3latfeats': gen_incv3_feats()
    if feat_type_id=='colorhist': gen_color_hist_feats()
    else: print('Option not supported yet!')

