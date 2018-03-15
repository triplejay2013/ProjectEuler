//===================================================================
// Name:		BinaryTree.hpp
// Author:		Justin Johnson
// Version:		1.0
// Copyright:	
// Description:	Binary Search Tree practice
//===================================================================
#ifndef _BINARYTREE_HPP_
#define _BINARYTREE_HPP_
#include <iostream>
#include <string>
#include "Node.hpp"

using namespace std;

class BinaryTree
{
public:
	//Binary Tree Constructor
	BinaryTree()
	:	m_pRoot(NULL), m_current(NULL), m_currentParent(NULL)
	{
		//Empty
	}

	//Binary Tree Deconstructor
	~BinaryTree(){destroySubTree(m_pRoot);}

	//Deconstructs tree from left to right
	void destroySubTree(Node* tree){
		if(!tree){return;}
		destroySubTree(tree->m_pLeft);
		destroySubTree(tree->m_pRight);
		delete tree;
	}

	//Inserts a value into the tree, Does not allow duplicates.
	//If the value is already in tree, false is returned. True Otherwise
	bool insert(string value){
		if(search(value)){return false;	} 
		else {insert_helper(m_pRoot, value);}
		return true;
	}

	//displays BST in order
	void display(){
		if(m_pRoot != NULL){display_helper(m_pRoot);}
	}

	bool hasNext(){
		return m_position <= numberNodes();
	}

	bool next(){
		//first time called
		if(!m_current){
			m_current = m_pRoot;
			//traverse to the bottom left of tree (first index)
			while(m_current->m_pLeft){
				m_currentParent = m_current;
				m_current = m_current->m_pLeft;
			}
			return m_currentParent->m_pLeft || m_currentParent->m_pRight;
		}
		//second+ time called
		else{
			//traverses tree in-order to find m_current, if a left child exists then that child is next
			if(m_current->m_pLeft){
				m_currentParent = m_current;
				m_current = m_current->m_pLeft;
				return true;
			}
			//else if previous is the same as m_current->m_pLeft, the parent is next
			else if(m_currentParent->m_pLeft == m_current){
				m_current = m_currentParent;
				m_currentParent = findParent(m_currentParent->m_data);
				return true;
			}
			//else the right child is next if present
			else if(m_current->m_pRight){
				m_current = m_current->m_pRight;
				return true;
			}
			//branch exhausted return to grandparent ie, both parent, left and right child have been traversed, return to grandparent
			else{
				m_current = m_currentParent->m_pLeft;
				return next();
			}
		}
	}

	Node* findParent(string value) {
		//if parent is the root of the tree;
		if(m_pRoot->m_data == value) return m_pRoot;
		Node* pCurrent = m_pRoot;

		while(pCurrent){
			if(pCurrent->m_pLeft){
				if(pCurrent->m_pLeft->m_data == value) return pCurrent;
			}
			if(pCurrent->m_pRight){
				if(pCurrent->m_pLeft->m_data == value) return pCurrent;
			}
			else if(value < pCurrent->m_data){
				pCurrent = pCurrent->m_pLeft;
			} 
			else{
				pCurrent = pCurrent->m_pRight;
			}
		}
		return NULL;
	}

	//Searchs for a value in the tree
	//returns true if it was found, false if it was not
	bool search(string value) const {
		Node* pCurrent = m_pRoot;

		while(pCurrent){
			if (pCurrent->m_data == value){	
				return true;
			} 
			else if(value < pCurrent->m_data){
				pCurrent = pCurrent->m_pLeft;
			} 
			else{
				pCurrent = pCurrent->m_pRight;
			}
		}
		return false;
	}

	//Deletes a value from the tree
	void remove(string value){
		if(m_pRoot != NULL){Node* tmp = remove_helper(m_pRoot, value);}
	}

	//Returns a Node Count of all Nodes in Tree
	unsigned int numberNodes(){
		m_nodes = 0;
		numberNodes(m_pRoot);
		return m_nodes;
	}

	//returns a count of all leaf nodes in a tree
	unsigned int numberLeafNodes(){
		m_leafNodes = 0;
		numberLeafNodes(m_pRoot);
		return m_leafNodes;
	}

	//returns the height of the tree(level)
	int height(){
		m_height = height(m_pRoot);
		return m_height;
	}

	string current(){
		if(!m_current) return "NONE";
		return m_current->m_data;
	}

private:
	int m_height;//height of the tree
	int m_leafNodes;//number of leaf nodes
	Node* m_pRoot;//root of the tree
	int m_nodes;//number of nodes in the tree
	Node* m_current;//node in focus, most recently used node
	Node* m_currentParent;
	int m_position;//how many nodes have been used

	//recursive call to display all the nodes in the tree
	void display_helper(Node* current){
		if(current != NULL){
			display_helper(current->m_pLeft);
			cout << current->m_data << "\n";
			display_helper(current->m_pRight);
		}
	}

	//recursive call to insert a given node with value (val) into the tree at respective position
	void insert_helper(Node*& pCurrent, string val){
		if(pCurrent == NULL){
			pCurrent = new Node(val);
			return;
		} 
		if (pCurrent->m_data == val){return;}
		else{
			if(val < pCurrent->m_data){insert_helper(pCurrent->m_pLeft, val);} 
			else {insert_helper(pCurrent->m_pRight, val);}
		}
	}

	//recursive call to remove node from the tree
	Node* remove_helper(Node*& pCurrent, string val){
		//checks if null
		if(pCurrent == NULL){return 0;} 
		else {
			//if found
			if(val == pCurrent->m_data){
				makeDeletion(pCurrent);
				return NULL;
				//move left if less than
			} else if (val < pCurrent->m_data){
				pCurrent->m_pLeft = remove_helper(pCurrent->m_pLeft, val);
				return pCurrent;
				//move right if greater than
			} else if (val > pCurrent->m_data){
				pCurrent->m_pRight = remove_helper(pCurrent->m_pRight, val);
				return pCurrent;
			}
		}
	}

	void makeDeletion(Node*& pCurrent){
		Node* toDelete = pCurrent;
		//used to help move pointers around
		Node* attachPoint;
		//if one child
		if (pCurrent->m_pLeft == NULL){pCurrent = pCurrent->m_pRight;} 
		else if (pCurrent->m_pRight == NULL){pCurrent = pCurrent->m_pLeft;}
		//if two children
		else{
			attachPoint = pCurrent->m_pRight;
			//right branch's min
			while (attachPoint->m_pLeft != NULL){attachPoint = attachPoint->m_pLeft;}
			//make attach point attach roots left pointer
			attachPoint->m_pLeft = pCurrent->m_pLeft;
			//attach root to attachPoint
			pCurrent = pCurrent->m_pRight;
		}
		delete toDelete;
	}

	void numberNodes(Node*& pCurrent){
		if(!pCurrent){return;}
		numberNodes(pCurrent->m_pLeft);
		numberNodes(pCurrent->m_pRight);
		m_nodes++;
	}

	void numberLeafNodes(Node*& pCurrent){
		if(!pCurrent){return;}
		numberLeafNodes(pCurrent->m_pLeft);
		numberLeafNodes(pCurrent->m_pRight);
		if(!pCurrent->m_pRight && !pCurrent->m_pLeft){m_leafNodes++;}
	}

	int height(Node*& pCurrent){
		if(!pCurrent){return 0;}
		int left = height(pCurrent->m_pLeft);
		int right = height(pCurrent->m_pRight);
		return std::max(left, right) + 1;
	}
};
#endif
