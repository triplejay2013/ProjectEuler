#include <iostream>

#include "Date.hpp"

using namespace std;

int main(){
	for(int i = 2000; i <= 2022; ++i){
		Date date = Date(3,11,i);
		date.display();
		cout << " is a ";
		cout << date.getDayOfWeek() << endl << endl;
	}

	return 0;
}
