#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <filesystem>
namespace fs = std::filesystem;


void fileio(std::string filestring){
    if (!(filestring.find("csv") < filestring.length())){return;}


    std::ifstream file;
    file.open("./GOoutput/" + filestring);
    std::string line;
    std::ofstream outfile;
    outfile.open("./GOoutput/GoTerms/" + filestring);
    bool check = false;
    bool check1 = false;
    int count = 0;
    while (getline(file, line)){
        //std::cout << line.length() << std::endl;
        //std::cout << line.length() <<std::endl;
        int length = line.length();
        for (int i = 0; i < length; i++ ){
            //std::cout << line;
            if (line[i] == ')'){check=false;outfile << std::endl;check1=false;}
            if ((check == true) && (line[i] == 'G'))check1=true;   
            if (check1==true){
                outfile << line[i];
            }
            
            if (line[i] == '(')check=true;
            
            
            
            
        }
    
    
        
    }
    outfile.close();
}

std::string directorylimiter(std::string directory){
    std::string finalstring = "";
    bool check = false;
    for (char c: directory){
        if (check == true){

            finalstring += c;
        }
        if (c == '/')check=true;
       
    }
    return(finalstring);
}

int main(){
    

    for (auto& f: fs::directory_iterator("GOoutput")){
        
        fileio(directorylimiter(f.path()));
        
    }
}