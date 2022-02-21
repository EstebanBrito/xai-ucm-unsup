import os

from ..settings.features_and_metrics import FEATURE_OPTIONS, SIM_OPTIONS, UNALLOWED_COMBINATIONS

YES, NO = 1, 0

def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')

def select_option():
    try: opt = int(input('Enter a number: '))
    except Exception: return -1
    else: return opt   

def select_rewrite(file_path, op_type):
    if os.path.exists(file_path):
        # TODO: Make prompt message more clear
        oper = 'SIM. MATRIX GENERATION' if op_type == 'sim_mx_gen' else 'FEATURE GENERATION'
        print(f'A {oper} process was performed before using those options.')
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
        print(f'[ {opt_key} ] --- {SIM_OPTIONS[sim_key]}')
    while True:
        sel_opt_key = select_option()
        if sel_opt_key in selection_map.keys(): break
        else: print('Unavailable option. Try again.')
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
        print(f'- {FEATURE_OPTIONS[sel_feat_key].description} with {SIM_OPTIONS[sel_sim_key]}')
        print('Please, run the script again and choose avaliable options...')
        exit(0)
    return sel_feat_key, sel_sim_key