//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?

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

vector<long> primeFactors(long n) {
    vector<long> ret;
    for(int i = 2; i < pow(n,0.5); ++i) {
        if(n%i == 0) {
            if(isPrime(i)) ret.push_back(i);
        }
    }
    return ret;
}

void print(const vector<long>& vec, long num) {
    for(long i : vec) {
        printf("%ld is a prime factor of %ld\n", i, num);
    }
}

int main() {
//    int num = 13195;
    long num = 600851475143;
    vector<long> factors = primeFactors(num);
    print(factors, num);
    printf("The largest prime factor of %ld is %ld", num, factors[factors.size()-1]);
    return 0;
}

