class Solution(object):

    def minSteps(self, n):
        memo = {}

        def helper(k):
            if k == 1:
                return 0
            if k in memo:
                return memo[k]
            min_ops = k  
            for i in range(2, int(k**0.5) + 1):
                if k % i == 0:
                    ops = helper(k // i) + i
                    min_ops = min(min_ops, ops)

            memo[k] = min_ops
            return min_ops

        return helper(n)