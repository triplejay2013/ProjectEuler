#ifndef _JANUARY_HPP_
#define _JANUARY_HPP_

#include "Month.hpp"

class January : public Month {
public:
	January(bool duringLeapYear = false)
	: Month(duringLeapYear, 6, 1)
	{
		//empty
	}

private:
};

#endif
