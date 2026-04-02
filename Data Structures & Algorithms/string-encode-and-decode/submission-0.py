class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index("#", i)        # find the '#' separator
            length = int(s[i:j])       # read the length
            res.append(s[j+1:j+1+length])  # extract exactly that many chars
            i = j + 1 + length         # move pointer forward
        return res
