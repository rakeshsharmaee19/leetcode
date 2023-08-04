class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        for i in wordDict:
            if i in s:
                if i[0] in dic:
                    dic[i[0]].append(i)
                else:
                    dic[i[0]]=[i]
        def ch(st, k, arr):
            if len(st)==k:
                return True
            elif arr[k]!=None:
                return arr[k]
            elif st[k] in dic:
                for i in dic[st[k]]:
                    if len(i)<=len(st[k:]):
                        if st[k:k+len(i)]==i:
                            k+=len(i)
                            rt = ch(st,k,arr)
                            if rt:
                                arr[k]=True
                                return True 
                            else:
                                k=k-len(i) 
                arr[k]=False
                return False     
            else:
                arr[k]=False
                return False
        arr=[None]*(len(s)+1)
        k=0
        aaa = ch(s, k, arr)
        return aaa        
