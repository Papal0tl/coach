def min_window(s: str, t: str) -> str:
    class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        x = {}
        
        for ch in t:
            x[ch] = x.get(ch, 0) + 1
        
        window = {}
        l = 0
        v = 0
        min_len = float("inf")

        for j in range(len(t)):
            c = s[j]
            if c in x:
                window[c] = window.get(c, 0) + 1
                if window[c] == x[c]:
                    v += 1

            while v == len(x):

        if min_len == float("inf"):
            return ""

        return s[]
