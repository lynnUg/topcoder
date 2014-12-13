"""



 Problem Statement for CostOfDancing


Problem Statement
    	
Gustavo studies at the Byteversity (one of the best universities in Byteland). He's also very keen on dancing, so he decided to enroll at a dance school.



The school offers many different courses, each teaching one dance. Different courses may have different costs. You are given a int[] danceCost. The elements of danceCost are the costs of all courses offered at the dance school.



Gustavo would like to learn exactly K of those dances. He is a poor student, so his only priority is to pay as little as possible for the courses.



You are given the int K and the int[] danceCost. Compute and return the smallest possible total cost of learning K dances.

 
Definition
    	
Class:	CostOfDancing
Method:	minimum
Parameters:	int, int[]
Returns:	int
Method signature:	int minimum(int K, int[] danceCost)
(be sure your method is public)

"""
class CostOfDancing(object):
	def minimum(self,K,danceCost):
		return sum(sorted(danceCost)[:K])
firstDance=CostOfDancing()
assert firstDance.minimum(2,[1, 5, 3, 4]) ==4