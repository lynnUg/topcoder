"""
You are given a String S. The string can have up to 2500 characters.

You have to reverse exactly one substring of S. Formally, you have to choose two 0-based indices {x,y} such that x <= y, and then you have to reverse the order of the letters with indices x through y, inclusive. That is, S[x]S[x+1]...S[y] becomes S[y]...S[x+1]S[x].

For example, if S="abcdefg", you can choose the indices {2,5} to obtain "abfedcg", the indices {0,1} to obtain "bacdefg", or the indices {3,3} to obtain "abcdefg". (In the last example, only one letter was selected, so the string did not change.)

Your goal is to produce the lexicographically smallest string possible. Return a int[] containing two elements: the optimal indices x and y. If there are multiple optimal choices, find the one with the smallest x. If there are still multiple optimal choices, find the one with the smallest y.



 Problem Statistics for 2014 TCO Algorithm > Round 2C > Room 36 > twds

	Class Name	Method Name	 	Difficulty	Status	Score	

	[ SubstringReversal ]	solve	problem details	Level One	Passed System Test	279.23	
	CliqueGraph	calcSum	problem details	Level Two	Passed System Test	195.32	
	InverseRMQ	possible	problem details	Level Three	Opened	0.00	



View SubstringReversal   Problem Statement
import java.util.*;
public class SubstringReversal {
    public int[] solve(String S) {
        int N = S.length();
        char[] arr = S.toCharArray();
        char min = arr[N - 1];
        int find = -1;
        for (int i = N - 2; i >= 0; --i) 
        {
            if (arr[i] > min)
            {
                find = i;
            } 
            else 
            {
                min = arr[i];
            }
        }
        if (find == -1) 
        {
            return new int[]{0, 0};
        }
        int x = find;
        int y = x;
        String check = S;
        for (int i = x; i < N; ++i) 
        {
            char[] copy = Arrays.copyOf(arr, N);
            for (int j = x, k = i; j < k; ++j, --k) 
            {
                char temp = copy[j];
                copy[j] = copy[k];
                copy[k] = temp;
           }
            String temp = new String(copy);
            if (temp.compareTo(check) < 0) 
            {
                y = i;
                check = temp;
            }
        }
        return new int[]{x, y};
    }
    
 
}
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
            while k<len(A) and j>-1:
                print B[k],B[j]
                B[k],B[j]=B[j],B[k]
                print B
                k+=1
                j-=1
            temp=''.join(B)
            print temp,start
            if temp<check:
                y=j
                check=temp
        return [x,y]

firstReversal=SubstringReversal()
print firstReversal.solve("abdc")
#assert firstReversal.solve("abdc")==[2,3]

