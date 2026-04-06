class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        seen = {}   # char -> last index
        for r in range(len(s)):
            char = s[r]

            if char in seen:
                # move left pointer (IMPORTANT: don't move it backwards)
                l = max(l, seen[char] + 1)

            # update last seen index of current character
            seen[char] = r

            # update max length
            max_length = max(max_length, r - l + 1)

        return max_length