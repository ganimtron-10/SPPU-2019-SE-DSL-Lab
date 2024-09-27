/*
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-E\Q32.cpp
Pizza parlor accepting maximum M orders. Orders are served in first come first served basis. Order once placed cannot be cancelled. Write C++ program to simulate the system using circular queue using array

Explaination Video Link: https://www.youtube.com/watch?v=Fsr_pDr-CMg&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=16&pp=iAQB
*/

#include <iostream>
using namespace std;

class CQueue
{
public:
	const static int m = 5;
	int array[m];
	int front = -1;
	int rear = -1;

	bool isFull()
	{
		// if((front == 0 and rear == m-1) || (rear = front -1)){
		// 	return 1;
		// }
		// return 0;
		return (front == 0 and rear == m - 1) || (rear == front - 1);
	}

	bool isEmpty()
	{
		return (front == -1 and rear == -1);
	}

	void enqueue(int x)
	{
		if (isFull())
		{
			cout << "CQueue Overflow" << endl;
			return;
		}

		if (front == -1)
		{
			front = 0;
			rear = 0;
		}
		else
		{
			if (rear == m - 1)
			{
				rear = 0;
			}
			else
			{
				rear++;
			}

			// rear = (++rear) % m;
		}

		array[rear] = x;
		// cout << "Rear is " << rear << endl;
	}

	void dequeue()
	{
		if (isEmpty())
		{
			cout << "CQueue Underflow" << endl;
			return;
		}

		if (front == rear)
		{
			front = -1;
			rear = -1;
		}
		else
		{
			if (front == m - 1)
			{
				front = 0;
			}
			else
			{
				front++;
			}
		}
	}

	void display()
	{
		if (isEmpty())
		{
			cout << "CQueue Underflow" << endl;
			return;
		}

		cout << "\nCQueue contains: ";

		if (front == rear)
		{
			cout << array[front];
		}
		else if (front < rear)
		{
			for (int i = front; i <= rear; i++)
			{
				cout << array[i] << " ";
			}
		}
		else
		{
			for (int i = front; i < m; i++)
			{
				cout << array[i] << " ";
			}
			for (int i = 0; i <= rear; i++)
			{
				cout << array[i] << " ";
			}
		}
	}
};

int main()
{
	CQueue cq;
	cq.enqueue(10);
	cq.enqueue(12);
	cq.enqueue(16);
	cq.enqueue(28);
	cq.enqueue(1);

	cq.dequeue();
	cq.dequeue();
	cq.dequeue();

	cq.enqueue(89);

	cq.display();
}

//  89     28 1