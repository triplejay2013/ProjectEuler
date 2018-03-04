#include <iostream>

#include "Month.hpp"
#include "February.hpp"
#include "January.hpp"
#include "March.hpp"
#include "January.hpp"
#include "February.hpp"
#include "March.hpp"
#include "April.hpp"
#include "May.hpp"
#include "June.hpp"
#include "July.hpp"
#include "August.hpp"
#include "September.hpp"
#include "October.hpp"
#include "November.hpp"
#include "December.hpp"

using namespace std;

int main(){
	Month* first = new January();
	Month* second = new February();
	Month* third = new March();
	Month* third = new March();
	Month* third = new March();
	Month* third = new March();
	Month* third = new March();
	Month* third = new March();
	Month* third = new March();
	Month* third = new March();
	Month* third = new March();
	Month* third = new March();

	cout << "January Code: " << first->getCode() << endl;
	cout << "February Code: " << second->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	return 0;
}
