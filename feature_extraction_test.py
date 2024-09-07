from FeatureExtractor.FeatureExtractor import FeatureExtractorClass
from Reinforcement_env.env_utils import PhyloGameUtils
from SPR_generator.SPR_move import Edge

fe = FeatureExtractorClass()

helper = PhyloGameUtils(feature_extractor_instance=fe, datasets=None, use_random_starts=False, results_dir="./experiments_results/feature_extraction_test")

input_tree = helper.get_starting_tree()
# likelihood = fe.extract_likelihood(input_tree, helper.data_set)['resulting_ll'][0]

print(input_tree)

prev_node = None

i = 0

prune_edge = None
rgft_edge = None

for node in input_tree.traverse():
    i += 1
    if i == 4:
        prune_edge = Edge(node.name, prev_node.name)
    if i == 6:
        rgft_edge = Edge(node.name, prev_node.name)
        break
    prev_node = node

print(prune_edge, rgft_edge)

tree_features = fe.extract_features(input_tree, [prune_edge, rgft_edge], calculation_flag='features', split_hash_dict={})
print(tree_features)

# print(likelihood)
