#include <iostream>
#include <vector>

using namespace std;

vector<long long> generatePrimes(const int& upperBound){
	vector<bool> sieve(upperBound,true);
	cout << "Beginning sieve creation" << endl;
	for(long long i = 2; i <= upperBound+1; ++i){
		if(sieve[i]){
			for(long long j = i*i; j <= upperBound+1; j += i){
				sieve[j] = false;
			}
		}
	}

	cout << "Initializing vector of primes" << endl;
	vector<long long> primes;
	int counter = 0;
	for(long long i = 2; i <= upperBound; ++i){
		if(i%1000000 == 0) cout << i << endl;
		if(sieve[i]){
			primes.push_back(i);
		}
	}
	return primes;
}

void print(const vector<long long>& vec){
	cout << "Printing out list of primes" << endl;
	for(int i = 0; i < vec.size(); ++i){
		if(vec[i] == 0) break;
		cout << vec[i] << endl;
	}
}

long long sumOfPrimes(const vector<long long>& primes){
	cout << "Summing up vector of primes" << endl;
	long long sum = 0;
	for(int i = 0; i < primes.size(); ++i){
		sum += primes[i];
	}
	return sum;
}

int main(){
	char quit;
	vector<long long> primes;
	int lowerBound, upperBound;
	while(true){
		cout << "UpperBound:(ex 2000 means sum of primes up to that number): ";
		cin >> upperBound;
		cout << endl;
		primes = generatePrimes(upperBound);
		printf("Sum of primes from 2 to %d is %lld\n", upperBound, sumOfPrimes(primes));
		cout << "Press q to quit, p to print\n";
		cin >> quit;
		if(quit == 'p' || quit == 'P') {
			print(primes);
			cout << "Press q to quit\n";
			cin >> quit;
		}
		if(quit == 'q' || quit == 'Q') break;
	}
	
	return 0; 
}
