#include <iostream>
#include <sstream>
#include "BigInt/BigInteger.hpp"

using namespace std;

BigInteger pow(int base, int power){
	BigInteger ret(1);
	for(int i = power; i > 0; --i){
		ret *= base;
	}
	return ret;
}

BigInteger powerDigitSum(int base,int power){
	BigInteger total = pow(base,power);
	BigInteger sum;
	for(int i = 0; i < total.getLength(); ++i){
		sum += total.getDigit(i);
	}
	return sum;
}

int main(){
	while(true){
		int power;
		cout << "Input power (default base is 2): ";
		cin >> power;
		if(power <= 0) break;
		printf("The sum of the digits of 2^%d is ", power);
		cout << powerDigitSum(2,power);
		cout << endl << endl;
	}
	
	return 0;
}
