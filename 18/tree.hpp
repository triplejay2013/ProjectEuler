#ifndef _TREE_HPP_
#define _TREE_HPP_

#include <iostream>
#include "Node.hpp"

using namespace std;

class Tree{
public:
	Tree();
	~Tree();

	bool insert(int num);
	bool remove(int num, int row);
	bool delete(int num);
	int height(Node*& pCurrent);

private:
	int m_leafNodes;//number of leaf nodes
	Node* m_pRoot;//root of the tree
	int m_nodes;//number of nodes in the tree
	int m_rows;//the height
	//index starts at 1 (NOT ZERO)
	int currentColumn = 1;//increases by one per row
	int maxColumn = 0;//max width for a given level in the tree
	/*
				currentColumn	maxColumn	
								0
					1       ----1 //goes to one after first insertion
	rows:		   1 2		----2
				  1 2 3		----3
				 1 2 3 4	----4
	*/

	//Class Methods
	void destroySubTree(Node* tree){

	//helpers
	void insert_helper(Node*& pCurrent, int val);
	Node* remove_helper(Node*& pCurrent, int val);
};

#endif
