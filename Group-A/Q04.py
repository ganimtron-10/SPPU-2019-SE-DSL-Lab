"""
Aledutron
SPPU 2019 SE DSL Lab
SPPU Computer Engineering Second Year (SE) Data Structure Lab (DSL) / Fundamentals of Data Structures (FDS) Assignments (2019 Pattern)
Youtube DSL / FDS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&si=u12IYwo93Z7RU4e8

Problem Statement:
Group-A\Q04.py
Write a Python program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for withdraw and deposit) D means deposit while W means withdrawal.Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

Explaination Video Link: https://www.youtube.com/watch?v=zvQUya4KT-I&list=PLlShVH4JA0osUGQB95eJ8h5bTTzJO89vz&index=6&pp=iAQB
"""


bank_balance = 0


def deposit(amt):
    global bank_balance
    bank_balance += amt


def withdraw(amt):
    global bank_balance
    if bank_balance >= amt:
        bank_balance -= amt
    else:
        print("Not Enough Bank Balance!!")


trans_log = input("Enter the Transaction log: ")

# entry_list = []
# entry = ""

# for char in trans_log:
#     if char == ",":
#         entry_list.append(entry)
#         entry = ""
#         continue

#     entry += char

# entry_list.append(entry)

entry_list = trans_log.split(", ")

for entry in entry_list:
    sep_entry_list = entry.split(" ")
    op = sep_entry_list[0]
    amt = int(sep_entry_list[1])

    if op == "D":
        deposit(amt)
    if op == "W":
        withdraw(amt)

print("Current Bank Balance =", bank_balance)
