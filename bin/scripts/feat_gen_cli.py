from ..utils.wizards import select_feat_gen_params, select_rewrite, YES, NO
from ..utils.utils import get_feature_options
from ..settings.folders import IMGS_FOLDER_PATH
from ..feat_gen import gen_feats

def gen_feats_using_cli():
    print('--- FEATURE GENERATION WIZARD ---')
    feat_opt_id = select_feat_gen_params()
    print()
    feat_opts = get_feature_options(feat_opt_id)
    feat_output_file_path = feat_opts['output_file_path']
    rewrite_opt =  select_rewrite(feat_output_file_path, 'feat_gen')
    if rewrite_opt == YES:
        print('Feature generation WILL BE peformed')
        gen_feats(IMGS_FOLDER_PATH, feat_output_file_path, feat_opt_id)
        print('Feature generation finished!')
    else:
        print('Feature generation will NOT be performed again')
