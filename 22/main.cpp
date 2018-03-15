#include <iostream>
#include <ctime>
#include <fstream>
#include <list>
#include <string>
#include "./BigInt/BigInteger.hpp"

/*
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53
= 49714.

What is the total of all the name scores in the file?
*/

using namespace std;

list<string> names;

void print(const int& position){
	int counter = 1;
	for(string i : names){
		if(counter == position){ cout << counter << ": " << i << endl; return;}
	}
}

string getName(int position){
	int counter = 1;
	for(string i : names){
		if(counter == position) return i;
		++counter;
	}
	return "NONE";
}

long nameScore(int location){
	int sum = 0;
	string name = getName(location);
	for(int j = 0; j < name.length(); ++j){
		switch(name[j]){
			case 'A': sum += 1; break; case 'B': sum += 2; break; case 'C': sum += 3; break; case 'D': sum += 4; break; case 'E': sum += 5; break;
			case 'F': sum += 6; break; case 'G': sum += 7; break; case 'H': sum += 8; break; case 'I': sum += 9; break; case 'J': sum += 10; break;
			case 'K': sum += 11; break; case 'L': sum += 12; break; case 'M': sum += 13; break; case 'N': sum += 14; break; case 'O': sum += 15; break;
			case 'P': sum += 16; break; case 'Q': sum += 17; break; case 'R': sum += 18; break; case 'S': sum += 19; break; case 'T': sum += 20; break;
			case 'U': sum += 21; break; case 'V': sum += 22; break; case 'W': sum += 23; break; case 'X': sum += 24; break; case 'Y': sum += 25; break;
			case 'Z': sum += 26; break; default: sum+=0;
		}
	}
	return location * sum;
}

void load(){
	ifstream ff("names.txt");
	string temp;
	while(ff.good()){
		getline(ff,temp,',');
		names.push_back(temp.substr(1,temp.length()-2));
	}
	names.sort();
	ff.close();
}

int main(){
	clock_t start;
	double duration;
	start = clock();

	cout << "Starting up Program\n";
	int position = 938;
	load();
	long long scoreSum = 0; 
	int counter = 1;
	for(string i : names){
		cout << counter << ": " << i << " has a score of " << nameScore(counter) << "\t\t";
		if(counter%4 == 0) cout << endl;
		scoreSum += nameScore(counter);
		++counter;
	}
	cout << endl;

	cout << "Total name score of the list is " << scoreSum << endl;
	duration = (clock() - start) / (double) CLOCKS_PER_SEC;
	cout << "The process took " << duration << " seconds\n";
	cout << endl;

	print(position);
	long score = nameScore(position);
	cout << "The score of " << getName(position);
	printf(" at position %d is %lu\n", position, score);

	return 0;
}
