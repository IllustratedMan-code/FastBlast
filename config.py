import pathlib
import json
import subprocess

config = {}
config["paths"] = []
config["settings"] = []

FastBlastDirectory = str(pathlib.Path(__file__).parent.absolute())
config["paths"].append({"Name": "FastBlast", "Path": FastBlastDirectory})

dbtype = input("What is the dbtype for your database:")

if dbtype == "prot":
    blastLocation = subprocess.check_output(["which", "blastp"]).decode("utf-8")
elif dbtype == "nucl":
    blastLocation = subprocess.check_output(["which", "blastn"]).decode("utf-8")
else:
    print("Unknown database type, please refer to the blast+ manual")
    print("defaulting to prot")
    blastLocation = subprocess.check_output(["which", "blastp"]).decode("utf-8")
config["paths"].append({"Name": "blast", "Path": blastLocation})

blastdb = input("What is the path to the blastdb:")
config["paths"].append({"Name": "blastdb", "Path": blastdb})

outputdir = input("Enter the path to the output directory:")
config["paths"].append({"Name": "output", "Path": outputdir})

threads = input("Enter the number of threads you would like to use:")
config["settings"].append({"Name": "ThreadCount", "Value": threads})

genedir = input("Enter the directory where the genes are located:")
config["paths"].append({"Name": "GeneDir", "Path": genedir})

assembly = input("Enter The path to the gene assembly(test species):")
config["paths"].append({"Name": "Assembly", "Path": genedir})


with open("config.json", "w") as outfile:
    json.dump(config, outfile)
