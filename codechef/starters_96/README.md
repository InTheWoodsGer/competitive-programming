# STARTER 96

https://www.codechef.com/START96

| Name                 | Div 4 | Div 3 | Div 2 | Div 1 | Done |
|----------------------|-------|-------|-------|-------|------|
| AB Difference        | X     |       |       |       | X    |
| Bells of Pilgrimage  | X     | X     |       |       | X    |
| Weeding              | X     | X     |       |       |      |
| Remove Multiples     | X     | X     | X     |       |      |
| Swap the Numbers     | X     | X     | X     | X     |      |
| Mex Array            | X     | X     | X     | X     |      |
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
