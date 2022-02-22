import os

from ..utils.utils import get_feature_options, get_sim_options
from ..settings.features_and_metrics import FEATURE_OPTIONS, SIM_OPTIONS

YES, NO = 1, 0

def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')

def select_option():
    try: opt = int(input('Enter a number: '))
    except Exception: return -1
    else: return opt   

def select_rewrite(file_path, op_type, opt_id):
    if os.path.exists(file_path):
        # Operation type
        if op_type == 'sim_mx_gen':
            opts = get_sim_options(opt_id)
            oper = 'SIM. MATRIX GENERATION'
        elif op_type == 'feat_gen':
            opts = get_feature_options(opt_id)
            oper = 'FEATURE GENERATION'
        else: print('Unknown operation')
        # TODO: Make prompt message more clear
        print(f"A {oper} process was performed before using {opts['description']}")
        print(' Would you like to repeat this process or use the existing results?')
        print('[ 0 ] - Use existing results')
        print('[ 1 ] - Repeat process')
        while True:
            opt = select_option()
            if opt==0: return NO
            elif opt==1: return YES
            else: print('Select a valid option. Try again.')
    else:
        return YES     

def select_feat_gen_params():
    selection_map = {i: feat_key for i, feat_key in enumerate(FEATURE_OPTIONS.keys())}
    print('Please, select what kind of features you want to use')
    print('to use in the process...')
    print()
    for opt_key, feat_key in selection_map.items():
        print(f"[ {opt_key} ] --- {FEATURE_OPTIONS[feat_key]['description']}")
    print()
    while True:
        sel_opt_key = select_option()
        if sel_opt_key in selection_map.keys(): break
        else: print('Unavailable option. Try again.')
    return selection_map[sel_opt_key]

def select_sim_mx_gen_params():
    selection_map = {i: sim_key for i, sim_key in enumerate(SIM_OPTIONS.keys())}
    print('Please, select what similirity metric you want')
    print('to use in the process...')
    print()
    for opt_key, sim_key in selection_map.items():
        print(f"[ {opt_key} ] --- {SIM_OPTIONS[sim_key]['description']}")
    while True:
        sel_opt_key = select_option()
        if sel_opt_key in selection_map.keys(): break
        else: print('Unavailable option. Try again.')
    return selection_map[sel_opt_key]

def select_sim_mx_and_feat_gen_params():
    '''Asks the user what kind of features are needed and returns 
    feature generation parameters for other functions to use'''
    # Select similarity option
    sel_sim_key = select_sim_mx_gen_params()
    clear_screen()
    # Select feature option (if sim. option supports it)
    sim_type = get_sim_options(sel_sim_key)['type']
    if sim_type == 'feat-based':
        sel_feat_key = select_feat_gen_params()
        clear_screen()
    else: sel_feat_key = None
    # Return info
    return sel_sim_key, sel_feat_key