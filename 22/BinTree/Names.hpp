//===================================================================
// Name:		Names.hpp
// Author:		Justin Johnson
// Version:		1.0
// Copyright:	
// Description:	Header File
//===================================================================
#ifndef _NAMES_HPP_
#define _NAMES_HPP_

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

class Names{
public:
	Names();//default constructor
	void print();//prints out list of names
	bool inList(string name);
	bool hasNext();
	string current();
	bool next();
private:
	vector<string> v_dictionary;//on program startup loads dictionary into a vector
};
#endif //_NAMES_HPP_
