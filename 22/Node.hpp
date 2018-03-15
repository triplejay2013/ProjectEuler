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
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

struct Node
{
	Node(string data = "")
	:	m_data(data),
		m_pRight(NULL),
		m_pLeft(NULL)
	{
		//empty
	}

	string m_data;
	Node* m_pRight;
	Node* m_pLeft;
};
#endif
