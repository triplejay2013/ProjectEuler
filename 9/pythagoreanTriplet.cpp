//A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//
//a^2 + b^2 = c^2
//For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
//
//There exists exactly one Pythagorean triplet for which a + b + c = 1000.
//Find the product abc.
//answer : 31875000

#include <iostream>
#include <cmath>

using namespace std;

struct PythagoreanTriplet {
    int a = 0;
    int b = 0;
    int c = 0;
};

//check to make sure the components of the triplet are a valid pythagorean triplet
bool test(PythagoreanTriplet triplet){
	if(pow(triplet.a,2) + pow(triplet.b,2) == pow(triplet.c,2)) return true;
	return false;
}

//Creates a pathagorean triplet with a^2 + b^2 = c^2 theorm
PythagoreanTriplet generateTriplet(int a, int b) {
    PythagoreanTriplet triplet {};
    PythagoreanTriplet empty {};
	if(a >= b || b >= pow(pow(a,2)+pow(b,2),.5)) return triplet;
	triplet.a = a;
	triplet.b = b;
	triplet.c = pow(pow(a,2) + pow(b,2), .5);
	if(test(triplet)) return triplet;
	return empty;
}

PythagoreanTriplet findSumParts(int sum){
	PythagoreanTriplet ret {};
	int i = 1;
	int j = 1;
	bool flag = false;
	while(i < sum){
		while(j < sum){
			ret = generateTriplet(i,j);
			//printf("A: %d B: %d C: %d\n", ret.a, ret.b, ret.c);
			if(ret.a + ret.b + ret.c == sum) flag = test(ret);
			if(flag) return ret;
			++j;
		}
		j = ++i;
	}
	return ret;
}

int main() {
	PythagoreanTriplet triplet {};
	triplet = findSumParts(1000);
	int product = triplet.a * triplet.b * triplet.c;
	printf("The product of %d, %d, and %d is %d\n",triplet.a, triplet.b, triplet.c, product);
    return 0;
}

