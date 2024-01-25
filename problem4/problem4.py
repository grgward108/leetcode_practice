class Solution(object):
    def kthFactor(self, n, k):

        hash = []
        for i in range(1, n+1):
            if n % i == 0:
                hash.append(i)

        m = len(hash) 
        if k > m:
            return -1
        else:
            return hash[k-1]