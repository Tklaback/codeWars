#git test foo

#include <iostream>

using namespace std;

#include <iostream>
#include <sstream>
#include <vector>
#include <tuple>
#include <map>

using namespace std;

class Stat
{
public:
  static std::string stat(const std::string &strg);
};

string create_map(map<string, int> *myMap, const string &strg){
    string delimiter = ", ";
    int position;
    string str1 = strg;
    while (str1.find(delimiter) != string::npos){
        position = str1.find(delimiter);
        string substring = str1.substr(0, position);
        
        string numberString;
        int x = 0;
        int bigNum = 0;
        for (unsigned num = 0; num < substring.size()+1;num++){
            int add_to_total = 0;
            if (num == substring.size()){
                // cout << numberString << endl;
                istringstream converter(numberString);
                converter >> add_to_total;
                bigNum += add_to_total;
                continue;
            }

            if (isalnum(substring[num])){
                numberString += substring[num];
            }
            
            else{
                if (x == 0){
                    // cout << numberString << " - hour" << endl;
                    istringstream converter(numberString);
                    converter >> add_to_total;
                    bigNum += (add_to_total*3600);
                    x += 1;
                }
                else if (x == 1){
                    // cout << numberString << " - minute" << endl;
                    istringstream converter(numberString);
                    converter >> add_to_total;
                    bigNum += (add_to_total*60);
                }
                numberString = "";
            }
        }
        (*myMap)[substring] = bigNum;
        // cout << bigNum << endl;
        str1.erase(0, position + 2);
    }
    string substring = str1.substr(0, position);
        string numberString;
        int x = 0;
        int bigNum = 0;
        for (unsigned num = 0; num < substring.size()+1;num++){
            int add_to_total = 0;
            if (num == substring.size()){
                istringstream converter(numberString);
                converter >> add_to_total;
                bigNum += add_to_total;
                continue;
            }

            if (isalnum(substring[num])){
                numberString += substring[num];
            }
            
            else{
                if (x == 0){
                    // cout << numberString << " - hour" << endl;
                    istringstream converter(numberString);
                    converter >> add_to_total;
                    bigNum += (add_to_total*3600);
                    x += 1;
                }
                else if (x == 1){
                    // cout << numberString << " - minute" << endl;
                    istringstream converter(numberString);
                    converter >> add_to_total;
                    bigNum += (add_to_total*60);
                }
                numberString = "";
            }
        }
        (*myMap)[substring] = bigNum;
        // cout << bigNum << endl;
    return "";
}

string Stat::stat(const string &strg){
    map<string, int> myMap;
    create_map(&myMap, strg);
    map<string, int>::iterator it;
    int total = 0;
    for (it = myMap.begin(); it != myMap.end(); it++){
        total += it->second;
        // cout << it->first << ": " << it->second << endl;
    }
    int range = myMap.rbegin()->second - myMap.begin()->second;
    int avg = ((float)total / myMap.size());
    const int hours = 3600, min = 60;
    // map<string, int>::iterator it;
    int middle;
    for (it = myMap.begin(), middle = 0; middle < myMap.size()/2; middle++, it++){
    }
    
    string str_r = ((to_string(range/hours).size()<2)? "0" + to_string(range/hours):to_string(range/hours)) + "|" + 
    ((to_string((range%hours)/min).size()<2)? "0" + to_string((range%hours)/min):to_string((range%hours)/min)) + "|" + 
    ((to_string((range%hours)%min).size()<2)? "0" + to_string((range%hours)%min):to_string((range%hours)%min));
    string str_a = ((to_string(avg/hours).size()<2)? "0" + to_string(avg/hours):to_string(avg/hours)) + "|" + 
    ((to_string((avg%hours)/min).size()<2)? "0" + to_string((avg%hours)/min):to_string((avg%hours)/min)) + "|" + 
    ((to_string((avg%hours)%min).size()<2)? "0" + to_string((avg%hours)%min):to_string((avg%hours)%min));
    string str_m = it->first;
    string first = str_m.substr(0, str_m.find('|'));
    str_m.erase(0,str_m.find('|')+ 1);
    string second = str_m.substr(0, str_m.find('|'));
    str_m.erase(0,str_m.find('|')+ 1);
    string new_m = ((first.size()<2)? "0" + first:first) + "|" + 
    ((second.size()<2)? "0" + second:second) + "|" + 
    ((str_m.size()<2)? "0" + str_m:str_m);
    
    
    return "Range: " + str_r + " Average: " + str_a + " Median: " + new_m;
}


int main(){
    cout << Stat::stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41") << endl;
}
