/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the long longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

#include <iostream>
#include <vector>

using namespace std;

vector<long long> findChain(const long long& originalNum){
	long long n = originalNum;
	vector<long long> ret;
	ret.push_back(originalNum);
	while(n != 1){ //if the number is even
		if(n%2 == 0){
			n /= 2;
		} 
		//else the number is odd
		else{
			n = (3*n) + 1;
		}
		ret.push_back(n);
	}

	return ret;
}

void printChain(vector<long long> vec){
	for(long long i = 0; i < vec.size(); ++i){
		if(i == vec.size() - 1){
			printf("%llu\n", vec[i]);
			break;
		}
		printf("%llu -> ", vec[i]);
	}
}

long long findAll(const long long& num){
	long long maxSize = 0;
	long long chainVal = 0;
	vector<long long> chain;
	vector<long long> max;
	for(long long i = 1; i < num; ++i){
		chain = findChain(i);
		//printChain(chain);
		if(chain.size() > maxSize){
			maxSize = chain.size();
			chainVal = i;
			max = chain;
		}
	}
	printChain(max);
	return chainVal;
}

int main(){
	char input;
	long long num = 13;
	while(true){
		cout << "Input number for Collatz Chain: ";
		cin >> num;
		cout << endl;
		cout << "Finding longest chain less than " << num << "\n";
		printf("Found largest chain at %llu\n", findAll(num));
		cout << "Press q to quit\n";
		cin >> input;
		if(input == 'q' || input == 'Q') break;
	}
	return 0;
}
