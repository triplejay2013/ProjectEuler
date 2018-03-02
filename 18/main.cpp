#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const string EXAMPLE="./example.txt";
const string NUM_PYRAMID="./numPyramid.txt";
vector<vector<int>> pyramid;
vector<int> total;
int rows;
//cols == rows

int sum(){
	int sum = 0;
	for(int i = 0; i < total.size(); ++i){
		sum += total[i];
	}
	return sum;
}

//0003
//0074
//0246
//8593
void maxRouteSum(){
	//save the first row value...top of the pyramid
	total.push_back(pyramid[0][rows-1]);
	int j = rows-1;
	//skip first row
	for(int i = 1; i < rows; ++i){
		if(pyramid[i][j-1] > pyramid[i][j]){
			total.push_back(pyramid[i][j-1]);
			//move cols left one
			j-=1;
		}
		else{
			//straight down
			total.push_back(pyramid[i][j]);
		}
	}
	for(int i = 0; i < total.size(); ++i){
		cout << total[i] << ", ";
	}
	cout << endl;
}

void print(){
	for(int i = 0; i < rows; ++i){
		for(int j = 0; j < rows; ++j){
			if(to_string(pyramid[i][j]).length()==1){
				cout << "    " << pyramid[i][j];
			}
			else if(to_string(pyramid[i][j]).length()==2){
				cout << "   " << pyramid[i][j];
			}
			else{
				cout << "  " << pyramid[i][j];
			}
		}
		cout << endl;
	}
}

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

void load(string file) {
	cout << "Loading " << file << endl;
	ifstream ff(file);
	int temp;
	rows = getRows(file);
	for(int i = 0; i < rows; ++i){
		vector<int> vec;
		//fills in row with necessary amount of zeros
		for(int j = rows-1; j > i; --j){
			vec.push_back(0);
		}
		//creates the actual triangle
		for(int j = 0; j < i + 1; ++j){
			ff >> temp;
			vec.push_back(temp);
		}
		pyramid.push_back(vec);
	}

	ff.close();
}

int main(){
	//load(EXAMPLE);
	load(NUM_PYRAMID);
	print();
	maxRouteSum();
	cout << sum() << endl;
	return 0;
}
