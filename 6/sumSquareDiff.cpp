//The sum of the squares of the first ten natural numbers is,
//1^2 + 2^2 + ... + 10^2 = 385
//The square of the sum of the first ten natural numbers is,
//(1 + 2 + ... + 10)^2 = 55^2 = 3025
//Hence the difference between the sum of the squares of the
// first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
//Find the difference between the sum of the squares of the first one hundred
// natural numbers and the square of the sum.

#include <iostream>
#include <cmath>

using namespace std;

long sumOfSquares(int range) {
    long sum = 0;
    for(int i = 1; i <= range; ++i) {
        sum += pow(i,2);
    }
    return sum;
}

long squareSum(int range) {
    long sum = 0;
    for(int i = 1; i <=range; ++i) {
        sum += i;
    }
    return static_cast<long>(pow(sum, 2));
}

int main() {
    long sumOf = sumOfSquares(100);
    long sum = squareSum(100);
//    cout << sumOf << endl;
//    cout << sum << endl;
    cout << sum - sumOf << endl;

    return 0;
}

