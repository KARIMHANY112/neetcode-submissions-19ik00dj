class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}        # char -> frequency
        max_freq = 0
        max_length = 0

        for r in range(len(s)):
            char = s[r]

            # update frequency
            count[char] = count.get(char, 0) + 1

            # update max frequency
            max_freq = max(max_freq, count[char])

            # check if window is invalid
            if (r - l + 1) - max_freq > k:
                # shrink window
                count[s[l]] -= 1
                l += 1

            # update answer
            max_length = max(max_length, r - l + 1)

        return max_length