#!bin/bash

if [ $# -eq 0 ]; then
	echo Enter the name of the blast database
	read blastdb
	
	echo Enter the directory where the gene lists are located
	read genelists

	echo Enter the output directory
	read output
else
	echo using command line arguments
	blastdb=$1
	genelists=$2
	output=$3
fi


for file in $genelists/*
do
	filename=$(basename $file)
	echo $output$filename
	sh blast.sh $file $blastdb $filename
	
done



