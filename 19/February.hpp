#ifndef _FEBRUARY_HPP_
#define _FEBRUARY_HPP_

#include "Month.hpp"

class February : public Month {
public:
	February(bool duringLeapYear = false)
	: Month(duringLeapYear, 2)
	{
		//empty
	}

private:
};

#endif
