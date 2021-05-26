# which python line goes here
#
import json
import sys
import pathlib
import os
import subprocess

os.chdir(pathlib.Path(__file__).parent.absolute())
configFile = open(
    str(pathlib.Path(__file__).resolve().parent.absolute()) + "/config.json"
)
config = json.load(configFile)
configFile.close()


def searchJsonForName(Name, jsonObject):
    for item in jsonObject:
        if item["Name"] == Name:
            return item
    raise NameError


GeneDir = searchJsonForName("GeneDir", config["paths"])["Path"]
FastBlastDirectory = searchJsonForName("FastBlast", config["paths"])["Path"]
threads = searchJsonForName("ThreadCount", config["settings"])["Value"]
blastdb = searchJsonForName("blastdb", config["paths"])["Path"]
outputdir = searchJsonForName("output", config["paths"])["Path"]
Assembly = searchJsonForName("Assembly", config["paths"])["Path"]


os.chdir(pathlib.Path(blastdb).parent)


def blast(Blastdb, Genelist, Output, Assembly, threads):
    print("Analysing " + Genelist)
    subprocess.check_call(
        [FastBlastDirectory + "/fae", Genelist, Assembly, "temp.fasta"]
    )
    subprocess.check_call(
        [
            "blastx",
            "-query",
            "temp.fasta",
            "-db",
            Blastdb,
            "-out",
            "tempblast.out",
            "-num_threads",
            threads,
        ]
    )
    subprocess.check_call([FastBlastDirectory + "/fae", "tempblast.out", Output])
    subprocess.check_call(["mv", "temp.fasta", os.path.splitext(Output)[0] + ".fasta"])
    subprocess.check_call(
        ["mv", "tempblast.out", os.path.splitext(Output)[0] + ".blastout"]
    )


def blastloop(Blastdb, geneDir, OutputDir, Assembly, threads):
    if not os.path.isdir(OutputDir):
        subprocess.check_call(["mkdir", OutputDir])
    for file in os.listdir(geneDir):
        basename, extension = os.path.splitext(file)
        if extension == ".csv":
            blast(
                Blastdb,
                geneDir + "/" + file,
                OutputDir + "/" + basename + ".csv",
                Assembly,
                threads,
            )


blastloop(blastdb, GeneDir, outputdir, Assembly, threads)
