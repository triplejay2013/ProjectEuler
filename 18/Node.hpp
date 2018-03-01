//===================================================================
// Name:		Node.hpp
// Author:		Justin Johnson
// Version:		1.0
// Copyright:	
// Description:	Binary Search Tree practice
//===================================================================
#ifndef _NODE_HPP_
#define _NODE_HPP_
#include <iostream>

using namespace std;

struct Node
{
	Node(int data = 0)
	:	m_data(data),
		m_pRight(0),
		m_pLeft(0)
	{
		//empty
	}

	int m_data;
	Node* m_pRight;
	Node* m_pLeft;
};
#endif
