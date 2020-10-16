#! /bin/bash

if [ $# -eq 0 ]; then
	echo Enter file Name for list of genes:

	read genelist

	echo Enter name of output file:

	read output
else
	echo using command line arguments
	genelist=$1
	output=$2
fi
echo
echo extracting gene information from fasta

fae $genelist ~/Documents/blast/db/full.fasta temp.fasta

echo running blastx
blastx -query  temp.fasta -db ~/Documents/blast/Iclc.fasta -out tempblast.out -num_threads 10

echo reformatting output
fae tempblast.out $output

echo done
