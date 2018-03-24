#include <iostream>
#include "BigInteger.hpp"

using namespace std;

BigInteger fib(int n){
	BigInteger numeratorFirst =BigInteger::pow(1+BigInteger::sqrt(5), n);
	//cout << numeratorFirst << endl;
	BigInteger numeratorSecond=(BigInteger::pow(1-BigInteger::sqrt(5), n));
	//cout << numeratorSecond << endl;
	BigInteger denominator=(BigInteger::pow(BigInteger(2),n)*BigInteger::sqrt(5));
	//cout << denominator << endl;
	BigInteger ret = (numeratorFirst - numeratorSecond)/denominator;
	return ret;
}

int main(){
	cout << fib(1000) << endl;
	return 0;
}
