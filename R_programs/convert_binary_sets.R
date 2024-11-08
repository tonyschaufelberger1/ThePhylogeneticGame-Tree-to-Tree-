for (x in list.dirs()) {
	treeType <- "masked_species_real_msa.phy.raxml.startTree"
	filename <- paste(x, "/", treeType, sep="")
	print("working...")
	if (file.exists(filename)) {
		tree <- ape::read.tree(filename)
		tryCatch(expr = {
			if (ape::is.binary(tree) == FALSE) {
				binaryTree <- TreeTools::MakeTreeBinary(tree)
				newFileName <- paste("./z__USER_CUSTOM_TREES/", substring(x,3), ".", treeType, sep="")
				file.create(newFileName)
				ape::write.tree(binaryTree, file=newFileName)
			}
			
	}, error= function(e) {print(paste("problem with the file:", filename))})
}}
warnings()
