#ifndef _MAY_HPP_
#define _MAY_HPP_

#include "Month.hpp"

class May : public Month {
public:
	May(bool duringLeapYear = false)
	:	Month(duringLeapYear, 0)
	{
		//empty
	}

private:
};

#endif
