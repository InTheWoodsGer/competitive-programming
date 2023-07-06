# STARTER 97

https://www.codechef.com/START97

| Name                     | Div 4 | Div 3 | Div 2 | Div 1 | Done |
|--------------------------|-------|-------|-------|-------|------|
| 2000                     | X     |       |       |       |      |
| Best of Two              | X     | X     |       |       |      |
| Caesar Cipher            | X     | X     |       |       |      |
| Schrodinger Smiley       | X     | X     | X     |       |      |
| Triplets Min             | X     | X     | X     | X     |      |
| No Plaindrome            | X     | X     | X     | X     |      |
| Make it Special          | X     | X     | X     | X     |      |
| Unreachability Cost      | X     | X     | X     | X     |      |
| Chec and Division        |       | X     | X     | X     |      |
| Disappearing Domino Game |       |       | X     | X     |      |

## 2000

**Problem**

Chef had collected N notes of Rs. 2000 to pay his total college fees. However, the government banned Rs. 2000 notes.

Chef wants to pay the same amount using Rs. 500 notes only. Find the number of notes Chef needs.

**Input Format**

Each test case consists of a single integer N - the number of notes of Rs. 2000 that Chef has collected.

**Output Format**

Output a single integer - the number of Rs. 500 notes needed.

**Constraints**

- 1≤N≤100

## Best of Two

**Problem**

Alice and Bob are playing a game. Each player rolls a regular six faced dice 3 times.
The score of a player is the sum of the values of the highest 2 rolls. The player with the highest score wins, and the game ends in a Tie if both players have the same score.

Find the winner of the game or determine whether it is a tie.

**Input Format**

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case contains six space-separated integers A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>, B<sub>1</sub>, B<sub>2</sub>, B<sub>3</sub> — the values Alice gets in her 3 dice rolls, followed by the values which Bob gets in his 3 dice rolls.

**Output Format**

For each test case, output on a new line Alice if Alice wins, Bob if Bob wins and Tie in case of a tie.

Note that you may print each character in uppercase or lowercase. For example, the strings tie, TIE, Tie, and tIe are considered identical.

**Constraints**

- 1≤T≤10<sup>10</sup>
- 1≤A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>, B<sub>1</sub>, B<sub>2</sub>, B<sub>3</sub>≤6

## Caesar Cipher

**Problem**

In the ROT-K cipher, each character in the string is shifted a fixed number of positions down the alphabet. The value of K represents the number of positions to shift. For instance, in ROT-2, each character is shifted 2 positions. The ROT-2 cipher of the string code is eqfg.

Note that the rotation is performed in a circular manner, meaning that if the character z is shifted by one position, we obtain the character a.

You are given strings S,T, and U, each of length N, such that the ROT-K cipher of string S is string T.

Find the ROT-K cipher of string U.

**Input Format**

- The first line of input will contain a single integer Q, denoting the number of queries.
- Each query consists of multiple lines of input.
  - The first line of each query contains N — the length of the strings.
  - The second line contains the string S.
  - The third line contains the string T.
  - The fourth line contains the string U.

**Output Format**

For each query, output on a new line, the ROT-K cipher of string U.

**Constraints**

- 1≤Q≤100
- 1≤N≤1000
- S,T, and U contain lowercase english alphabets only.

## Schrodinger Smiley

**Problem**

In the realm of emoticons, the Schrödinger smiley both smiles and frowns until its state is observed.

Given a string S consisting only of :, (, and ) (colon, left parenthesis, and right parenthesis).

We define a Schrödinger's Smiley as any positive number of right parenthesis between two colons. For example, :):, :))):, and :))))): are Schrödinger's smileys while :))(:, :(:, ::): and :: are not.

Find the total number of substrings in S that are Schrödinger Smileys.

A substring is obtained by deleting any (possibly zero) number of characters from the beginning and any (possibly zero) number of characters from the end of the string.

**Input Format**

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
  - The first line of each test case contains an integer N, the length of the string S.
  - The next line contains the string S.

**Output Format**

For each test case, output on a new line, the total number of substrings in S that are Schrödinger Smileys.

**Constraints**

- 1≤T≤10<sup>5</sup>
- 1≤N≤10<sup>5</sup>
- S consists of :, (, and ) only.
- The sum of N over all test cases won't exceed 5⋅10<sup>5</sup>.

