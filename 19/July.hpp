#ifndef _JULY_HPP_
#define _JULY_HPP_

#include "Month.hpp"

class July : public Month {
public:
	July(bool duringLeapYear = false)
	:	Month(duringLeapYear, 5)
	{
		//empty
	}
private:
};

#endif
