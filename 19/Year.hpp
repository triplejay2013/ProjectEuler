#ifndef _YEAR_HPP_
#define _YEAR_HPP_

#include <string>

class Year {
public:
	//Constructors & Deconstructors
	Year()
	: _leapYear(false), _year(2000)
	{
		calculateYearCode();
	}

	Year(int year){
		if(year%4 == 0 ) _leapYear = true;
		_year = year;
		calculateYearCode();
	}

	Year(std::string year){
		_year = std::stoi(year);
		if(_year%4 == 0 ) _leapYear = true;
		calculateYearCode();
	}

	//getters and setters
	bool getLeapYear() const{
		return _leapYear;
	}

	int getYear() const{
		return _year;
	}

	//class methods
	void calculateYearCode(){
		int temp = _year;
		int x;
		if(_year >= 2000 && _year <= 2099){
			//strip away 2000 for easier calculation
			temp-=2000;
			x = temp;
			temp/=4;
			x+= temp;
			//reduce by increments of seven
			while(x>=0){
				x-=7;
			}
			//fix if reduced past zero
			if(x < 0) x+=7;
			_yearCode = x;
		}
	}

private:
	//flag to determine if the year is a leap year
	bool _leapYear;
	//integer representation of the year
	int _year;
	int _yearCode;
};

#endif
