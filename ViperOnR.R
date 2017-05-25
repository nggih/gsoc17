list.files()
library(viper)
data(c, package = "")
browseVignettes("aracne.networks")
#BIG GOAL: FIND THE REGULATORS.
#There is no package called 'aracne.networks'
#Download the package:
source("https://bioconductor.org/biocLite.R")
biocLite("aracne.networks")

#Check paper aracne.network Giorgi, 2017

adjfile <- system.file("aracne", "filtered_10.adj") # does not work.
adjfile # empty
browseVignettes("aracne.networks") # downloaded to check whether it contributes to the samples.

library(aracne.networks)
data(package="aracne.networks")$results[, "Item"]

data(filtered_10, package = "regulonbrca") # there is no package called ‘regulonbrca’
data("regulonbrca") # good
write.regulon(regulonbrca, n=10)
adjfile <- system.file("aracne", "filtered_10.adj", package="bcellViper")
adjfile <- 'filtered_10.adj'

# Can we skip i to regul with aracne2regulon instead?
regul <- aracne2regulon('filtered_10.adj', 'Taylor_TF.txt', verbose = FALSE)

"Error in `rownames<-`(`*tmp*`, value = c(\"RNF14\", \"CCNE1\", \"RNF10\", \"ZDHHC14\",  : 
  length of 'dimnames' [1] not equal to array extent"

# Perhaps the filtered_10.adj can't just be from renaming the files of filtered_10.txt
# Trying to convert from txt to adj using GeWorkbench.
# the other problem that will appear is to save the network.txt to network.adj.

# GeWorkBench can't save it to adj directly.

# This is from the manual. I modify the adj to filtered_10
data(bcellViper, package = "bcellViper")
adjfiletest <- system.file("aracne", "bcellaracne.adj", package = 'bcellViper')
adjfile <- system.file("aracne", "filtered_10.adj", package = 'bcellViper')
adjfiletest
adjfile

regul <- aracne2regulon(adjfiletest, dset, verbose = FALSE)

head(dset)
dset
print(regul)
