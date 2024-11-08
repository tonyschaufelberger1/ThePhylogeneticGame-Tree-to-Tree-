for (x in list.dirs()) {
	filename <- paste(x, "/masked_species_real_msa.phy_phyml_tree_bionj.txt.rooted", sep="")
	print("working...")
	if (file.exists(filename)) {
		tree <- ape::read.tree(filename)
		tryCatch(expr = {
			if (ape::is.binary(tree) == FALSE) {
				print("FALSE!")
				q()
			}
			
	}, error= function(e) {print(paste("problem with the file:", filename))})
}}
