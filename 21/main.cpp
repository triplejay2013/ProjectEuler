#include <iostream>
#include <string>
#include <ctime>

/*
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/

using namespace std;

long d(int n){
	long sum=0;
	for(int i = 1; i <= n/2; ++i){
		if(n%i == 0){
			sum+=i;
		}
	}
	return sum;
}

bool amicablePair(long a, long b){
	if(a == b) return false;
	if(d(a) == b && d(b) == a) return true;
	return false;
}

int main(){
	//Program to Solve Project Euler Problem
	//impelmenting a timer just for fun
	clock_t start;
	double duration;
	start = clock();

	int upperLimit = 10000;
	long sum = 0;
	bool flag = false;
	cout << "A list of all amicable numbers less than " << upperLimit << ":\n";
	for(int i = 1; i < upperLimit; ++i){
		if(i %1000 == 0){
			duration = (clock() - start) / (double) CLOCKS_PER_SEC;
			cout << "Index " << i << " " << duration << " seconds\n";
		}		
		for(int j = i; j < upperLimit; ++j){
			if(amicablePair(i, j)){
				flag = true;
				printf("\t%d is amicable with %d\n", i, j);
				sum += i + j;
			}
		}
	}

	if(!flag) cout << "\tNo number is amicable with " << upperLimit << "\n";
	else printf("The sum of all amicable numbers less than %d is %lu\n", upperLimit, sum);

	duration = (clock() - start)/ (double) CLOCKS_PER_SEC;
	cout << "The process took " << duration << " seconds\n";



/*
	//Sampel Program
	while(true){
		int a,b;
		cout << "Input two numbers:\n";
		cin >> a >> b;
		if(a <= 0 || b <= 0) break;
		printf("%d and %d are amicable pairs? %s\n\n", a, b, amicablePair(a,b) ? "True" : "False");
	}
	*/
	return 0;
}
