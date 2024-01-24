class Solution(object):
    def checkIfExist(self, arr):
        ans = []
        for i in range(len(arr)):
            if arr[i] * 2 in ans:
                return True
            elif arr[i] % 2 == 0 and arr[i] / 2 in ans:
                return True
            else:
                ans.append(arr[i])
        return False
        """
        :type arr: List[int]
        :rtype: bool
        """