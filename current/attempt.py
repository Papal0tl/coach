class Solution:
    def minWindow(self, s: str, t: str) -> str:
        x = {}

        for ch in t:
            x[ch] = x.get(ch, 0) + 1

        window = {}
        l = 0
        v = 0
        min_len = float("inf")

        first = 0

        for r in range(len(s)):
            c = s[r]
            if c in x:
                window[c] = window.get(c, 0) + 1
                if window[c] == x[c]:
                    v += 1

            while v == len(x):
                if r - l + 1 <= min_len:
                    min_len = r - l + 1
                    first = l

                d = s[l]
                l += 1
                if d in x:
                    if window[d] == x[d]:
                        v -= 1
                    window[d] -= 1

        if min_len == float("inf"):
            return ""

        return s[first: first + min_len]
