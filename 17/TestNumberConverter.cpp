#include <iostream>
#include "NumberConverter.hpp"

//TODO make into test class
using namespace std;

int main(){
	NumberConverter nums;
	int lower, upper;
	cout << "Starting Test Suite: (0 to quit)\n";
	while(true){
		cout << "Input Lower Bound (inclusive): ";
		cin >> lower;
		if(lower <= 0) break;
		cout << "Input Upper Bound (inclusive): ";
		cin >> upper;
		if(upper <= 0 || upper <= lower) break;
		printf("The total number of letters in the range from %d to %d is %lu\n", lower, upper, nums.countRange(lower, upper));
		for(int i = lower; i <= upper; ++i){
			cout << nums.display(i) << endl;
		}
	}

	return 0;
}
