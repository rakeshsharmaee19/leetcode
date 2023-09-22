class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        n_t = len(t)
        i=0
        c=0
        while i<n_t and c<n:
            if t[i]==s[c]:
                c+=1
            i+=1
        if c==n:
            return True
        else:
            return False
