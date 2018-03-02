//https://www.mathblog.dk/project-euler-18/` for referenc

#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

const string EXAMPLE="./example.txt";
const string NUMS="./numPyramid.txt";
int rows;
int** pyramid;

int getRows(string file){
	string temp;
	int sum = 0;
	ifstream ff(file);
	while(getline(ff,temp)){
		++sum;
	}
	ff.close();
	return sum;
}

int** load(string file){
	cout << "Loading " << file << endl;
	ifstream ff(file);
	rows = getRows(file);
	int temp;
	pyramid = new int*[rows];
	for(int i = 0; i < rows; ++i){
		//creates the actual triangle
		pyramid[i] = new int[rows];
		for(int j = 0; j < i + 1; ++j){
			ff >> temp;
			pyramid[i][j] = temp;
		}
		//fills in row with necessary amount of zeros
		for(int j = rows-1; j > i; --j){
			pyramid[i][j] = 0;
		}
	}

	ff.close();
	return pyramid;
}

void print(){
	for(int i = 0; i < rows; ++i){
		for(int j = 0; j < rows; ++j){
			if(to_string(pyramid[i][j]).length()==1){
				cout << "     " << pyramid[i][j];
			}
			else if(to_string(pyramid[i][j]).length()==2){
				cout << "    " << pyramid[i][j];
			}
			else if(to_string(pyramid[i][j]).length()==3){
				cout << "   " << pyramid[i][j];
			}
			else{
				cout << "  " << pyramid[i][j];
			}
		}
		cout << endl;
	}
}

//3000
//7400
//2460
//8593
int refactorPyramid(){
	int temp;
	//start at second to last row, create current row by adding current to max of next row
	for(int i = rows-2; i >= 0; --i){
		for(int j = 0; j < rows; ++j){
			if(pyramid[i][j] != 0){
				temp = pyramid[i][j] + max(pyramid[i+1][j], pyramid[i+1][j+1]);
				pyramid[i][j] = temp;
			}
		}
	}
	return pyramid[0][0];
}

int main(){
	//load(EXAMPLE);
	load(NUMS);
	print();
	cout << refactorPyramid() << endl;
	print();

	return 0;
}
