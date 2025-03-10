# [Diamond V] Sails - 5474 

[문제 링크](https://www.acmicpc.net/problem/5474) 

### 성능 요약

메모리: 5892 KB, 시간: 60 ms

### 분류

자료 구조, 그리디 알고리즘

### 제출 일자

2025년 3월 10일 20:38:59

### 문제 설명

<p>A new pirate sailing ship is being built. The ship has N masts (poles) divided into unit sized segments – the height of a mast is equal to the number of its segments. Each mast is fitted with a number of sails and each sail exactly fits into one segment. Sails on one mast can be arbitrarily distributed among different segments, but each segment can be fitted with at most one sail.</p>

<p>Different configurations of sails generate different amounts of thrust when exposed to the wind. Sails in front of other sails at the same height get less wind and contribute less thrust. For each sail we define its inefficiency as the total number of sails that are behind this sail and at the same height. Note that "in front of" and "behind" relate to the orientation of the ship: in the figure below, "in front of" means to the left, and "behind" means to the right.</p>

<p>The total inefficiency of a configuration is the sum of the inefficiencies of all individual sails. </p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/c1a99b8c-2f33-4131-be1a-a9a716f2f208/-/preview/" style="width: 745px; height: 323px;"><br>
 </p>

<p style="text-align: center;">This ship has 6 masts, of heights 3, 5, 4, 2, 4 and 3 from front (left side of image) to back. This distribution of sails gives a total inefficiency of 10. The individual inefficiency of each sail is written inside the sail.</p>

<p>Write a program that, given the height and the number of sails on each of the N masts, determines the smallest possible total inefficiency. </p>

### 입력 

 <p>The first line of input contains an integer N (2 ≤ N ≤ 100 000), the number of masts on the ship.</p>

<p>Each of the following N lines contains two integers H and K (1 ≤ H ≤ 100 000, 1 ≤ K ≤ H), the height and the number of sails on the corresponding mast. Masts are given in order from the front to the back of the ship. </p>

### 출력 

 <p>Output should consist of a single integer, the smallest possible total inefficiency.</p>

<p>Note: use a 64-bit integer type to calculate and output the result (long long in C/C++, int64 in Pascal). </p>

