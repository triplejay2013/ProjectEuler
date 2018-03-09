#ifndef _DATE_HPP_
#define _DATE_HPP_

#include "Year.hpp"
#include "Month.hpp"
#include "Day.hpp"

class Date {
public:
	Date()
	: _year(Year(2001)), _month(Month(1)), _day(Day(1))
	{
		calculateCode();
	}

	Date(const int& month, const int& day, const int& year){
		_month = Month(month);
		if(day > _month.getNumDays()) _day = Day(-1);
		else _day = Day(day);
		_year = Year(year);
		if(_year.getLeapYear()) _month.leapYearFix();
		calculateCode();
		_day.setDay(_dateCode);
	}

	std::string getDayOfWeek(){
		return _day.getDay();
	}

	int getDay(){
		return _day.getIntDay();
	}

	void display(){
		//printf("Month: %d  Day: %d    Year: %d\n", _month.getCode(), _day.getCode(), _year.getCode());
		printf("%d/%d/%d\n", _month.getIntMonth(), _day.getIntDay(), _year.getIntYear());
	}


private:
	void calculateCode(){
		_dateCode = _day.getCode() + _month.getCode() + _year.getCode();
		while(_dateCode >= 0){
			_dateCode -= 7;
		}
		if(_dateCode < 0) _dateCode += 7;
	}

	Year _year;
	Month _month;
	Day _day;
	int _dateCode;
};

#endif
