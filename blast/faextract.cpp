#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

char** processargs (int argc, char** args){
    bool blast = false;

    if (argc < 3){
        std::cout << "Not enough args, please enter [reference, input, output] or \n [input, output]" << std::endl;
        exit(1);
    }
    if (argc > 4){
        std::cout << "Too many args, please enter [input, reference,  output] or \n [input, output]" << std::endl;
        exit(1);
    }
    
    return(args);
}

void newfasta (std::string genelist, std::string oldfasta, std::string outputfile){
    std::ifstream genes;
    std::ifstream ofa;
    std::ofstream out;
    std::string geneline;
    std::vector <std::string> compare;

    genes.open(genelist);
    ofa.open(oldfasta);
    out.open(outputfile);

    while(getline(genes, geneline)){
        compare.push_back(">" + geneline);
    }

    std::string line;
    bool linecheck = false;

    while(getline (ofa, line)){
        if (line[0] == '>'){
            if (any_of(compare.begin(), compare.end(),[line](std::string str){return(line==str);} )){
                out << line << std::endl;
                linecheck=true;
            }else{
                linecheck=false;
            }
        } else if (linecheck == true){
            out << line << std::endl;
        }
    }
    out.close();
}

void blastgenes (std::string blastdata, std::string outputfile){
    std::ifstream blast;
    std::ofstream out;
    out.open(outputfile);
    blast.open(blastdata);
    std::string line;
    while(getline (blast,line)){
        if (line[0] == '>'){
            out << line.substr(1, 10) << std::endl;
        }
    }
    out.close();
}

int main(int argc, char** args){
    char** procargs = processargs(argc, args);

    if (argc  == 4){
        newfasta(args[1], args[2], args[3]);
    }
    if (argc == 3){
        blastgenes(args[1], args[2]);
    }
}


