# [Diamond III] Coin Collecting - 16983 

[문제 링크](https://www.acmicpc.net/problem/16983) 

### 성능 요약

메모리: 123084 KB, 시간: 240 ms

### 분류

그리디 알고리즘

### 제출 일자

2025년 3월 31일 19:56:51

### 문제 설명

<p>Mr. JOI has a huge desk in his collection room, and there are a number of rare coins on it. To clean up the desk, he is going to rearrange the coins.</p>

<p>The desk can be regarded as a 2 000 000 001 × 2 000 000 001 grid. The columns are numbered from −1 000 000 000 through 1 000 000 000 from left to right, and the rows are numbered from −1 000 000 000 through 1 000 000 000 from bottom to top. The cell with the column number x and the row number y is denoted by (x, y).</p>

<p>There are 2N coins. Currently, the i-th coin (1 ≤ i ≤ 2N) is placed at the cell (X<sub>i</sub>, Y<sub>i</sub>). Mr. JOI’s goal is to place a coin on each cell (x, y) with 1 ≤ x ≤ N and 1 ≤ y ≤ 2. In order not to hurt the coins, the only operation he can perform is to choose a coin and move it to one of the neighboring cells (a cell neighbors another if and only if they share an edge). It is allowed that multiple coins are placed on a cell at some point. He wants to achieve the goal with as few operations as possible.</p>

<p>Write a program which, given the number of coins and the cells where the coins are currently placed, calculates the minimum number of operations needed to achieve the goal.</p>

### 입력 

 <p>Read the following data from the standard input.</p>

<pre>N
X<sub>1</sub> Y<sub>1</sub>
.
.
.
X<sub>2N</sub> Y<sub>2N</sub></pre>

### 출력 

 <p>Write one line to the standard output. The output should contain the minimum number of operations needed to achieve the goal.</p>

