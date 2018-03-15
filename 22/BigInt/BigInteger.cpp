/*Justin Johnson
A01936095
Converting ints and strings to Big Integers
version 1.0
*/
#include <iostream>
#include <algorithm>
#include <cmath>
#include "BigInteger.hpp"
//#include <cstring> //for memcpy
#include <string>


using namespace std;

//Default Constructor
BigInteger::BigInteger(){
	m_sizeReserved = 4; 
	m_digitCount = 0;
	int x = 0;

	m_number = new char[m_sizeReserved];
    for (int i = 0; i < m_sizeReserved; ++i){
        m_number[i] = 0;
    }
}

//Integer Constructor (conversion) 
BigInteger::BigInteger(int x){
	m_digitCount = 0;
    int pos = 0;
	m_sizeReserved = 0;
	int num = x;
	while (x > 0){//saves digitCount
		x % 10;
		x /= 10;
		m_digitCount++;
	}
    if (num == 0){
        m_digitCount = 4;
    }
	m_sizeReserved = m_digitCount;
    m_number = new char[m_sizeReserved];
    while (num > 0){
        m_number[pos] = num % 10;
        num /= 10;
        pos++;
    }
}

//String Constructor
BigInteger::BigInteger(string x){
	m_sizeReserved = x.length();
	m_digitCount = 0;
    m_number = new char[m_sizeReserved];
    for (int i = m_sizeReserved -1; i >= 0; i--){
        m_number[m_digitCount] = x[i] - '0';
        m_digitCount++;
    }
}

//Copy Constructor
BigInteger::BigInteger(const BigInteger& rOther){
	m_number = new char[rOther.m_sizeReserved];
    m_sizeReserved = rOther.m_sizeReserved;
    m_digitCount = rOther.m_digitCount;

	for (int i = 0; i < m_sizeReserved; i++){
		m_number[i] = rOther.m_number[i];
	}
}

//move Constructor
BigInteger::BigInteger(BigInteger&& rOther){
    m_number = rOther.m_number;
    rOther.m_number = NULL;
    m_sizeReserved = rOther.m_sizeReserved;
    rOther.m_sizeReserved = 0;
    m_digitCount = rOther.m_digitCount;
    rOther.m_digitCount = 0;
}

//Overloaded move assignment operator
BigInteger& BigInteger::operator=(BigInteger&& rOther){
    m_number = rOther.m_number;
    rOther.m_number = NULL;
    m_sizeReserved = rOther.m_sizeReserved;
    rOther.m_sizeReserved = 0;
    m_digitCount = rOther.m_digitCount;
    rOther.m_digitCount = 0;

    return *this;
}

//Overloaded assignment operator
BigInteger& BigInteger::operator=(const BigInteger& rOther){ // overridden
    m_sizeReserved = rOther.m_sizeReserved;
    m_digitCount = rOther.m_digitCount;

	for (int i = 0; i < m_sizeReserved; i++){
        this->m_number[i] = rOther.m_number[i];
    } 

	return *this;
}

//Overloaded addition operator (BigInt + int)
BigInteger BigInteger::operator+(const int& rOther){
    BigInteger rhs(rOther);
	BigInteger result = rhs + *this;

	return result;
}

//overloaded addition operator (BIGINT + BIGINT)
BigInteger BigInteger::operator+(const BigInteger& rhs){
	BigInteger result;
	unsigned int length = (this->m_digitCount > rhs.m_digitCount) ? this->m_digitCount : rhs.m_digitCount;

	int carry = 0;
	for (unsigned int digit = 0; digit < length; digit++){
		int v1 = this->getDigit(digit);
		int v2 = rhs.getDigit(digit);
		int sum = v1 + v2 + carry;
		int single = sum % 10;
		carry = ((sum - single) > 0) ? (sum - single) / 10 : 0;

		result.setDigit(digit, single);
	}
	if (carry > 0){
		result.setDigit(length, carry);
	}

	return result;
}

//overloaded plus equals operator (BIGINT += BIGINT)
BigInteger& BigInteger::operator+=(const BigInteger& rOther){
    *this = *this + rOther;

    return *this;
}

