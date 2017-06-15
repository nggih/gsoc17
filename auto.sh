#!/bin/bash
echo "---Starting Script---"
echo "---Generating Vars---"
ARRAY=(UCS_f10 ACC_f10 UVM_f10 MESO_f10 KICH_f10)
for TCGA in "${ARRAY[@]}"
do
	INITIAL=$TCGA
	FILE="filtered10/$INITIAL.txt"
	echo "---Making Directory of $INITIAL---"
	mkdir $INITIAL
	echo "---ARACNE-AP for $INITIAL---"
	java -Xmx12G -jar Aracne.jar -e $FILE -o $INITIAL --tfs Taylor_TF.txt --pvalue 1E-8 --seed 1 --calculateThreshold
	echo "---Threshold Calculated---"
	echo "---Run 100 Reps Bootstraps---"
	for i in {1..3}	
	do
		java -Xmx12G -jar Aracne.jar -e $FILE -o $INITIAL --tfs Taylor_TF.txt --pvalue 1E-8 --seed $i
	done
	echo "---All Iterations Done!---"
	echo "---Consolidating---"
	java -Xmx12G -jar Aracne.jar -o $INITIAL --consolidate
	echo "---Done!, check on the network.txt in $INITIAL---"
done


