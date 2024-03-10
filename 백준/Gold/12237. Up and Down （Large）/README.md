# [Gold IV] Up and Down (Large) - 12237 

[문제 링크](https://www.acmicpc.net/problem/12237) 

### 성능 요약

메모리: 31120 KB, 시간: 1444 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 3월 10일 21:46:17

### 문제 설명

<p>You are given a sequence of distinct integers <strong>A</strong> = [<strong>A</strong><strong><sub>1</sub></strong>, <strong>A</strong><strong><sub>2</sub></strong>, ..., <strong>A</strong><strong><sub>N</sub></strong>], and would like to rearrange it into an <em>up and down</em> sequence (one where <strong>A</strong><strong><sub>1</sub></strong> < <strong>A</strong><strong><sub>2</sub></strong> < ... < <strong>A</strong><strong><sub>m</sub></strong> > <strong>A</strong><strong><sub>m+1</sub></strong> > ... > <strong>A</strong><strong><sub>N</sub></strong> for some index <strong>m</strong>, with m between 1 and <strong>N</strong> inclusive).</p>

<p>The rearrangement is accomplished by swapping two <strong><em>adjacent</em></strong> elements of the sequence at a time. Predictably, you are particularly interested in the minimum number of such swaps needed to reach an <em>up and down</em> sequence.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case begins with a line containing a single integer: <strong>N</strong>. The next line contains <strong>N</strong> <strong><em>distinct</em></strong> integers: <strong>A</strong><strong><sub>1</sub></strong>, ..., <strong>A</strong><strong><sub>N</sub></strong>.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>A</strong><strong><sub>i</sub></strong> ≤ 10<sup>9</sup></li>
	<li>The <strong>A</strong><strong><sub>i</sub></strong> will be pairwise distinct.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> ≤ 1000.</span></li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of swaps required to rearrange <strong>A</strong> into an <em>up and down</em> sequence.</p>

