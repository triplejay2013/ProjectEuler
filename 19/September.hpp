#ifndef _SEPTEMBER_HPP_
#define _SEPTEMBER_HPP_

#include "Month.hpp"

class September : public Month {
public:
	September(bool duringLeapYear = false)
	:	Month(duringLeapYear, 4)
	{
		//empty
	}
private:
};

#endif
