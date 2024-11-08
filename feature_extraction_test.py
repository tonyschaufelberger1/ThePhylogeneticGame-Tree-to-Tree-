from FeatureExtractor.FeatureExtractor import FeatureExtractorClass
from Reinforcement_env.env_utils import PhyloGameUtils
from SPR_generator.SPR_move import Edge
import ete3
# from tqdist import *
# from Espalier import MAF
# import dendropy
import subprocess
import SharedConsts as SC

fe = FeatureExtractorClass()

helper = PhyloGameUtils(feature_extractor_instance=fe, datasets=None, use_random_starts=True, results_dir="./experiments_results/feature_extraction_test")

# likelihood = fe.extract_likelihood(input_tree, helper.data_set)['resulting_ll'][0]

species_input = 0

species_target = set()

input_tree, target_tree = helper.get_starting_tree()

print(input_tree)
print(target_tree)


subprocess.call("touch test1.in", shell=True)
subprocess.call(f"echo '{input_tree.write(format=1)}' > test1.in", shell=True)
subprocess.call(f"echo '{target_tree.write(format=1)}' >> test1.in", shell=True)
spr_dist = subprocess.check_output(f"/usr/bin/Rscript ./R_programs/spr_dist.R <<< $'{input_tree.write(format=1)}\n{target_tree.write(format=1)}'", shell=True, executable='/bin/bash')
spr_dist = int(spr_dist.strip().decode('UTF-8').split(' ')[1])
quartet_dist = subprocess.check_output("/usr/bin/Rscript ./R_programs/quartet_dist.R < test1.in", shell=True)
quartet_dist = float(quartet_dist.strip().decode('UTF-8').split(' ')[1])
mast = subprocess.check_output("/usr/bin/Rscript ./R_programs/mast.R < test1.in", shell=True)
mast = mast.strip().decode('UTF-8').split(' ')[1]
mast = mast[1:len(mast)-1]
print("(" + mast[0:len(mast)-1] + ");")
mast = ete3.Tree(mast, format=1)
print(mast)


results = subprocess.check_output(f"/usr/bin/Rscript ./R_programs/all.R <<< $'{input_tree.write(format=1)}\n{target_tree.write(format=1)}'", shell=True, executable='/bin/bash')
results = results.strip().decode('UTF-8').split(' ')
quartet_dist = float(results[1].split('\n')[0])
print(quartet_dist)
spr_dist = int(results[2])
print(spr_dist)

subprocess.call("touch test1.in", shell=True)
subprocess.call(f"echo '{input_tree.write(format=4)}' > test1.in", shell=True)
subprocess.call(f"echo '{target_tree.write(format=4)}' >> test1.in", shell=True)

subprocess.call("touch uspr_dists.out", shell=True)
subprocess.call(SC.USPR_SCRIPT + " --uspr < test1.in > uspr_dists.out", shell=True)
uspr_dist = subprocess.check_output("cat uspr_dists.out", shell=True)
uspr_dist = uspr_dist.decode('UTF-8').split('\n')[3].split(' ')[2]
print("Optimal SPR distance as calculated by uSPR", uspr_dist)


print("SPR distance upper bound between input and target", spr_dist)
print("Quartet distance between input and target", quartet_dist)

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
