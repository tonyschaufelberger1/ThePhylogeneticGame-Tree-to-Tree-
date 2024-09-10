from FeatureExtractor.FeatureExtractor import FeatureExtractorClass
from Reinforcement_env.env_utils import PhyloGameUtils
from SPR_generator.SPR_move import Edge
# from tqdist import *
# from Espalier import MAF
# import dendropy
import subprocess

fe = FeatureExtractorClass()

helper = PhyloGameUtils(feature_extractor_instance=fe, datasets=None, use_random_starts=True, results_dir="./experiments_results/feature_extraction_test")

# likelihood = fe.extract_likelihood(input_tree, helper.data_set)['resulting_ll'][0]

species_input = 0

species_target = set()

target_tree = helper.get_starting_tree()

for node in target_tree.iter_descendants():
    if node.is_leaf():
        species_target.add(node.name)


while species_input != species_target:
    species_input = set()

    input_tree = helper.get_starting_tree()

    for node in input_tree.iter_descendants():
        if node.is_leaf():
            species_input.add(node.name)

    # print(species_input)
    print(species_target == species_input)

subprocess.call("touch test1.in", shell=True)
subprocess.call(f"echo '{input_tree.write(format=1)}' > test1.in", shell=True)
subprocess.call(f"echo '{target_tree.write(format=1)}' >> test1.in", shell=True)
spr_dist = subprocess.check_output("/usr/bin/Rscript ./test.R < test1.in", shell=True)
spr_dist = int(spr_dist.strip().decode('UTF-8').split(' ')[1])
print(spr_dist)

# DendoTreeIn = dendropy.Tree.get(data=input_tree.write(format=1), schema = 'newick')
# DendoTreeTarget = dendropy.Tree.get(data=target_tree.write(format=1), schema = 'newick')
# print(DendoTreeIn, DendoTreeTarget)

# print(DendoTreeIn.print_plot())
# print(DendoTreeTarget.print_plot())

# print(input_tree)
# print(target_tree)


# spr_dist = MAF.get_spr_dist(DendoTreeIn, DendoTreeTarget)
# print(spr_dist)

# input_tree_copy = input_tree.copy()
# target_tree_copy = target_tree.copy()

# input_tree_copy.prune(species_target, preserve_branch_length=False)
# target_tree_copy.prune(species_input, preserve_branch_length=False)
# print(input_tree_copy, target_tree_copy)

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

tree_features = fe.extract_features(input_tree, target_tree, [prune_edge, rgft_edge], calculation_flag='features', split_hash_dict={})
print(tree_features)

# print(likelihood)