//multiplies BigInt * BigInt
BigInteger BigInteger::operator*(const BigInteger& rhs){
	BigInteger result;
	const BigInteger& b = (this->m_digitCount < rhs.m_digitCount) ? *this : rhs;
	const BigInteger& t = (this->m_digitCount < rhs.m_digitCount) ? rhs : *this;
    BigInteger temp;

	for (unsigned int bDigit = 0; bDigit < b.m_digitCount; bDigit++){
		int v1 = b.getDigit(bDigit);
		int carry = 0;
		for (unsigned int tDigit = 0; tDigit < t.m_digitCount; tDigit++){
			int v2 = t.getDigit(tDigit);
			int sum = v1 * v2 + carry;
			int single = sum % 10;
			carry = ((sum - single) > 0) ? (sum - single) / 10 : 0;

			temp.setDigit(bDigit + tDigit, single);
		}
		if (carry > 0){
			temp.setDigit(bDigit + t.m_digitCount, carry);
		}
		result = result + temp;
	}

	return result;
}

//multiplies BigInt * BigInt
BigInteger& BigInteger::operator*=(const BigInteger& rOther){
    *this = *this * rOther;

    return *this;
}


bool BigInteger::operator<=(const BigInteger& rhs){
	if (this->m_digitCount < rhs.m_digitCount) return true;
	if (this->m_digitCount > rhs.m_digitCount) return false;
	// Have to go digit by digit

	for (int digit = m_digitCount - 1; digit >= 0; digit--){
		if (this->m_number[digit] < rhs.m_number[digit]) return true;
		if (this->m_number[digit] > rhs.m_number[digit]) return false;
	}

	return true;
}

bool BigInteger::operator==(const BigInteger& rOther){
    bool check = false;
	if (this->m_digitCount < rOther.m_digitCount) check = false;
    else if (this->m_digitCount > rOther.m_digitCount) check =  false;

    for (int digit = m_digitCount -1; digit >= 0; digit--){
        if(this->m_number[digit] == rOther.m_number[digit]){
            check = true;
        }
        else{
            return false;
        }
    }

    return check;
}

//pre-increment operator
BigInteger& BigInteger::operator++(){
    BigInteger one(1);// use 'delete'?
    *this += one;

    return *this;
}

//post-increment operator
BigInteger BigInteger::operator++(int){
    BigInteger one(1);// use 'delete'?
    BigInteger retVal = *this;
    *this += one;

    return retVal;
}

//double operator override
BigInteger::operator double() const{
    double tmp = 0;
    for (int digit = m_digitCount - 1; digit >=0; digit--){
        tmp += this->m_number[digit];
        tmp *= 10;
    }
    tmp /= 10;

    return tmp;
}

//ostream operator override
ostream& operator<<(ostream& os, const BigInteger& rOther){
    for (int digit = rOther.m_digitCount -1; digit >=0; digit--){
        os << rOther.getDigit(digit);
    }

    return os;
}

//multiplies BigInt * int
BigInteger BigInteger::multiply(const BigInteger& x, unsigned int y){
	BigInteger result;
	unsigned int carry = 0;
	unsigned int pos = 0;

	for (unsigned int digit = 0; digit < x.m_digitCount; digit++){
		carry += x.getDigit(digit) * y;
		result.setDigit(pos++, carry % 10);
		carry /= 10;
	}

    if (carry > 0){
        result.setDigit(pos, carry);
    }

	return result;
}

//Displays
void BigInteger::display(bool debug){
	for (unsigned int digit = m_digitCount; digit > 0; digit--){
		cout << static_cast<int>(m_number[digit - 1]);
	}

	if (debug){
		cout << " [size = " << m_sizeReserved << ", digit count = " << m_digitCount << "] " << endl;
	}
}

//Destructor
BigInteger::~BigInteger(){
    if (m_number != NULL){
        delete [] m_number;
        m_number = NULL;
    }
}

//returns digit at 'position'
int BigInteger::getDigit(unsigned int position) const{
	if (position < m_digitCount){
		return m_number[position];
	}

	return 0;
}

//returns length of BigInt ex: 12345 has length of 5
int BigInteger::getLength() const {
	return m_digitCount;
}

//Sets a position in a array to the passed in digit
void BigInteger::setDigit(unsigned int position, char digit){
	if (position >= m_sizeReserved){//if wanting to insert in a position that doesn't exist
		m_sizeReserved *= 2;//double array size

		char* temp = m_number;//creats new pointer that points to teh same values as m_number
		m_number = new char[m_sizeReserved];//redefines m_number with a different pointer to an empty array
        for (int i = 0; i < m_digitCount; i++){
            m_number[i] = temp[i];
        }
        delete [] temp;
        temp = NULL;
        m_number[position] = digit;
	}
    else{
        m_number[position] = digit;
    }
    if (position == m_digitCount){
        m_digitCount++;
    }
}
