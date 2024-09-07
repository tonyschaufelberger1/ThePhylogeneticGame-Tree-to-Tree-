from FeatureExtractor.FeatureExtractorFeatureToolBox import FeatureExtractorFeatureToolBoxClass
from FeatureExtractor.FeatureExtractor import FeatureExtractorClass
from Reinforcement_env.env_utils import PhyloGameUtils
from SPR_generator.SPR_move import Edge

fe = FeatureExtractorClass()

helper = PhyloGameUtils(feature_extractor_instance=fe, datasets=None, use_random_starts=False, results_dir="./experiments_results/feature_extraction_test")

input_tree = helper.get_starting_tree()

FTB = FeatureExtractorFeatureToolBoxClass(current_tree=input_tree, prune_tree=None,
                                                                      remaining_tree=None, b_subtree=None,
                                                                      c_subtree=None, data_set_number=199,
                                                                      resulting_tree=None,
                                                                      split_hash_dict={})

print(FTB.features_bl_dana(which_tree='current_tree'))
tree_results = {name: 0 for name in FTB.tree_mappings['current_tree'].keys() if name.find('ll') == -1}
# print(tree_results)

