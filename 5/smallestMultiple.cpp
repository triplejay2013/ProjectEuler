//2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
//What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#include <iostream>

using namespace std;

bool canDivide(int num, int range) {
    for(int i = 1; i <= range; ++i) {
        if(num%i != 0) return false;
    }
    return true;
}

int findCommonMultiple(int range) {
    int counter = 1;
    while(true) {
        if(canDivide(counter, range)) return counter;
        ++counter;
    }
}

int main() {
    int smallestMultiple = findCommonMultiple(20);
    cout << smallestMultiple << endl;

    return 0;
}
