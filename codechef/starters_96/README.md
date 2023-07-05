# STARTER 96

https://www.codechef.com/START96

| Name                 | Div 4 | Div 3 | Div 2 | Div 1 | Done |
|----------------------|-------|-------|-------|-------|------|
| AB Difference        | X     |       |       |       | X    |
| Bells of Pilgrimage  | X     | X     |       |       | X    |
| Weeding              | X     | X     |       |       | X    |
| Remove Multiples     | X     | X     | X     |       | X    |
| Swap the Numbers     | X     | X     | X     | X     | X    |
| Mex Array            | X     | X     | X     | X     | X    |
| Zero Array           | X     | X     | X     | X     |      |
| Remove Stones        | X     | X     | X     | X     |      |
| Absolute Differences |       |       | X     | X     |      |
| Chef and Prefixes    |       | X     | X     | X     |      |

## AB Differences

**Problem**

Chef is taking his baby steps into the world of programming.

The very first program he's tasked to write is as follows:
"Given two integers A and B, print A+B."

Unfortunately, Chef makes a typo: his program outputs A×B instead of A+B.

Given the values of A and B, can you help Chef find the absolute difference between the correct answer and the value his program prints?

**Input Format**

The only line of input will contain two space-separated integers, A and B.

**Output Format**

Print a single integer: the difference between the correct answer and Chef's output.

**Constraints**

1≤A,B≤10

## Bells of Pilgrimage

**Problem**

The Child of Prophecy has embarked on a journey to save the land of the Fae.
On her journey, she must ring N Bells of Pilgrimage.

The Child of Prophecy has an initial mana level of P. After that:
- Each of the first X bells she rings will increase her mana level by 10.
- Each of the remaining bells will increase her mana level by 5.
- As a bonus, once the final bell is rung, her mana level will increase by a further 20.

K bells have been rung so far. What is the current mana level of the Child of Prophecy?

**Input Format**

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single line of input, containing four space-separated integers N, X, K, and P — as described in the statement.

**Output Format**

For each test case, output on a new line a single integer: the Child of Prophecy's current mana level.

**Constraints**
- 1≤T≤100
- 1≤X<N≤10<sup>5</sup>
- 0≤K≤N
- 0≤P≤10<sup>5</sup>

## Weeding

**Problem**

Chef purchased a new herbicide, and now wants to test its effectiveness.

Initially, there are no weeds in Chef's garden.
For each i=1,2,3,…,N, exactly one new weed will pop up in the garden at the start of day A<sub>i</sub>.
It is known that A<sub>1</sub><A<sub>2</sub><…<A<sub>N</sub>.

Chef can spray the herbicide at most once per day.
Any weed that receives the spray K or more times in total will die.

Chef would like to know: is it possible that after M days, all the weeds are gone?

**Input Format**

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
  - The first line of each test case contains three space-separated integers N, M, and K — the number of weeds, the total number of days, and the number of sprays needed to kill a weed, respectively.
  - The second line of each test case contains N space-separated integers A<sub>1</sub><A<sub>2</sub><…<A<sub>N</sub>: the days on which new weeds show up.

**Output Format**

For each test case, output on a new line the answer: Yes if all the weeds are gone after M days, and No otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings Yes, YES, yes, and YeS will all be treated as equivalent.

**Constraints**

- 1≤T≤10<sup>5</sup>
- 1≤N≤10<sup>5</sup>
- 1≤A<sub>1</sub><A<sub>2</sub><A<sub>3</sub><…<A<sub>N</sub>≤M≤10<sup>9</sup>
- 1≤K≤10<sup>9</sup>
- The sum of N across all tests won't exceed 2⋅10<sup>5</sup>.

## Remove Multiples

**Problem**

You are given integers N and M.

You have with you the set S={1,2,3,…,N}.

You are also given a set Q of size M, which is a subset of the set S.
You are required to convert S into Q using the following operation:

