from .incv1_feats import gen_incv1_feats
from .incv1_probs import gen_incv1_probs
from .incv3_feats import gen_incv3_feats
from .color_hist import gen_color_hist_feats
from ..utils.utils import get_feature_options

def gen_feats(path_input, path_output, feat_opt_id):
    feat_opts = get_feature_options(feat_opt_id)
    # Generate feats. according to user's selected option
    # TODO: Refactor gen. funcs. into more generic ones (gen_model_based_feats, gen_image_based_feats, etc)
    if feat_opt_id=='incv1latfeats': gen_incv1_feats(path_input, path_output, feat_opt_id)
    elif feat_opt_id=='incv3latfeats': gen_incv3_feats(path_input, path_output, feat_opt_id)
    elif feat_opt_id=='colorhist': gen_color_hist_feats(path_input, path_output, feat_opt_id)
    else: print('Feature option not supported yet!')

