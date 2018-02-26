//http://www.mathblog.dk/project-euler-17-letters-in-the-numbers-1-1000/
//see that website for an explanation or comparison
#include <iostream>
#include "NumberConverter.hpp"

int main(){
	NumberConverter nums;
	int choice;
	int input;
	int input1;
	while(true){
		printf("\n1 for single; 2 for range; 0 to quit: ");
		cin >> choice;
		if(choice <= 0) break;
		cout << endl;
		if(choice == 1){
			while(true){
				cout << "Input number: ";
				cin >> input;
				if(input <= 0) break;
				cout << "The number " << input << " written out is: " << nums.display(input) << endl;
				cout << "The number " << input << " has " << nums.count(input) << " letter(s)\n";
			}
		}
		if(choice == 2){
			while(true){
				cout << "Input Lower Bound (inclusive): ";
				cin >> input;
				if(input <= 0) break;
				cout << "Input Upper Bound (inclusive): ";
				cin >> input1;
				if(input1 <= 0) break;
				printf("The total number of letters in the range from %d to %d is %lu\n", input, input1, nums.countRange(input, input1));
			}
		}
	}

	return 0;
}
