#ifndef _DATE_HPP_
#define _DATE_HPP_

#include "Year.hpp"
#include "Month.hpp"
#include "Day.hpp"

class Date {
public:
	Date(){
		_year = Year();
		_month = Month();
		_day = Day();
	}

	Date(int year, int month, int day){
		_year = Year(year);
		_month = Month(month);
		_day = Day(day);
	}

	Date(Year year, Month month, Day day){
		_year = year;
		_month = month;
		_day = day;
	}
	//getDate()
	//display()
	//toString()
private:
	Year _year;
	Month _month;
	Day _day;
};

#endif
