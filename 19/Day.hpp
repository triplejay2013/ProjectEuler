#ifndef _DAY_HPP_
#define _DAY_HPP_

#include <string>

enum class DAY {
	MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
};

class Day {
public:
	Day()
	: _date(1), _day(DAY::MONDAY)
	{

	}

	Day(const int& date)
	: _date(date), _day(DAY::MONDAY)
	{

	}

	int getCode(){
		return _date;
	}

	std::string getDay(){
		switch(_day){
			case DAY::MONDAY: return "Monday";
			case DAY::TUESDAY: return "Tuesday";
			case DAY::WEDNESDAY: return "Wednesday";
			case DAY::THURSDAY: return "Thursday";
			case DAY::FRIDAY: return "Friday";
			case DAY::SATURDAY: return "Saturday";
			case DAY::SUNDAY: return "Sunday";
		}
		return "NONE";
	}

	int getIntDay(){
		return _date;
	}

	void setDay(const int& day){
		switch(day){
			case 1: _day = DAY::MONDAY; break;
			case 2: _day = DAY::TUESDAY; break;
			case 3: _day = DAY::WEDNESDAY; break;
			case 4: _day = DAY::THURSDAY; break;
			case 5: _day = DAY::FRIDAY; break;
			case 6: _day = DAY::SATURDAY; break;
			case 7: _day = DAY::SUNDAY; break;
			default: _day = DAY::SUNDAY; break;
		}
	}
private:
	int _date;
	DAY _day;
};

#endif
