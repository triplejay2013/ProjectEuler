#ifndef _DECEMBER_HPP_
#define _DECEMBER_HPP_

#include "Month.hpp"

class December : public Month {
public:
	December(bool duringLeapYear = false)
	:	Month(duringLeapYear, 4)
	{
		//empty
	}
private:
};

#endif
