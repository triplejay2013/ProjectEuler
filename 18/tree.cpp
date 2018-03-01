#include "tree.hpp"

Tree::Tree()
:	m_pRoot(NULL)
{/*empty*/}

~Tree:Tree(){destroySubTree(m_pRoot);}

//Deconstructs tree from left to right
void Tree::destroySubTree(Node* tree){
	if(!tree){return;}
	destroySubTree(tree->m_pLeft);
	destroySubTree(tree->m_pRight);
	delete tree;
}

/*
	adds a node to the tree from left to right
	1
   2 3
  4 5 6
*/
bool Tree::insert(int num){
	bool ret = insert_helper(m_pRoot, num);
	//the rows is equal to the height of the tree
	int temp = height(m_pRoot);

	//if the height doesn't match the row count
	//a new level was added and maxColumn should increase by one
	if(temp != rows){
		rows = temp;
		++maxColumns;
	}
	return ret;
}

bool Tree::insert_helper(Node*& pCurrent, int val){
	//if pCurrent has no value create new node and insert
	//if(cols == 0)
	if(pCurrent == NULL){
		pCurrent = new Node(val);
		//value was inserted, return true
		return true;
	} 
	else{
		//if within bounds
		if(currentColumn <= maxColumn){
			//and if the current node's  has a value
			if(pCurrent->m_pLeft){
				//then move to next node in column
				insert_helper(pCurrent, val);
			}
		}
		return false;
	}
}

int Tree::height(Node*& pCurrent){
	if(!pCurrent){return 0;}
	int left = height(pCurrent->m_pLeft);
	int right = height(pCurrent->m_pRight);
	return std::max(left, right) + 1;
}
