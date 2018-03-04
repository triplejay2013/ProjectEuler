#ifndef _MARCH_HPP_
#define _MARCH_HPP_

#include "Month.hpp"

class March : public Month {
public:
	March(bool duringLeapYear = false)
	:	Month(duringLeapYear, 2)
	{
		//empty
	}
private:
};

#endif
