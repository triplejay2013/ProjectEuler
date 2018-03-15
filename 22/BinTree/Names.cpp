//===================================================================
// Name:		Names.cpp
// Author:		Justin Johnson
// Version:		1.0
// Copyright:	
// Description:	Loads a list of names alphabeticallyh into BST
//===================================================================
#include "Names.hpp"

//===================================================================
// Default constructor - Loads initial dictionary
//===================================================================
Names::Names()
{
	ifstream dictionary("names.txt");
	if(!dictionary){
		cerr << "Error opening file\n";
		exit(1);
	}
	int counter = 0;
	string line;
	while(dictionary.good()){
		getline(dictionary, line, ',');//read csv file
		v_dictionary.insert(v_dictionary.begin() + counter, line.substr(1,line.length()-2));
		++counter;
	}
	//for efficiency the vector is randomized and put into BST
	random_shuffle(v_dictionary.begin(), v_dictionary.end());
	for(int i = 0; i < v_dictionary.size(); ++i){
		t_dictionary.insert(v_dictionary[i]);
	}
	dictionary.close();
}

//===================================================================
// prints List of Names
//===================================================================
void Names::print() {
	t_dictionary.display();
}

string Names::current(){
	return t_dictionary.current();
}

bool Names::hasNext(){
	return t_dictionary.hasNext();
}

bool Names::next(){
	return t_dictionary.next();
}

bool Names::inList(string name){
	return t_dictionary.search(name);
}
