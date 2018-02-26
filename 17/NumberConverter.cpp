#include "NumberConverter.hpp"

NumberConverter::NumberConverter(){
	load();
}

NumberConverter::~NumberConverter(){
	//empty
}

void NumberConverter::load(){
	m_numbers[0]="Zero"; m_numbers[1]="One"; m_numbers[2]="Two"; m_numbers[3]="Three"; 
	m_numbers[4]="Four"; m_numbers[5]="Five"; m_numbers[6]="Six"; m_numbers[7]="Seven"; 
	m_numbers[8]="Eight"; m_numbers[9]="Nine"; m_numbers[10]="Ten"; m_numbers[11]="Eleven"; 
	m_numbers[12]="Twelve"; m_numbers[13]="Thirteen"; m_numbers[14]="Fourteen"; 
	m_numbers[15]="Fifteen"; m_numbers[16]="Sixteen"; m_numbers[17]="Seventeen"; 
	m_numbers[18]="Eighteen"; m_numbers[19]="Nineteen"; m_numbers[20]="Twenty"; 
	m_numbers[30]="Thirty"; m_numbers[40]="Forty"; m_numbers[50]="Fifty"; 
	m_numbers[60]="Sixty"; m_numbers[70]="Seventy"; m_numbers[80]="Eighty"; 
	m_numbers[90]="Ninety"; 
}

void NumberConverter::print() const {
	/*
	map<int,string>::iterator pos;
	for(pos = m_numbers.begin(); pos != m_numbers.end(); ++pos){
		cout << "key: \"" << pos->first << "\" " 
			<< "value: " << pos->second << endl;
	}
	*/
	cout << "NOTHING FOR NOW FOLKS\n";
}

int NumberConverter::toInt(const string& str) const {
	stringstream ss(str);
	int ret;
	ss >> ret;
	return ret;
}

//single digit numbers 0-9
string NumberConverter::displayOnes(const int& num){
	if(num == 0) return "";
	string str=to_string(num);
	if(str.length()!=1) return str;
	return m_numbers[num]; 
}

//double digit number 10-99
string NumberConverter::displayTens(const int& num){
	if(num==0)return "";
	string str=to_string(num);
	string temp0, temp1;
	int tens, ones;
	if(str.length() == 1) return displayOnes(num);
	if(str.length() == 2){
		temp0=str[0]; temp1=str[1];
		tens=toInt(temp0); ones=toInt(temp1);
		switch(tens){
			case 0: return m_numbers[ones];
			case 1: 
			switch(ones){
				case 0: return m_numbers[10];
				case 1: return m_numbers[11];
				case 2: return m_numbers[12];
				case 3: return m_numbers[13];
				case 4: return m_numbers[14];
				case 5: return m_numbers[15];
				case 6: return m_numbers[16];
				case 7: return m_numbers[17];
				case 8: return m_numbers[18];
				case 9: return m_numbers[19];
			}
		}
		if(tens!=1)tens*=10; if(ones==0) return m_numbers[tens];
		return m_numbers[tens]+ " " + m_numbers[ones];
	}
	//str.length() >= 3
	return str;
}

//triple digit numbers 100-999
string NumberConverter::displayHundreds(const int& num){
	if(num==0)return "";
	string str=to_string(num);
	string temp0, temp1, temp2;
	int hundreds, tens, ones;
	if(str.length() == 1) return displayOnes(num);
	if(str.length() == 2) return displayTens(num);
	if(str.length() == 3){
		temp0=str[0]; temp1=str[1]; temp2=str[2];
		hundreds=toInt(temp0); tens=toInt(temp1); ones=toInt(temp2);
		tens *= 10; 
		switch(hundreds){
			case 0: return displayTens(tens + ones);
			default:
				switch(tens){
					case 0: 
						if(ones==0) return m_numbers[hundreds] + " Hundred " + displayOnes(ones);
						return m_numbers[hundreds] + " Hundred and " + displayOnes(ones);
					default:
						switch(ones){
							case 0: return m_numbers[hundreds] + " Hundred and " + displayTens(tens);;
							default: return m_numbers[hundreds] + " Hundred and " + displayTens(tens + ones);
						}
				}
		}
	}
	//str.length() >= 4
	return str;
}

string NumberConverter::displayThousands(const int& num){
	string str=to_string(num);
	if(num==0)return str;
	string temp0, temp1, temp2, temp3;
	int thousands, hundreds, tens, ones;
	if(str.length() == 1) return displayOnes(num);
	if(str.length() == 2) return displayTens(num);
	if(str.length() == 3) return displayHundreds(num);
	if(str.length() == 4){
		temp0=str[0]; temp1=str[1]; temp2=str[2]; temp3=str[3];
		thousands=toInt(temp0); hundreds=toInt(temp1); tens=toInt(temp2); ones=toInt(temp3);
		hundreds *= 100;
		tens *= 10;
		if(thousands==0) return displayHundreds(hundreds + tens + ones);
		switch(hundreds){
			case 0: return m_numbers[thousands] + " Thousand " + displayTens(tens + ones);
			default: 
				switch(tens){
					case 0: return m_numbers[thousands] + " Thousand " + displayHundreds(hundreds) + " " + displayOnes(ones);
					default:
						switch(ones){
							case 0:return m_numbers[thousands] + " Thousand " + displayHundreds(hundreds) + displayTens(tens);
						}
				}
		}
		return m_numbers[thousands] + " Thousand " + displayHundreds(hundreds + tens + ones);
	}
	//str.length() >= 5
	return str;
}

//displays the word representation of a given number
string NumberConverter::display(const int& num){
	string str=to_string(num);
	if(str.length()==1) return displayOnes(num);
	if(str.length()==2) return displayTens(num);
	if(str.length()==3) return displayHundreds(num);
	if(str.length()==4) return displayThousands(num);
	return str;
}


//Counts number of letters in word representation of a given number
int NumberConverter::count(const int& num){
	return removeWhitespace(display(num)).length();
}

//Counts numbers of letters in wofd representation of all numbers an a range (from lower to upper inclusive)
long NumberConverter::countRange(const int& lower, const int& upper){
	long total = 0;
	for(int i = lower; i <= upper; ++i){
		total+=count(i);
	}
	return total;
}

string NumberConverter::removeWhitespace(string str){
	string ret;
	for(int i = 0; i < str.length(); ++i){
		if(str[i] != ' ') ret+= str[i];
	}
	return ret;
}
