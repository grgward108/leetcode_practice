1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


%solution
Just use Sliding Window. i think the catch is how to iterate it, you need a current variable and a global maximum variable holder. 