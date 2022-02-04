#include <string>
#include <vector>
#include <iostream>

using namespace std;

// template <typename T> std::vector<T> uniqueInOrder(const std::vector<T>& iterable){
//     vector<T> myVec;
//     for (int itm = 0; itm < iterable.size(); itm++){
//       if (iterable[itm] == iterable[itm+1]){
//           continue;
//       }
//       else{
//           myVec.push_back(iterable[itm]);
//       }
//   }
//   return myVec;
// }
// // std::vector<char> uniqueInOrder(const std::string& iterable){
// //   vector<char> myVec;
// //   for (int itm = 0; itm < iterable.size(); itm++){
// //       if (iterable[itm] == iterable[itm+1]){
// //           continue;
// //       }
// //       else{
// //           myVec.push_back(iterable[itm]);
// //       }
// //   }
// //   return myVec;
// // }

// int main(){
//     // vector<char> myVec = uniqueInOrder("ABBCcAD");
//     // for (char num : myVec){
//     //     cout << num << endl;
//     // }
//     vector<int> vec;
//     vec.push_back(4);
//     vec.push_back(5);
//     vec.push_back(6);
//     vec.push_back(0);
    
//     for (char num : uniqueInOrder(vec)){
//         cout << num << endl;
//     }
// }
