/*
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-D\Q25.cpp
A palindrome is a string of character that‘s the same forward and backward. Typically, punctuation, capitalization, and spaces are ignored. For example, “Poor Dan is in a droop” is a palindrome, as can be seen by examining the characters “poor danisina droop” and observing that they are the same forward and backward. One way to check for a palindrome is to reverse the characters in the string and then compare with them the original-in a palindrome, the sequence will be identical. Write C++ program with functions☻
a) To print original string followed by reversed string using stack
b) To check whether given string is palindrome or not

Explaination Video Link: https://www.youtube.com/watch?v=8EvsaNWmtqA&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=12&pp=iAQB
*/

#include <iostream>
using namespace std;

class Stack
{
public:
    const static int size = 100;
    int top = -1;
    char array[size];

    void push(char x)
    {
        if (top == size - 1)
        {
            cout << "Stack Overflow!!";
            return;
        }

        array[++top] = x;
    }

    char pop()
    {
        if (top == -1)
        {
            cout << "Stack Underflow!!";
            return -1;
        }

        return array[top--];
    }

    void display()
    {
        if (top == -1)
        {
            cout << "Stack is Empty";
        }

        cout << "Stack contains: ";
        for (int i = 0; i <= top; i++)
        {
            cout << array[i] << " ";
        }
        cout << endl;
    }
};

int main()
{

    Stack s;

    string user_input;

    cout << "Enter a string: ";
    getline(cin, user_input);

    string org_str = "";

    for (int i = 0; i < user_input.size(); i++)
    {

        char ch = user_input[i];

        if (ch >= 'a' and ch <= 'z')
        {
            ch = (char)(ch - 'a' + 'A');
        }
        if (ch >= 'A' and ch <= 'Z')
        {
            s.push(ch);
            org_str.push_back(ch);
        }
    }

    // s.display();

    cout << "Original string: " << org_str << endl;

    string rev_str = "";
    while (s.top != -1)
    {
        rev_str.push_back(s.pop());
    }
    cout << "Reversed string: " << rev_str << endl;

    bool is_palindrome = true;
    for (int i = 0; i < org_str.size(); i++)
    {
        if (org_str[i] != rev_str[i])
        {
            is_palindrome = false;
            break;
        }
    }

    cout << user_input << " is " << (is_palindrome ? "" : "not ") << "a palindrome.";
}
