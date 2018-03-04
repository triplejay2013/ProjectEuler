#ifndef _DATE_HPP_
#define _DATE_HPP_

#include "Year.hpp"
#include "Month.hpp"
#include "Day.hpp"

#include "February.hpp"
#include "January.hpp"
#include "March.hpp"
#include "January.hpp"
#include "February.hpp"
#include "March.hpp"
#include "April.hpp"
#include "May.hpp"
#include "June.hpp"
#include "July.hpp"
#include "August.hpp"
#include "September.hpp"
#include "October.hpp"
#include "November.hpp"
#include "December.hpp"

class Date {
public:
	Date(){
		_year = Year();
		_month = getMonth(1);
		_day = Day();
	}

	Date(const int& day, const int& month, const int& year)
	:	_year(Year(year)), _month(getMonth(month)), _day(Day(day))
	{
		//empty
	}

	std::string getDayOfWeek(){
		int sum = _year.getCode() + _month.getCode() + _day.getCode();
		while(sum >= 0){
			sum -= 7;
		}
		if(sum < 0) sum +=7;
		_day.setDayOfWeek(sum);
		return _day.getDayOfWeek();
	}

	void display() {
		printf("%d/%d/%d", _day.getDay(), _month.getMonth(), _year.getYear());
	}

	//toString()
private:
	Year _year;
	Month _month;
	Day _day;

	Month getMonth(int month){
		switch(month){
			case 1: return January(_year.getLeapYear());
			case 2: return February(_year.getLeapYear());
			case 3: return March(_year.getLeapYear());
			case 4: return April(_year.getLeapYear());
			case 5: return May(_year.getLeapYear());
			case 6: return June(_year.getLeapYear());
			case 7: return July(_year.getLeapYear());
			case 8: return August(_year.getLeapYear());
			case 9: return September(_year.getLeapYear());
			case 10: return October(_year.getLeapYear());
			case 11: return November(_year.getLeapYear());
			case 12: return December(_year.getLeapYear());
			default: return January(_year.getLeapYear());
		}
	}
};

#endif
