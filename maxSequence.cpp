/*The maximum sum subarray problem consists in finding the 
maximum sum of a contiguous subsequence in an array or list of integers:
maxSequence({-2, 1, -3, 4, -1, 2, 1, -5, 4});
should be 6: {4, -1, 2, 1}
*/

#include <vector>
#include <iostream>

int maxSequence(const std::vector<int>& arr){
  
	vector<int> my_vec;
	for (unsigned pass = 0; pass < arr.size(); pass++){
		int max = 0;
		int actual = arr[pass];
		for (unsigned next_itm = pass + 1; next_itm <= arr.size(); next_itm++){
			if (actual > max){
				max = actual;
			}
			actual += arr[next_itm];
		}
		my_vec.push_back(max);
	}
	int var = *max_element(my_vec.begin(), my_vec.end());
	return var;
}

