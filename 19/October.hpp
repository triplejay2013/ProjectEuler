#ifndef _OCTOBER_HPP_
#define _OCTOBER_HPP_

#include "Month.hpp"

class October : public Month {
public:
	October(bool duringLeapYear = false)
	:	Month(duringLeapYear, 6)
	{
		//empty
	}
	
private:
};

#endif
