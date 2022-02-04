
#include <iostream>
#include <vector>

using namespace std;

class Tortoise
{
public:
    static std::vector<int> race(int v1, int v2, int g);
};

vector<int> Tortoise::race(int v1, int v2, int g){
    vector<int> myVec;
    // if (v1 >= v2)return {-1, -1, -1};
    double newV1 = (double)v1 / 3600;
    double newV2 = (double)v2 / 3600;
    cout << newV1 << " " << newV2 << endl;;
    int x = (int)((double)(g) / (double)(newV2 - newV1));
    cout << x << endl;
    int hours = x / 3600;
    cout << hours << endl;
    int minutes = (x %3600) / 60;
    int seconds = (x % 3600) % 60;
    myVec.push_back(hours);
    myVec.push_back(minutes);
    myVec.push_back(seconds);
    
    return myVec;
}

int main(){
    Tortoise *myTort = new Tortoise();
    vector<int> vec = myTort->race(720, 850, 70);
    for (int num : vec){
        cout << num << endl;
    }
}
    