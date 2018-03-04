#ifndef _NOVEMBER_HPP_
#define _NOVEMBER_HPP_

#include "Month.hpp"

class November : public Month {
public:
	November(bool duringLeapYear = false)
	:	Month(duringLeapYear, 2, 11)
	{
		//empty
	}
private:
};

#endif
