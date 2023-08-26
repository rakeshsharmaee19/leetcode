class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        s=''
        
        while columnNumber>0:
            s=a[((columnNumber-1)%26)]+s
            columnNumber=(columnNumber-1)//26
        return s
