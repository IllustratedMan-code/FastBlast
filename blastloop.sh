#!bin/bash


STR="outputfiles/"
for f in Genelists/*
do
	echo $STR$f
	sh blast.sh $f $STR$f
	
done



