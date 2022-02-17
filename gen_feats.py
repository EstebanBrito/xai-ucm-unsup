#from bin.feat_gen.incv1_feats import gen_incv1_feats
#from bin.feat_gen.incv3_feats import gen_incv3_feats
from bin.feat_gen import gen_feats

# TODO: Erase library loading messages when loading/using Tensorflow
if __name__ == '__main__':
    gen_feats()
