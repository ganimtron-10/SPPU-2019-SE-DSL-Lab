/*
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-C\Q19.cpp
Department of Computer Engineering has student's club named 'Pinnacle Club'. Students of second, third and final year of department can be granted membership on request. Similarly one may cancel the membership of club. First node is reserved for president of club and last node is reserved for secretary of club. Write C++ program to
maintain club member‘s information using singly linked list. Store student PRN and Name. Write functions to:
a) Add and delete the members as well as president or even
secretary.
b) Compute total number of members of club
c) Display members
d) Two linked lists exists for two divisions. Concatenate two lists.

Explaination Video Link: https://www.youtube.com/watch?v=BCRvaGOenUs&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=17&pp=iAQB
*/

#include <iostream>
using namespace std;

class Node
{
public:
	string prn;
	string name;
	Node *next;

	Node(string gprn, string gname)
	{
		prn = gprn;
		name = gname;
		next = NULL;
	}
};

Node *h1 = NULL;
Node *h2 = NULL;

Node *addPresident(Node *head, string prn, string name)
{
	Node *gNode = new Node(prn, name);
	if (head == NULL)
	{
		head = gNode;
		return head;
	}

	gNode->next = head;
	head = gNode;
	return head;
}

Node *addMember(Node *head, string prn, string name)
{
	Node *gNode = new Node(prn, name);
	if (head == NULL)
	{
		cout << "President must be added before members.";
		return head;
	}

	Node *president = head;
	gNode->next = president->next;
	president->next = gNode;
	return head;
}

Node *addSecretary(Node *head, string prn, string name)
{
	Node *gNode = new Node(prn, name);
	if (head == NULL)
	{
		cout << "President must be added before secretary.";
		return head;
	}

	Node *cur = head;
	while (cur->next != NULL)
	{
		cur = cur->next;
	}
	cur->next = gNode;
	return head;
}

Node *deletePresident(Node *head)
{
	if (head == NULL)
	{
		cout << "President doesnot exists." << endl;
		return head;
	}
	Node *dNode = head;
	head = head->next;
	delete (dNode);
	return head;
}

Node *deleteMember(Node *head, string prn)
{
	if (head == NULL || head->next == NULL || head->next->next == NULL)
	{
		cout << "Member doesn't exists." << endl;
		return head;
	}

	Node *cur = head->next;
	Node *prev = head;
	while (cur != NULL and cur->prn != prn)
	{
		prev = cur;
		cur = cur->next;
	}

	if (cur == NULL)
	{
		cout << "Given Member doesn't exist in the club." << endl;
		return head;
	}
	else
	{
		prev->next = cur->next;
		delete (cur);
		return head;
	}
}

Node *deleteSecretary(Node *head)
{
	if (head == NULL || head->next == NULL)
	{
		cout << "Secretary doesnot exists." << endl;
		return head;
	}

	Node *cur = head, *prev = NULL;
	while (cur->next != NULL)
	{
		prev = cur;
		cur = cur->next;
	}
	prev->next = NULL;
	delete (cur);
	return head;
}

Node *merge(Node *h1, Node *h2)
{
	if (h1 == NULL)
		return h2;
	if (h2 == NULL)
		return h1;

	Node *cur = h1;
	while (cur->next != NULL)
	{
		cur = cur->next;
	}

	cur->next = h2;

	return h1;
}

void displayLL(Node *head)
{
	cout << "Printing LL" << endl;
	Node *cur = head;
	while (cur != NULL)
	{
		cout << cur->prn << " " << cur->name << endl;
		cur = cur->next;
	}
}

void countLL(Node *head)
{
	// cout << "Counting LL" << endl;
	Node *cur = head;
	int cnt = 0;
	while (cur != NULL)
	{
		cnt++;
		cur = cur->next;
	}
	cout << "Total Cnt = " << cnt << endl;
	if (cnt - 2 < 1)
	{
		cout << "No member exists." << endl;
	}
	else
	{
		cout << "Member Cnt = " << cnt - 2 << endl;
	}
}

int main()
{

	h1 = addPresident(h1, "1", "abc");
	h1 = addMember(h1, "11", "def");
	h1 = addMember(h1, "111", "hjs");
	h1 = addSecretary(h1, "21", "yt");
	displayLL(h1);
	countLL(h1);

	h1 = deleteMember(h1, "111");

	displayLL(h1);
	countLL(h1);
}