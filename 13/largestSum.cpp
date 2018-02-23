/*
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

*see 'largestSum.txt'
*/

#include <iostream>
#include <fstream>
#include <vector>
#include "./BigInt/BigInteger.hpp"

using namespace std;

BigInteger load(){
	ifstream file("./largestSum.txt");
	string tmpStr;
	BigInteger temp;
	BigInteger sum(0);
	while(getline(file, tmpStr)){
		temp = tmpStr;
		sum += temp;
	}
	file.close();
	return sum;
}

int main(){
	cout << "The sum of the list of 50 digit numbers is " << load() << endl;

	return 0;
}

