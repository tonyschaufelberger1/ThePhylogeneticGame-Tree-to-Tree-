suppressPackageStartupMessages(library("Quartet"))
f <- file("stdin")

open(f)

i <- 0

while(length(line <- readLines(f,n=1)) > 0) {
  if (i == 0)
    tree1 <- ape::read.tree(text=line)
  else
    tree2 <- ape::read.tree(text=line)
  i <- i + 1
  # process line
}

# mast <- phangorn::mast(tree1, tree2, tree=TRUE, rooted=FALSE)
statuses <- QuartetStatus(tree1, tree2)
print(QuartetDivergence(statuses, similarity=FALSE))
# print(ape::write.tree(mast))

print(TreeDist::SPRDist(tree1, tree2))

