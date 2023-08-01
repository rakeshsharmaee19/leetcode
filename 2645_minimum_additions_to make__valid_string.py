class Solution:
    def addMinimum(self, word: str) -> int:
        return len(word.replace('abc','X' ).replace('ab' ,'C' ).replace('ac' ,'B' ).replace('bc' ,'A' ).replace('a'  ,'AA').replace('b'  ,'BB').replace('c'  ,'CC').replace('X'  ,''  ))
