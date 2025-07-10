'''
30. Substring with Concatenation of All Words
Difficulty: Hard
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. 
"acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
'''
# Solution
from collections import Counter
# words of equal length -> fixed-length window substring search
# each valid string: total_len = len(words) * len(word)
# use frequency map to track occurrences of each word in words
# use sliding window approach optimized for fixed-length words search
# T: O(len(s) * len(words))
# S: O(# of words * word length)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])  # each word is of equal length
        word_count = len(words)  # number of words
        total_len = word_len * word_count  # total length of concatenated words
        word_map = Counter(words)  # frequency map of words

        result = []
    
        # Iterate through each possible starting position for word_len-sized windows
        for i in range(word_len):
            left, right = i, i  # window pointers
            cur_map = Counter()  # track words in the current window
            count = 0  # number of matched words
        
            while right + word_len <= len(s):  # ensure we don't go out of bounds while expanding the window
                word = s[right:right + word_len]  # extract word-sized chunk
                right += word_len  # move the right pointer
            
                if word in word_map:
                    cur_map[word] += 1
                    count += 1
                
                # if word count exceeds the required count, move the left pointer to shrink the window
                    while cur_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        cur_map[left_word] -= 1
                        count -= 1
                        left += word_len  # move left pointer forward
                
                # if all words matched, store the starting index
                    if count == word_count:
                        result.append(left)
            
                else:  # reset if an invalid word is found
                    cur_map.clear()
                    count = 0
                    left = right
    
        return result

'''
Test Case
s = "barfoothefoobarman"
words = ["foo","bar"]
Output
[0,9]
'''