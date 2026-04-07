from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window_count = Counter()

        l = 0
        for r in range(len(s2)):
            # add current character
            window_count[s2[r]] += 1

            # keep window size equal to len(s1)
            if (r - l + 1) > len(s1):
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                l += 1

            # compare counts
            if window_count == s1_count:
                return True

        return False