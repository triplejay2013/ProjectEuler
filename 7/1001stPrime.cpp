//By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//What is the 10 001st prime number?

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool isPrime(const long& num) {
    for(int i = 2; i <= pow(num,0.5); ++i) {
        if(num%i == 0) return false;
    }
    return true;
}

vector<long> generatePrimes(int range) {
    vector<long> ret;
    long nums = 2;//cuz two is first prime
    while(range > 0) {
        if(isPrime(nums)) {
            ret.push_back(nums);
            --range;
        }
        ++nums;
    }
    return ret;
}

void print(const vector<long>& vec) {
    for(long i : vec) {
        cout << i << endl;
    }
}

int main() {
    vector<long> primes = generatePrimes(10001);
    print(primes);

    return 0;
}

