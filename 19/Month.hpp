#ifndef _MONTH_HPP_
#define _MONTH_HPP_

class Month {
public:
	Month(bool duringLeapYear = false, int monthCode = 1)
	: _duringLeapYear(duringLeapYear), _monthCode(monthCode)
	{
		if(duringLeapYear) _monthCode -=1;
	}

	Month(int month){
	/*
		switch(month){
			case 1: _month  = new January();
			case 2: _month = new February();
			case 3: _month = new March();
			case 4: _month = new April();
			case 5:	_month = new May();
			case 6: _month = new June();
			case 7: _month = new July();
			case 8: _month = new August();
			case 9: _month = new September();
			case 10: _month = new October();
			case 11: _month = new November();
			case 12: _month = new December();
		}
		*/
	}

	int getCode(){
		return _monthCode;
	}

private:
	Month* _month;
	int _monthCode;
	bool _duringLeapYear;
};

#endif
