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


print(TreeDist::SPRDist(tree1, tree2))

