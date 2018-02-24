//See www.robertdickau.com/lattices.html to understand the solution
#include <iostream>
#include <vector>

using namespace std;

/*
	n is the size of the grid (NxN)
	starting at the bottom right and extending to the upper left,
	this function finds how many paths are located down the center right diagnoal
	Once the algorithm reaches the limit it returns that value, which is the total number of paths
*/
long long findPaths(int size){
	const int gridSize = size;
	//A 5x5 grid actually has 6x6 number of points
	long long grid [gridSize+1][gridSize+1];

	//Initialize the grid with boundaries of 1
	//This only includes the 'right' and 'bottom' edges of the grid
	for(int i = 0; i < gridSize; ++i){
		grid[i][gridSize] = 1;
		grid[gridSize][i] = 1;
	}

	//start at bottom right corner (not the outermost...inset by one), and set values for all the grid points
	//by adding values to the bottom and right of each point
	for(int i = gridSize - 1; i >= 0; --i){
		for(int j = gridSize - 1; j >= 0; --j){
			grid[i][j] = grid[i+1][j] + grid[i][j+1];
		}
	}

	return *grid[0,0];
}

long long getGridPoint(int col, int row,int size){
	const int gridSize = size;
	//A 5x5 grid actually has 6x6 number of points
	long long grid [gridSize+1][gridSize+1];

	//Initialize the grid with boundaries of 1
	//This only includes the 'right' and 'bottom' edges of the grid
	for(int i = 0; i < gridSize; ++i){
		grid[i][gridSize] = 1;
		grid[gridSize][i] = 1;
	}

	//start at bottom right corner (not the outermost...inset by one), and set values for all the grid points
	//by adding values to the bottom and right of each point
	for(int i = gridSize - 1; i >= 0; --i){
		for(int j = gridSize - 1; j >= 0; --j){
			grid[i][j] = grid[i+1][j] + grid[i][j+1];
		}
	}

	return *grid[col,row];
}

//this is unfinished....but whatevs
void printRow(int size, int rowNum){
	//cout << "+";
	cout << getGridPoint(0,rowNum, size);
	for(int i = 0; i < size; ++i){
		//cout << " -- +";
		cout << "-- " << getGridPoint(i,rowNum,size) << " -- ";
	}
	cout << "\n";
}

void printCol(int size){
	cout << "|";
	for(int i = 0; i < size; ++i){
		cout << "    |";
	}
	cout << "\n";
}

void printGrid(int size){
	for(int i = 0; i < size; ++i){
		printRow(size, i);
		printCol(size);
	}
	printRow(size, size);
}

int main(){
	while(true){
		cout << "Input a grid size: ";
		int size;
		cin >> size;
		if(size <= 0) break;
		printf("A %dX%d grid has %llu paths!\n", size, size, findPaths(size));
		printGrid(size);

	}
	
	return 0;
}
