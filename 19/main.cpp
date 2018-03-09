#include <iostream>

#include "Date.hpp"

using namespace std;

int main(){
/*	
	for(int i = 2000; i <= 2022; ++i){
		Date date = Date(3,11,i);
		date.display();
		cout << " is a ";
		cout << date.getDayOfWeek() << endl << endl;
	}

	int month,day,year;
	cout << "Input a date (press enter after MONTH/DAY/YEAR): \n";
	cin >> month;
	cin >> day;
	cin >> year;
	Date date = Date(month, day, year);
	date.display();
	cout << " is a ";
	cout << date.getDayOfWeek() << endl << endl;
	*/

	int counter = 0;
	for(int year = 1901; year <= 2000; ++year){
		for(int month = 1; month <= 12; ++month){
			for(int day = 1; day <= 31; ++day){
				Date date = Date(month, day, year);
				if(date.getDay() <= -1) continue;
				if(date.getDayOfWeek() == "Sunday" && day == 1) ++counter;
				//printf("Day: %d    DayOfWeek: ", day);
				//cout << date.getDayOfWeek() << endl;
			}
		}
	}

	printf("There are %d Sundays from %d to %d that fall on the 1st of the month\n", counter, 1901, 2000);

	return 0;
}
