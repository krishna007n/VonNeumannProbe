# Number-pattern
Simple program to print the sequence: 1,2,3,3,4,4,4,4.....
------------------------------------------------------------------------------------------
The initial step to build a Von Neumann Probe. But the above program is a sequential way to produce the pattern.

Initially, the array contains one root element(which is 1). 

Creation of next element:
  Selecting the maximum value from the array
  Setting it as the 'c' value.
  Adding the 'c' value to the distinct elements. When a new element occurs 'c' value decreases by one.
  Appending the values created into the array

eg: if array is [1,2]. The maximum value is 2. Then new values generated will be, 1+2 and 2+1. New values will get appended. Then array will be [1,2,3,3].

The number of elements will follow the function: 2^n

Basic logic: 
  1's first child will be 2(by adding 1) 
  1's second child will be 3(by adding 2), and 2's first child will be 3(by adding 1) 
  1's third child will be 4(by adding 3), 2's new child: 4(+2), 3's new child: 4(+1)
  .................................................................................

If we can implement parallel processing and some changes are made. All elements will produce the next child(One copy which is mutated by incrementing value) simultaneously like a virus spread.
