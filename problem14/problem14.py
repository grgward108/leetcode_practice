class Solution(object):
    def combinationSum3(self, k, n):

        if (k)*(k+1)/2 > n or (18-k)*(k)/2 < n:
            return []
        
        answer = []

        def findsolution(start, current_array, current_sum):
            if len(current_array) == k and current_sum == n:
                answer.append(list(current_array))
                return
            else:
                for i in range(start, 10):
                    if current_sum + i < n:
                        findsolution(i + 1, current_array + [i], current_sum + i)
        
        findsolution(0, [], 0)

        return answer