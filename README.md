# ThePhylogeneticGameSPRDistances
Fork of the Git repository for the paper : "The tree reconstruction game: phylogenetic
reconstruction using reinforcement learning" <br />
Link to paper: https://github.com/michaelalb/ThePhylogeneticGame

Git repository for the paper "A Reinforcement Learning Pipeline for Computing the SPR Distance Between Phylogenetic Trees"

This paper aims to investigate the effectiveness of the Reinforcement Learning approach when computing the SPR distance between two phylogenetic trees. Due to time and computation constraints, the results are not optimized but rather a proof-of-concept. The paper builds on the structure designed in the original paper, adjusting it to suit our need.


In order to install the necessary environment please make sure you have 
Anaconda. Create the environment with <br />

`conda env create -f environment.yml`

To run an experiment run the ProjectMain.py file. <br />
There are the relevant parameters: <br />
-- experiment_unique_dir_name - which will create a unique directory for you experiment results.<br/>
-- cpus - which allows you to run the training process on multiple cpus for increased runtime.

All parameters for experiment configuration are in SharedConsts.py with appropriate documentation.

## Additional dependencies:
-- uSPR by Chris Whidden (https://github.com/cwhidden/uspr)
-- Rscript, and the TreeDist, Quartet, ape, and Phangorn packages

Additionally, datasets were used from https://github.com/skelk2001/kernelizing-agreement-forests/
