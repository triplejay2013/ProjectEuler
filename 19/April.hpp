#ifndef _APRIL_HPP_
#define _APRIL_HPP_

#include "Month.hpp"

class April : public Month {
public:
	April(bool duringLeapYear = false)
	:	Month(duringLeapYear, 5,4)
	{
		//empty
	}
private:
};

#endif
