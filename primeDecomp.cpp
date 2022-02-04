#include <iostream>
#include <map>
#include <cmath>

using namespace std;

class PrimeDecomp
{
public:
    static std::string factors(int lst);
};

bool is_prime(int num){
    if (num < 2)return false;
    else if (num == 2)return true;
    if (num % 2 == 0)return false;

    int root = sqrt(num);

    for (int itr=3; itr < root+1; itr += 1){
        if (num%itr == 0)return false;
    }
    return true;
}

map<int,int> myMap;

void modifyMap(int lst);

string PrimeDecomp::factors(int lst){
    modifyMap(lst);
    map<int,int>::iterator it;
    string strang;
    for (it = myMap.begin(); it != myMap.end(); it++){
      if (it->second > 1){
        strang += '(' + to_string(it->first) + '*' + '*' + to_string(it->second) + ')';
      }
      else{
        strang += '(' + to_string(it->first) + ')';
      }
      
    }
    myMap.clear();
    return strang;
}

void modifyMap(int lst){
  if (is_prime(lst)){
      if (myMap.find(lst) == myMap.end()){
        myMap.insert(pair<int,int>(lst, 1));
      }
      else{
        myMap[lst] += 1;
      }
    }
    else{
      int multiple = sqrt(lst) + 1;
      while (multiple > 0){
        if (lst%multiple==0){
          modifyMap(multiple);
          modifyMap(lst/multiple);
          break;
        }
        else{
          multiple--;
        }
      }
    } 
}

int main(){
    
}