#ifndef _BIGINTEGER_HPP_
#define _BIGINTEGER_HPP_

#include <string>

using namespace std;

class BigInteger
{
public:
    //MY CONSTRUCTORS
	BigInteger();//default Constructor
	BigInteger(int x);//Int constructor (conversion)
	BigInteger(string x);//String Constructor (conversion)
	BigInteger(const BigInteger& rOther);//copy constructor
    BigInteger(BigInteger&& rOther);//move constructor

    //OVERLOADED OPERATORS
    BigInteger& operator=(BigInteger&& rOther);//overloaded move = operator
	BigInteger& operator=(const BigInteger& rOther);//overloaded = operator (BIGINT)
    BigInteger operator+(const BigInteger& rOther);//overloaded + operator (BIGINT + BIGINT)
    BigInteger operator+(const int& rOther);//overloaded + operator (BIGINT + INT)
    BigInteger& operator+=(const BigInteger& rOther);//overloaded += operator (BIGINT += BIGINT)
    BigInteger operator*(const BigInteger& rhs);//overloaded * operator (BigInt * BigInt)
    BigInteger& operator*=(const BigInteger& rOther);//overloaded *= operator (BigInt *= BigInt)
    bool operator<=(const BigInteger& rhs);//overloaded <= operator (BigInt <= BigInt)
    bool operator==(const BigInteger& rOther);//overloaded == operator (BigInt == BigInt)
    BigInteger& operator++();//pre_increment ++operator
    BigInteger operator++(int);//post-increment operator++
    operator double() const;//overloaded double

    //PREVIOUS ASSIGNMENT FUNCTIONS
	static BigInteger multiply(const BigInteger& x, unsigned int y);//BigINt*int
	void display(bool debug = false);
	~BigInteger();//deconstructor (deletes allocated memory)

private:
	char* m_number;		// Internal representation of the number.
	unsigned int m_sizeReserved;	// Total size of the allocated space used to internally store the number
	unsigned int m_digitCount;	// How many digits are in the number.

	int getDigit(unsigned int position) const;
	void setDigit(unsigned int position, char digit);

	void initializeWithInt(int x);
    friend ostream& operator<<(ostream& os, const BigInteger& rOther);

};

ostream& operator<<(ostream& os, const BigInteger& rOther);

#endif
