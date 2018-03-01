#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const string EXAMPLE="./example.txt";
const string NUM_PYRAMID="./numPyramid.txt";
vector<vector<int>> pyramid;
int rows = -1;//offset to make it work

int maxRouteSum(){
	//first value at top of pyramid
	int current = pyramid[0][0], sum = 0, max = 0;
	for(int i = 1; i < rows; ++i){//skip the first one
		for(int j = 0; j < i+1; ++j){
			if(pyramid[i][j]){

			}
		}
	}
}

void print(){
	for(int i = 0; i < rows; ++i){
		for(int j = 0; j < i+1; ++j){
			cout << pyramid[i][j];
		}
		cout << endl;
	}
}

void load(string file) {
	cout << "Loading " << file << endl;
	ifstream ff(file);
	int temp;

	for(int counter = 1; !ff.eof(); ++counter){
		vector<int> tempVec;
		for(int j = 1; j < counter+1; ++j){
			ff >> temp;
			if(ff.eof()) break;
			tempVec.push_back(temp);
			rows = counter;//the final value of counter (the rows)
		}
		pyramid.push_back(tempVec);
	}
}

int main(){
	load(EXAMPLE);
	print();
	return 0;
}