- Choose an integer k (1≤k≤N) such that there exists a multiple of k in S, and remove the smallest multiple of k from S.
This incurs a cost of k.

For example, if S={1,3,4,6} and you choose k=2, you delete the smallest multiple of 2 present in S (which is 4) for a cost of 2.

After this, S will be {1,3,6}.

Find the maximum cost required to convert S to Q.

**Input Format**

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
  - The first line of each test case contains two space-separated integers N and M — the number of elements in the set S and set Q respectively.
  - The second line contains M spaced integers, denoting the elements of the set Q.

**Output Format**

For each test case, output on a new line the maximum cost required to convert S to Q.

**Constraints**
- 1≤T≤10<sup>5</sup>
- 1≤N≤10<sup>9</sup>
- 1≤M≤N
- The sum of M over all test cases does not exceed 3×10<sup>5</sup> 

## Swap the Numbers

**Problem**

You're given an array A=[A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>] containing N integers.
You also have an integer K.

You can perform the following operation on this array:
- Choose indices i and j such that ∣i−j∣≥K, and swap A<sub>i</sub> and A<sub>j</sub>. 
That is, you can swap the values of two indices that are at a distance of at least 
K from each other.

- Find the lexicographically smallest array that can be reached, if you perform the above operation several (possibly, zero) times.

Note: For two arrays X and Y of the same length, X is said to be lexicographically smaller than Y if there exists an index i (1≤i≤N) such that:
- X<sub>1</sub>=Y<sub>1</sub>, X<sub>2</sub>=Y<sub>2</sub>, ...,X<sub>i-1</sub>=Y<sub>i-1</sub>; and
- X<sub>i</sub> < Y<sub>i</sub>
 
**Input Format**

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
  - The first line of each test case contains two space-separated integers N and K.
  - The next line contains N space-separated numbers, the values A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>.

**Output Format**

For each test case, print on a new line N space-separated integers — the lexicographically smallest array possible after applying the above operation several times.

**Constraints**

- 1≤T≤10<sup>4</sup>
- 1≤N,K≤10<sup>5</sup>
- 1≤A<sub>i</sub>≤10<sup>9</sup>
- The sum of N across all tests won't exceed 10<sup>6</sup>.

## Mex Array

**Problem**

Given an array A containing N non-negative integers, you have to create a new array B that is formed in the following way:

While A is not empty:
- Choose an integer k (1≤k≤∣A∣). Here, ∣A∣ denotes the current length of A.
- Choose k elements of A.
- Append the MEX of these chosen elements to the end of array B, and erase them from the array A.

That is, in each move you pick a non-empty subsequence of A, append its MEX to B, and delete the subsequence from A.

Find the lexicographically maximum array B that can be formed via this process.

Notes:
- An array X is lexicographically greater than an array Y if:
  - In the first position where X and Y differ, X<sub>i</sub>>Y<sub>i</sub>; or
  - ∣X∣>∣Y∣ and Y is a prefix of X.
- The MEX of a set of non-negative integers is the minimal non-negative integer that is not in the set. For example, MEX({1,2,3,2})=0 and MEX({0,1,2,5,4})=3.

**Input Format**

- The first line of the input contains a single integer T — the number of test cases. The description of test cases follows.
- Each test case consists of two lines of input.
  - The first line of each test case contains a single integer N — the number of elements in the array A.
  - The second line of each test case contains N space-separated non-negative integers A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>, where A<sub>i</sub> is the i<sup>th</sup> integer from the array A.

**Output Format**

For each test case, print two lines.
- The first line should contain a single integer M — the length of the lexicographically maximum array B you can create.
 - The second line should contain M space-separated integers, denoting the elements of the array B.

**Constraints**

- 1≤T≤10<sup>5</sup>
- 1≤N≤2⋅10<sup>5</sup>
- It is guaranteed that the sum of N over all test cases does not exceed 2*10<sup>5</sup>.
- 0≤A<sub>i</sub>≤N.