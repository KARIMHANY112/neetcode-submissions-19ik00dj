from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_count = Counter(t)
        window = {}

        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in t_count and window[c] == t_count[c]:
                have += 1

            # shrink window
            while have == need:
                # update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # remove from left
                left_char = s[l]
                window[left_char] -= 1

                if left_char in t_count and window[left_char] < t_count[left_char]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""