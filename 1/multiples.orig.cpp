#include <iostream>

using namespace std;

//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these multiples is 23.
//Find the sum of all the multiples of 3 or 5 below 1000.
//https://projecteuler.net/problem=1

//checks to see if number is a multiple of 3 or 5
bool multiple(int num) {
    if(num == 0) return false;
    if(num%3==0 || num%5==0) return true;
    return false;
}

int main() {
    int sum = 0;
    for(int i = 1; i < 1000; ++i) {
        if(multiple(i)) {
            sum+=i;
        }
    }
    cout << sum << endl;
    return 0;
}
