class Solution:
    def finalString(self, s: str) -> str:
        ss = ''
        for i in s:
            if i=='i':
                ss=ss[::-1]
            else:
                ss=ss+i
        # print(ss)
        return ss
