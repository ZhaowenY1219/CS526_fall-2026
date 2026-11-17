================================================================================
README.md - Problem 1
================================================================================

--------------------------------------------------------------------------------
 Introduction 
--------------------------------------------------------------------------------
This program implements a custom Min-Priority Queue to merge multiple sorted sales logs from different checkout registers into a single list. Each register's sales log is already sorted in increasing order and may be empty.The final result is a list of (time, register) pairs sorted by sale time. When two sales have the same time, the sale from the register with the smaller number comes first.

--------------------------------------------------------------------------------
 Algorithm
--------------------------------------------------------------------------------

step 1: read the input and intialize the data
--------------------------------------------------------------------------------
1. read the sales logs frome standard input, with one register's log per line
2. assign register numbers starting from 1 according  to the order in wich the logs appear
3. store each register's sales times in its original order. each log is already sorted in increasing order and may be empty
4. initialize a position index for each register to track the next sale to be processed
5. initialize an empty result list to store the merged(time, register)pairs

step 2: implement a custom Min - Priority Queue
--------------------------------------------------------------------------------
The priority queue must follow these ordering rules:
1. an entry with a smaller sale time has higher priority
2. if two entries have the same sale time, the entry with the smaller register number has higher priority

The priority queue provides two main operations:
1. insert(entry): add a new entry and restore the heap order by bubbling up
2. remove_min(): remove and return the highest - priorty entry, then restore the heap order by bubbling down

step 3: initialize the priority Queue
--------------------------------------------------------------------------------
1. examine each register's sales log
2. if a register's log is empty, skip it
3. otherwise, insert its first sale into the priority queue as( time, register)
4. set the register's position index to indicate that its first sale has been processed into the queue

only the first unprocessed sale from each non - empty register is inserted

therefore, the priority queue never contains more than one entry from the same register and never holds more than k entries

step 4: merge the sales logs
--------------------------------------------------------------------------------
while the priority queue is not empty:
1. remove the highest - priority entry (time, register) from the priority queue
2. append this pair to result list
3. move to the next sale in the corresponding register's log by advancing its position index
4. if another sale is avaiable in that register, insert the next entry (next_time, register) into the priority queue
5. if the register has no remaining sales, do not insert another entry for it
6. repeat this process until the priority queue becomes empty

Since each register's log is already sorted, inserting only its next unprocessed sale ensures that its sales are processed in their original increasing order.The priority queue always selects the smallest available sale time. when two sales have the time, the smaller register number is selected first.

step 5: return the merged result
--------------------------------------------------------------------------------
1. continue removing entries from the priority queue and adding the next available sale from the corresponding register until all sales have been processed
2. when the priority queue becomes empty, all register logs have been merged
3. return the result list containing all (time, register) pairs in increasing order of sale time, with ties resoveld by register number

--------------------------------------------------------------------------------
Interesting aspects
--------------------------------------------------------------------------------
1.The priority queue is implemented using a binary min-heap, with insertion handled by bubbling up and removal handled by bubbling down.

2.The queue just contains the initial unprocessed sale from each non-empty register. If a sale from the same register is available, it is entered after it has been withdrawn. As a result, the priority queue never carries more than k entries and never has more than one item from the same register.

--------------------------------------------------------------------------------
How to run
--------------------------------------------------------------------------------

python3 HW6/problem1/problem1.py < HW6/problem1/problem1Resource/merge_input1.txt
python3 HW6/problem1/problem1.py < HW6/problem1/problem1Resource/merge_input2.txt
python3 HW6/problem1/problem1.py < HW6/problem1/problem1Resource/merge_input3.txt
python3 HW6/problem1/problem1.py < HW6/problem1/problem1Resource/merge_input4.txt
python3 HW6/problem1/problem1.py < HW6/problem1/problem1Resource/merge_input5.txt
python3 HW6/problem1/problem1.py < HW6/problem1/problem1Resource/merge_input6.txt
python3 HW6/problem1/problem1.py < HW6/problem1/problem1Resource/merge_input7.txt
python3 HW6/problem1/problem1.py < HW6/problem1/problem1Resource/merge_input9.txt





