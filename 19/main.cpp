#include <iostream>

#include "Date.hpp"

using namespace std;

int main(){
	Date date = Date(11,3,2061);
	date.display();
	cout << endl;
	cout << date.getDayOfWeek() << endl;
	date = Date(12,3,2061);
	date.display();
	cout << endl;
	cout << date.getDayOfWeek() << endl;
	return 0;
}
