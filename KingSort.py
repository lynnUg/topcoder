'''
Problem Statement
    	
Every good encyclopedia has an index. The entries in the index are usually sorted in alphabetic order. However, there are some notable exceptions. In this task we will consider one such exception: the names of kings.

In many countries it was common that kings of the same name received ordinal numbers. This ordinal number was written as a Roman numeral and appended to the actual name of the king. For example, "Louis XIII" (read: Louis the thirteenth) was the thirteenth king of France having the actual name Louis.

In the index of an encyclopedia, kings who share the same name have to be sorted according to their ordinal numbers. For example, Louis the 9th should be listed after Louis the 8th.

You are given a String[] kings. Each element of kings is the name of one king. The name of each king consists of his actual name, a single space, and a Roman numeral. Return a String[] containing the names rearranged into their proper order: that is, the kings have to be in ascending lexicographic order according to their actual name, and kings with the same name have to be in the correct numerical order.

 
Definition
    	
Class:	KingSort
Method:	getSortedList
Parameters:	String[]
Returns:	String[]
Method signature:	String[] getSortedList(String[] kings)
(be sure your method is public)
'''

class KingSort(object):
    ROMAN_TOKENS=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    ROMAN_VALUES=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    def convert_to_number(self,number):
    	result=0
    	for i in range(0,len(self.ROMAN_TOKENS)):
    		while(number.startswith(self.ROMAN_TOKENS[i])):
				number=number[len(self.ROMAN_TOKENS[i]):]
				result+=self.ROMAN_VALUES[i]
    	return result

    def comparator(self,x,y):
    	first=x.split(" ")
    	second=y.split(" ")
    	if first[0]!=second[0]:
    		if first[0]>second[0]:
    			return 1
    		return -1
    	else:
			if self.convert_to_number(first[1])>self.convert_to_number(second[1]):	
				return 1
			return -1
    def getSortedList(self,kings):
		kings_copy=[king for king in kings]
		kings_copy.sort(self.comparator)
		return kings_copy
first=KingSort()
print first.getSortedList(["A XL", "A X", "B X", "B XL", "A XI", "B XI"])