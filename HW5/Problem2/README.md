================================================================================
README.md - Problem 2: Morse Code
================================================================================

--------------------------------------------------------------------------------
 Introduction 
--------------------------------------------------------------------------------



--------------------------------------------------------------------------------
 Algorithm
--------------------------------------------------------------------------------

Step 1 create a status table
--------------------------------------------------------------------------------

Create a state table containing three rows and n columns, where n is the length of the input string. Each column represents a position (offset), with positions numbered starting from 0.

The three rows represent the possible vowel lengths:

Row 1: vowels with 1 symbol E;
Row 2: vowels with 2 symbols A, I;
Row 3: vowels with 3 symbols O,U

'offset':  the starting position of the current vowel in the original Morse code string

'len': length of morse code symbols currently used for vowels

'M[len][offset]' :the number of possible decoding sequences obtained by first fully decoding the portion of the string from the beginning up to the current offset into vowels, and then appending a valid vowel sequence of length `len` starting from the current position.

'P(offset)': the total number of ways in which all symbols from the beginning of the input string up to the current offset can be fully decoded into vowels


Step2 set base case
--------------------------------------------------------------------------------

Set Initial Conditions: P(0) = 1

When the offset is 0, it represents an empty string. One way to decode an empty string is to not add any characters.


Step3 The Recurrence Relation
--------------------------------------------------------------------------------

Starting at offset 0, recurrence relation:

P(offset) = M[1][offset - 1]+ M[2][offset - 2] + M[3][offset - 3]

'M[1][offset - 1]': the number of decoding operations required for the last vowel, which occupies 1 symbol(E)

'M[2][offset - 2]': the number of decoding operations required for the last vowel, which occupies 2 symbols(A,I)

'M[3][offset - 3]': the number of decoding operations required for the last vowel, which occupies 3 symbols(O,U)


Step4 Check the length  and Fill the status table
--------------------------------------------------------------------------------

case 1: check the next 1 symbol 

 If the current symbol is a '.' ： M[1][offset] = P(offset),
 otherwise,  M[1][offset] = 0

case 2: check the next 2 symbols

 If the current two symbols is are '.-' or '..': M[2][offset] = P(offset)
 otherwise,  M[2][offset] = 0
 
case 3: check the next 3 symbols

 If the current two symbols is are '---' or '..-': M[3][offset] = P(offset)
 otherwise,  M[3][offset] = 0

Step5 Calculate the final answer
--------------------------------------------------------------------------------

Calculate the total number of vowel decodings in the entire morse code 

P(n) = M[1][n-1] + M[2][n-2] +M[3][n-3]

‘n’ represents the total length of the original input string

--------------------------------------------------------------------------------
 Interesting aspects
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
 How to run
--------------------------------------------------------------------------------

python3 problem2.py 1 < Problem2Resource/vowel_input1.txt
python3 problem2.py 2 < Problem2Resource/vowel_input2.txt
python3 problem2.py 3 < Problem2Resource/vowel_input3.txt
python3 problem2.py 4 < Problem2Resource/vowel_input4.txt




