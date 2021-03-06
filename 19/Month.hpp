#ifndef _MONTH_HPP_
#define _MONTH_HPP_

#include <string>

enum class MONTH {
	JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, 
	SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER
};

class Month {
public:
	Month()
	: _month(MONTH::JANUARY), _numDays(31)
	{
		//empty
	}

	Month(const int& month){
		switch(month){
			case 1: _month = MONTH::JANUARY; _numDays = 31; break;
			case 2: _month = MONTH::FEBRUARY; _numDays = 28; break;
			case 3: _month = MONTH::MARCH; _numDays = 31; break;
			case 4: _month = MONTH::APRIL; _numDays = 30; break;
			case 5: _month = MONTH::MAY; _numDays = 31; break;
			case 6: _month = MONTH::JUNE; _numDays = 30; break;
			case 7: _month = MONTH::JULY; _numDays = 31; break;
			case 8: _month = MONTH::AUGUST; _numDays = 31; break;
			case 9: _month = MONTH::SEPTEMBER; _numDays = 30; break;
			case 10: _month = MONTH::OCTOBER; _numDays = 31; break;
			case 11: _month = MONTH::NOVEMBER; _numDays = 30; break;
			case 12: _month = MONTH::DECEMBER; _numDays = 31; break;
			default: _month = MONTH::JANUARY; _numDays = 31; break;
		}
		setMonthCode();
	}

	int getCode() const{
		return _monthCode;
	}

	int getNumDays() const {
		return _numDays;
	}

	void setMonthCode(){
		switch(_month){
			case MONTH::JANUARY: _monthCode=6; break;
			case MONTH::FEBRUARY: _monthCode=2; break;
			case MONTH::MARCH: _monthCode=2; break;
			case MONTH::APRIL: _monthCode=5; break;
			case MONTH::MAY: _monthCode=0; break;
			case MONTH::JUNE: _monthCode=3; break;
			case MONTH::JULY: _monthCode=5; break;
			case MONTH::AUGUST: _monthCode=1; break;
			case MONTH::SEPTEMBER: _monthCode=4; break;
			case MONTH::OCTOBER: _monthCode=6; break;
			case MONTH::NOVEMBER: _monthCode=2; break;
			case MONTH::DECEMBER: _monthCode=4; break;
			default: _monthCode=0; break;
		}
	}

	void leapYearFix(){
		switch(_month){
			case MONTH::JANUARY: _monthCode=5; break;
			case MONTH::FEBRUARY: _monthCode=1; _numDays +=1; break;
		}
	}

	int getIntMonth(){
		switch(_month){
			case MONTH::JANUARY: return 1;
			case MONTH::FEBRUARY: return 2;
			case MONTH::MARCH: return 3;
			case MONTH::APRIL: return 4;
			case MONTH::MAY: return 5;
			case MONTH::JUNE: return 6;
			case MONTH::JULY: return 7;
			case MONTH::AUGUST: return 8;
			case MONTH::SEPTEMBER: return 9;
			case MONTH::OCTOBER: return 10;
			case MONTH::NOVEMBER: return 11;
			case MONTH::DECEMBER: return 12;
			default: return 0;
		}
	}

	std::string getMonth(){
		switch(_month){
			case MONTH::JANUARY: return "January";
			case MONTH::FEBRUARY: return "February";
			case MONTH::MARCH: return "March";
			case MONTH::APRIL: return "April";
			case MONTH::MAY: return "May";
			case MONTH::JUNE: return "June";
			case MONTH::JULY: return "July";
			case MONTH::AUGUST: return "August";
			case MONTH::SEPTEMBER: return "September";
			case MONTH::OCTOBER: return "October";
			case MONTH::NOVEMBER: return "November";
			case MONTH::DECEMBER: return "December";
			default: return "NONE";
		}
	}

private:
	MONTH _month;
	int _monthCode;
	int _numDays;
};

#endif
