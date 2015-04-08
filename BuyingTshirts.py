"""
A local store is selling T-shirts with the face of Fox Ciel printed on them. Each such T-shirt costs T pesos. Quimey and Pablo love those T-shirts. They each buy a new T-shirt whenever they have the money to do so. 

Currently, Quimey and Pablo have no money at all. During the following N days they are going to earn some money and they will use it to buy the T-shirts. The days are numbered from 0 (today) to N-1 (the day N-1 days in the future). 

For each valid i, Q[i] and P[i] are the amounts in pesos Quimey and Pablo will earn on day i. (Note that each of those amounts is at most T. Therefore, Quimey and Pablo will be able to buy at most one T-shirt each day.) 

For example, suppose that a T-shirt costs T=10 pesos. If Q={2,3,5,10}, the following will happen to Quimey:
On day 0, he earns 2 pesos. He now has 2 pesos.
On day 1, he earns 3 pesos. He now has 5 pesos.
On day 2, he earns 5 pesos. He now has 10 pesos, which is enough to buy a T-shirt. He goes to the store and buys one. Afterwards, he has 0 pesos left.
On day 3, he earns 10 pesos. He then goes to buy a second T-shirt. Afterwards, he again has 0 pesos left.
If P={10,8,6,4}, Pablo would buy one T-shirt on day 0, and then another T-shirt on day 2. After buying the T-shirt on day 2 he would have 4 pesos left. After day 3 he would then have a total of 8 pesos, which is still not enough for a T-shirt. Note that in this example Quimey and Pablo would go to the store together on day 2. 

You are given the int T: the price of a single T-shirt. You are also given the int[]s Q and P with N elements each: the amounts Quimey and Pablo earn each day. Compute and return the number of days on which Quimey and Pablo both go to the store
 
Definition
    	
Class:	BuyingTshirts
Method:	meet
Parameters:	int, int[], int[]
Returns:	int
Method signature:	int meet(int T, int[] Q, int[] P)
(be sure your method is public)

"""