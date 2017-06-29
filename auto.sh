#!/bin/bash
echo "---Starting Script---"
echo "---Generating Vars---"
ARRAY=(BRCA_90)
for TCGA in "${ARRAY[@]}"
do
	INITIAL=$TCGA
	FILE="90/$INITIAL.txt"
	echo "---Making Directory of $INITIAL---"
	mkdir $INITIAL
	echo "---ARACNE-AP for $INITIAL---"
	java -Xmx5G -jar Aracne.jar -e $FILE -o $INITIAL --tfs Taylor_TF.txt --pvalue 1E-8 --seed 1 --calculateThreshold
	echo "---Threshold Calculated---"
	echo "---Run 100 Reps Bootstraps---"
	for i in {0..100}	
	do
		java -Xmx5G -jar Aracne.jar -e $FILE -o $INITIAL --tfs Taylor_TF.txt --pvalue 1E-8 --seed $i
	done
	echo "---All Iterations Done!---"
	echo "---Consolidating---"
	java -Xmx5G -jar Aracne.jar -o $INITIAL --consolidate
	echo "---Done!, check on the network.txt in $INITIAL---"
done


