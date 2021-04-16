#%%
import os
import re
import glob

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser




def DebugHtml(test):
    os.chdir("/home/david/Documents/blast/Blastfiles/outputfiles/Genelists")

    file = open("scripts/htmltest/brower.html", "w")
    file.write(test)
    file.close()




def GeneOntology(name):
    print("Starting GeneOntology for " + name )
    br = RoboBrowser(parser="html.parser")
    br.open("http://geneontology.org/")

    form = br.get_forms()[1]

    geneinput = form["input"]
    species = form["species"]

    form["species"].value = "IXOSC"





    os.chdir("/home/david/Documents/blast/Blastfiles/outputfiles/Genelists")
    os.listdir(".")
    file = open(name, "r")

    string = ""

    for line in file.readlines():
        #print(line)
        string = string + line 


    form["input"] = string
    #print(form)
    br.submit_form(form)

    #print(br.find_all())
    #DebugHtml(str(br.parsed))

    table_link = br.find("a", href=re.compile("/tools/compareToRefListTxt.jsp"))
    br.follow_link(table_link)
    csv_content = br.response.content.decode("utf-8")

    savefile = open("GOoutput/"+name, "w")
    savefile.write(csv_content)
    savefile.close()
    print("finished")

def main():

    os.chdir("/home/david/Documents/blast/Blastfiles/outputfiles/Genelists/profileddata")
    for i in glob.glob('*.csv'):
        if i not in ["body.csv", "leg.csv", "table.csv"]:
            GeneOntology(i)


main()
    
