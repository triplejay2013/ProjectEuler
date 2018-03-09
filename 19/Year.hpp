#ifndef _YEAR_HPP_
#define _YEAR_HPP_

#include <string>

class Year {
public:
	Year()
	: _year(2001), _yearCode(1)
	{
		calculateCode();
	}

	Year(const int& year){
		_year = year;
		calculateCode();
		isLeapYear();
	}

	int getCode(){
		return _yearCode;
	}

	int getIntYear(){
		return _year;
	}

	bool getLeapYear(){
		return _leapYear;
	}

private:

	void isLeapYear(){
		std::string temp = std::to_string(_year);
		std::string digits = temp.substr(temp.length()-2, 2);
		int year = std::stoi(digits);
		if(year%4 == 0) _leapYear = true;
		else{ _leapYear = false;}
	}

	void calculateCode(){
		std::string str = std::to_string(_year);
		std::string digits = str.substr(str.length()-2, 2);
		int year = std::stoi(digits);
		int code = year;
		int temp = year/4;
		code += temp;
		while(code >= 0){
			code -= 7;
		}
		if(code < 0) code += 7;
		_yearCode = code;
	}

	int _year;
	int _yearCode;
	bool _leapYear;
};

#endif
