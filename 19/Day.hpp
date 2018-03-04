#ifndef _DAY_HPP_
#define _DAY_HPP_

#include <string>

class Day {
public:
	Day(){
		_dayCode = 1;
		dayOfWeek = "Monday";
	}
	
	Day(int day){
		_dayCode = day;
	}

	//Copy Constructor
	Day(const Day& rhs){
		_dayCode = rhs._dayCode;
		dayOfWeek = rhs.dayOfWeek;
	}

	//move Constructor
	Day(Day&& rhs){
		_dayCode = rhs._dayCode;
		dayOfWeek = rhs.dayOfWeek;
	}

	int getCode() const {
		return _dayCode;
	}

	std::string getDayOfWeek(){ 
		return dayOfWeek;
	}

	void setDayOfWeek(int day){
		switch(day){
			case 0: dayOfWeek = "Sunday"; break;
			case 1: dayOfWeek = "Monday"; break;
			case 2: dayOfWeek = "Tuesday"; break;
			case 3: dayOfWeek = "Wednesday"; break;
			case 4: dayOfWeek = "Thursday"; break;
			case 5: dayOfWeek = "Friday"; break;
			case 6: dayOfWeek = "Saturday"; break;
			default: dayOfWeek = "Monday"; break;
		}
	}

	int getDay() const {
		return _dayCode;
	}

	//Overloaded move assignment operator
	Day& operator=(Day&& rhs){
		_dayCode = rhs._dayCode;
		dayOfWeek = rhs.dayOfWeek;
		return *this;
	}

	//Overloaded assignment operator
	Day& operator=(const Day& rhs){
		_dayCode = rhs._dayCode;
		dayOfWeek = rhs.dayOfWeek;
		return *this;
	}

private:
	int _dayCode;
	std::string dayOfWeek;
};

#endif
