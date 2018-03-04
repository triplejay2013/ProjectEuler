//TODO make actual test suite class...see USU 1440 class notes
#include <iostream>

#include "../Date.hpp"
#include "../Month.hpp"
#include "../February.hpp"
#include "../January.hpp"
#include "../March.hpp"
#include "../January.hpp"
#include "../February.hpp"
#include "../March.hpp"
#include "../April.hpp"
#include "../May.hpp"
#include "../June.hpp"
#include "../July.hpp"
#include "../August.hpp"
#include "../September.hpp"
#include "../October.hpp"
#include "../November.hpp"
#include "../December.hpp"

using namespace std;

int main(){
	Month* first = new January();
	Month* second = new February();
	Month* third = new March();
	Month* fourth = new April();
	Month* fifth = new May();
	Month* sixth = new June();
	Month* seventh = new July();
	Month* eighth = new August();
	Month* ninth = new September();
	Month* tenth = new October();
	Month* eleventh = new November();
	Month* twelvth = new December();

	cout << "January Code: " << first->getCode() << endl;
	cout << "February Code: " << second->getCode() << endl;
	cout << "March Code: " << third->getCode() << endl;
	cout << "April Code: " << fourth->getCode() << endl;
	cout << "May Code: " << fifth->getCode() << endl;
	cout << "June Code: " << sixth->getCode() << endl;
	cout << "July Code: " << seventh->getCode() << endl;
	cout << "August Code: " << eighth->getCode() << endl;
	cout << "September Code: " << ninth->getCode() << endl;
	cout << "October Code: " << tenth->getCode() << endl;
	cout << "November Code: " << eleventh->getCode() << endl;
	cout << "December Code: " << twelvth->getCode() << endl;
	return 0;
}
