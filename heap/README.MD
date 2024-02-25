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

heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

heapq.heappushpop(heap, item)¶
Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

heapq.heapify(x)
Transform list x into a heap, in-place, in linear time.