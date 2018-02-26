#ifndef _NUMBER_CONVERTER_HPP_
#define _NUMBER_CONVERTER_HPP_

#include <iostream> 
#include <map>
#include <sstream>

using namespace std;

/*
This class is used to convert integer numbers to their written english representations
This will only work for numbers 0 - 9999
TODO Potentaily add Russian and other language capabilities?
*/
class NumberConverter{

private:
	//holds integer and string values for english numbers 0-99
	map<int,string> m_numbers;

	//Display Helper Methods
	string displayThousands(const int& num);
	string displayHundreds(const int& num);
	string displayTens(const int& num);
	string displayOnes(const int& num);

	//Formatting
	string removeWhitespace(string str);

public:
	//Constructor and Deconstructor
	NumberConverter();
	~NumberConverter();

	//Methods
	int count(const int& num);
	long countRange(const int& lower, const int& upper);
	string display(const int& num);
	int toInt(const string& str) const;
	void print() const;
	void load();
};

#endif

/*
std::ostream& operator << (std::ostream& os, const Number& obj){
	os << static_cast<std::underlying_type<Number>::type>(obj);
	return os;
}
I used this code for enum classes....might come in handy one day
*/
