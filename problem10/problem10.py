class Solution(object):
    def maxOperations(self, nums, k):
        end = 0

        d = defaultdict(int) 
        for i in nums: 
            d[i] += 1

        for count in d:
            key = k- count
            if key in d:
                if key == count:
                    end += d[key]//2
                else:
                    occurences = min(d[key], d[count])
                    end += occurences
                    d[key] -= occurences
                    d[count] -= occurences

        return end