#ifndef _AUGUST_HPP_
#define _AUGUST_HPP_

#include "Month.hpp"

class August : public Month {
public:
	August(bool duringLeapYear = false)
	: 	Month(duringLeapYear, 1, 8)
	{
		//empty
	}
private:
};

#endif
