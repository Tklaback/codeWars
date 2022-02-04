#include <vector>
#include <iostream>
#include <array>
#include <map>
#include <sstream>
#include <typeinfo>
using namespace std;

class StockList
{
public:
  static std::string stockSummary(std::vector<std::string> &lstOfArt, std::vector<std::string> &categories);
};

string StockList::stockSummary(std::vector<std::string> &lstOfArt, std::vector<std::string> &categories){
    if (lstOfArt.empty() || categories.empty())return "";
    map<char, int> myMap;
    for (string letter : categories){
        const char * s = letter.c_str();
        myMap[*s] = 0;
    }
    for (unsigned itm=0;itm < lstOfArt.size(); itm++){
        int num = lstOfArt[itm].find(' ');
        istringstream converter(lstOfArt[itm].substr(num+1, lstOfArt[itm].size()-1));
        int number;
        converter >> number;
        myMap[lstOfArt[itm][0]] += number;
    }
    string strang;
    for (unsigned it = 0;it < categories.size(); it++){
        const char * s = categories[it].c_str();
        if (myMap.find(*s) != myMap.end()){
            ostringstream converter;
            converter << myMap[*s];
            strang.push_back('(');
            strang.push_back(*s);
            strang += " : ";
            strang += converter.str();
            strang.push_back(')');
            strang += " - ";
        }
        
    }
    strang.erase(strang.size()-3, 3);
    return strang;
}

int main(){
    
    array<string, 5> codes = {"BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"};
    vector<string> vect;
    std::vector<std::string> cd;
    cd.push_back("A");
    cd.push_back("B");
    cd.push_back("C");
    cd.push_back("D");
    for (int num=0; num < codes.size(); num++){
        vect.push_back(codes[num]);
    }
    cout << StockList::stockSummary(vect, cd) << endl;
}   
