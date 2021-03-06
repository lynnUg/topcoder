"""
You are given a String S. The string can have up to 2500 characters.

You have to reverse exactly one substring of S. Formally, you have to choose two 0-based indices {x,y} such that x <= y, and then you have to reverse the order of the letters with indices x through y, inclusive. That is, S[x]S[x+1]...S[y] becomes S[y]...S[x+1]S[x].

For example, if S="abcdefg", you can choose the indices {2,5} to obtain "abfedcg", the indices {0,1} to obtain "bacdefg", or the indices {3,3} to obtain "abcdefg". (In the last example, only one letter was selected, so the string did not change.)

Your goal is to produce the lexicographically smallest string possible. Return a int[] containing two elements: the optimal indices x and y. If there are multiple optimal choices, find the one with the smallest x. If there are still multiple optimal choices, find the one with the smallest y.




"""
import copy
class SubstringReversal(object):
    def solve(self,S):
        A=list(S)
        min_A=A[-1]
        start=-1
        for i in range(len(A)-1,-1,-1):
            if A[i]>min_A:
                start=i
            else:
                min_A=A[i]

        if start==-1:
            return [0,0]
        x,y=start,start
        check=S
        for i in range(start,len(A)):
            B=copy.deepcopy(A)
            k,j=start,i
            while k<j:
                print B[k],B[j]
                B[k],B[j]=B[j],B[k]
                print B
                k+=1
                j-=1
            temp=''.join(B)
            if temp<check:
                y=i
                check=temp
        return [x,y]

firstReversal=SubstringReversal()
assert firstReversal.solve("abdc")==[2,3]

