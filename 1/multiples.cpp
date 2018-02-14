#include <iostream>

using namespace std;

/*
 * adds up multiples of factor1 and factor2 up until the limit
 * ex: f1=3 f2=5 lim=10, sum == 23, factors are 3,5,6,9
*/
int multipleSum(const int& factor1, const int& factor2, const int& limit){
	int sum=0;
	for(int i = 1; i < limit; ++i){
		if(i%factor1 == 0 || i%factor2 == 0)
			sum+=i;
	}
	return sum;
}

int main(){
	cout << multipleSum(3,5,10) << endl;
	cout << multipleSum(3,5,1000) << endl;

	return 0;
}
