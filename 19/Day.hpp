#ifndef _DAY_HPP_
#define _DAY_HPP_

class Day {
public:
	Day(){
		_dayCode = 1;
	}
	
	Day(int day){
		_dayCode = day;
	}
private:
	int _dayCode;
};

#endif
