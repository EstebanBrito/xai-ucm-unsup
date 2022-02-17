import os

from ..settings.features_and_metrics import FEATURES_NAMES, SIM_METRICS_NAMES, UNALLOWED_COMBINATIONS

def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')

def select_option():
    try: opt = int(input('Enter a number: '))
    except Exception: return -1
    else: return opt   

def select_feat_gen_params():
    selection_map = {i: feat_key for i, feat_key in enumerate(FEATURES_NAMES.keys())}
    print('Please, select what kind of features you want to use')
    print('to use in the process...')
    print()
    for opt_key, feat_key in selection_map.items():
        print(f'[ {opt_key} ] --- {FEATURES_NAMES[feat_key]}')
    while True:
        sel_opt_key = select_option()
        if sel_opt_key in selection_map.keys(): break
        else: print('   Unavailable option. Try again.')
    return selection_map[sel_opt_key]

def select_sim_mx_gen_params():
    selection_map = {i: sim_key for i, sim_key in enumerate(SIM_METRICS_NAMES.keys())}
    print('Please, select what similirity metric you want')
    print('to use in the process...')
    print()
    for opt_key, sim_key in selection_map.items():
        print(f'[ {opt_key} ] --- {SIM_METRICS_NAMES[sim_key]}')
    while True:
        sel_opt_key = select_option()
        if sel_opt_key in selection_map.keys(): break
        else: print('   Unavailable option. Try again.')
    return selection_map[sel_opt_key]

def select_feat_and_sim_mx_gen_params():
    '''Asks the user what kind of features are needed and returns 
    feature generation parameters for other functions to use'''
    print('----SIMILARITY MATRIX GENERATION WIZARD----')
    sel_feat_key = select_feat_gen_params()
    clear_screen()
    sel_sim_key = select_sim_mx_gen_params()
    clear_screen()
    if (sel_feat_key, sel_sim_key) in UNALLOWED_COMBINATIONS:
        print('This combination of features is not allowed/supported:')
        print(f'- {FEATURES_NAMES[sel_feat_key]} with {SIM_METRICS_NAMES[sel_sim_key]}')
        print('Please, run the script again and choose avaliable options...')
        exit(0)
    return sel_feat_key, sel_sim_key