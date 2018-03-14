#include <iostream>
#include "./BigInt/BigInteger.hpp"

/*
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
*/

using namespace std;

BigInteger factorial(int value) {
    BigInteger result(1);
    for (int next = 1; next <= value; next++) {
        result *= next;
    }
    return result;
}

long factorialDigitSum(BigInteger factorial){
	long sum = 0;
	for(int i = 0; i < factorial.getLength(); ++i){
		sum += factorial.getDigit(i);
	}
	return sum;

}

int main(){
	while(true){
		int input;
		cout << "Enter a number: ";
		cin >> input;
		if(input <=0) break;
		printf("Factorial of %d is: ", input);
		cout << factorial(input) << endl;
		cout << "The sum of the digits in " << factorial(input) << " is: " << factorialDigitSum(factorial(input)) << endl;
	}
	return 0;
}
