#ifndef _JUNE_HPP_
#define _JUNE_HPP_

#include "Month.hpp"

class June : public Month {
public:
	June(bool duringLeapYear = false)
	: 	Month(duringLeapYear, 3, 6)
	{
		//empty
	}
		
private:
};

#endif
