#ifndef _MONTH_HPP_
#define _MONTH_HPP_

class Month {
public:
	//default constructor
	Month(bool duringLeapYear = false, int monthCode = 1, int month = 1)
	: _duringLeapYear(duringLeapYear), _monthCode(monthCode), _month(month)
	{
		if(_duringLeapYear) _monthCode -=1;
	}

	//Copy Constructor
	Month(const Month& rhs){
		_monthCode = rhs._monthCode;
		_month = rhs._month;
		_duringLeapYear = rhs._duringLeapYear;
	}

	//move Constructor
	Month(Month&& rhs){
		_monthCode = rhs._monthCode;
		_month = rhs._month;
		_duringLeapYear = rhs._duringLeapYear;
	}

	int getCode() const {
		return _monthCode;
	}

	int getMonth() const {
		return _month;
	}

	//Overloaded move assignment operator
	Month& operator=(Month&& rhs){
		_monthCode = rhs._monthCode;
		_month = rhs._month;
		_duringLeapYear = rhs._duringLeapYear;
		return *this;
	}

	//Overloaded assignment operator
	Month& operator=(const Month& rhs){
		_monthCode = rhs._monthCode;
		_month = rhs._month;
		_duringLeapYear = rhs._duringLeapYear;
		return *this;
	}

private:
	int _monthCode;
	int _month;
	bool _duringLeapYear;

};

#endif
