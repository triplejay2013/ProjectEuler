/*
	generates a list of primes in an output file
*/

#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

bool isPrime(const long& num) {
	if(num%2 == 0) return false;
    for(int i = 3; (i*i) <= num+1; i+=2) {
        if(num%i == 0) return false;
    }
    return true;
}

int main(){
	int num;
	ofstream myFile("primes.txt");
	cin >> num;
	for(int i = 2; i < num; ++i){
		if(isPrime(i)) myFile << i << endl;
	}
	myFile.close();

	return 0;
}
