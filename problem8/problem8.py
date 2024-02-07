class Solution(object):
    def maxVowels(self, s, k):
        # Initialize pointers and variables
        left = 0
        right = 0
        vowels = set(["a", "i", "u", "e", "o"])  # Using a set for faster lookup
        maxVowels = 0
        currentVowels = 0

        while right < len(s):
            if s[right] in vowels:
                currentVowels += 1
            
            if right - left + 1 > k:
                if s[left] in vowels:
                    currentVowels -= 1
                left += 1

            maxVowels = max(maxVowels, currentVowels)

            right += 1

        return maxVowels
