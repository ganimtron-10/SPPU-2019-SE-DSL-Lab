/*
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-E\Q29.cpp
Queues are frequently used in computer programming, and a typical example is the creation of a job queue by an operating system. If the operating system does not use priorities, then the jobs are processed in the order they enter the system. Write C++ program for simulating job queue. Write functions to add job and delete job from queue.

Explaination Video Link: https://www.youtube.com/watch?v=ECUwcDhSDOc&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=14&pp=iAQB
*/

#include <iostream>
using namespace std;

class Queue
{
public:
    const static int size = 10;
    int start = -1;
    int end = -1;
    int array[size];

    void push(int x)
    {
        if (end == size - 1)
        {
            cout << "Queue Overflow!!" << endl;
        }

        array[++end] = x;
    }

    int pop()
    {
        if (start == end)
        {
            cout << "Queue Underflow!!" << endl;
            return -1;
        }

        return array[++start];
    }

    void display()
    {

        if (start == end)
        {
            cout << "Queue is empty!!";
        }

        cout << "Queue contains:";
        for (int i = start + 1; i <= end; i++)
        {
            cout << array[i] << " ";
        }
        cout << endl;
    }
};

void add_job(Queue &q, int job)
{
    q.push(job);
}

void delete_job(Queue &q)
{
    q.pop();
}

int main()
{
    Queue job_line;
    add_job(job_line, 1);
    add_job(job_line, 10);
    add_job(job_line, 100);
    add_job(job_line, 1000);

    job_line.display();

    delete_job(job_line);
    delete_job(job_line);

    job_line.display();
}