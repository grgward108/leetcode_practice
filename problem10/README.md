1679. Max Number of K-Sum Pairs


You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.


#Solution

using defaultdict(int) was good on my part. however i missed out on using the minimum, as i tried to decrement it one by one

i think this is one of my weaknesses in programming, i still have a hardtime of trying to think like a computer . like the using of the minimal thing. i assumed that if d[num] has already been used then it shouldnt be iterated again, but then i realized that because we use min, the iteration wont even matter. 