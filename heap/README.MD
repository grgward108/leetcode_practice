215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

#Solution

This uses heap. let us review heap
The heap is a tree data structure where each node is smaller than or equal to its children if its a min heap, or greater than or equal to its children if its a max heap. 

root is the greatest element. 
We have 5 main operations in a binary heap:
1. Insert
2. get min/max
3. Extract min/max
4. Update
5. Build