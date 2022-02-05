#ifndef
#define
/*
    Author: Ty Klabcka
    Date: December 5, 2021

    Functionality: Given a positive number n > 1 this program finds the prime factor 
    decomposition of n. The result will be a string with the following form :  
    "(p1**n1)(p2**n2)...(pk**nk)"with the p(i) in increasing order and n(i) empty 
    if n(i) is 1.
*/
#include <iostream>
#include <map>
#include <cmath>

using namespace std;

class PrimeDecomp
{
public:
    static std::string factors(int lst, map<int, int>);
};

bool is_prime(int num){
    /* Return true if num is prime, otherwise return false*/
    if (num < 2)return false;
    else if (num == 2)return true;
    if (num % 2 == 0)return false;

    int root = sqrt(num);

    for (int itr=3; itr < root+1; itr++){
        if (num%itr == 0)return false;
    }
    return true;
}

void modifyMap(int lst, map<int, int> &myMap); 

string PrimeDecomp::factors(int lst, map<int, int> myMap){
    /* uses modified map to create a string to display the results neatly */
    modifyMap(lst, myMap);
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

void modifyMap(int lst, map<int, int> &myMap){
  /*If prime and not in map, add to map. Else, recurse until 
    all multiples up to that number have been evaluated. */
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
          modifyMap(multiple, myMap);
          modifyMap(lst/multiple, myMap);
          break;
        }
        else{
          multiple--;
        }
      }
    } 
}

#endif