================================================================================
README.md - Problem 1
================================================================================


--------------------------------------------------------------------------------
1. Introduction 
--------------------------------------------------------------------------------




--------------------------------------------------------------------------------
algorithm
--------------------------------------------------------------------------------

step 1: read the input and intialize the data

1. read the sales logs frome standard input, with one register's log per line
2. assign register numbers starting from 1 according  to the order in wich the logs appear
3. store each register's sales times in its original order. each log is already sorted in increasing order and may be empty
4. initialize a position index for each register to track the next sale to be processed
5. initialize an empty result list to store the merged(time, register)pairs

step 2: implement a custom Min - Priority Queue

The priority queue must follow these ordering rules:
1. an entry with a smaller sale time has higher priority
2. if two entries have the same sale time, the entry with the smaller register number has higher priority

The priority queue provides two main operations:
1. insert(entry): add a new entry and restore the heap order by bubbling up
2. remove_min(): remove and return the highest - priorty entry, then restore the heap order by bubbling down
3. 
