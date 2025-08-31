# [Gold III] Dutch Democracy - 32892 

[문제 링크](https://www.acmicpc.net/problem/32892) 

### 성능 요약

메모리: 112404 KB, 시간: 168 ms

### 분류

정렬, 배낭 문제

### 제출 일자

2025년 8월 31일 16:49:19

### 문제 설명

<p>The process of forming the Dutch government has taken more than half a year for three elections in a row. Perhaps we can streamline the initial stages of coalition building?</p>

<p>The first step after the election results is to find a group of parties (called a <em>coalition</em>) with enough seats to have a strict majority. Your task is to count the number of candidate coalitions that satisfy specific conditions. A coalition is considered a <em>candidate coalition</em> if it meets these two criteria:</p>

<p><strong>Strict Majority:</strong> The total number of seats held by the coalition must be strictly more than half of the total seats across all parties.</p>

<p><strong>No Superfluous Parties:</strong> The coalition must be minimal in the sense that removing any one party from the coalition would cause it to lose its strict majority.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0aedabe8-91ab-45c0-8807-5aff2e320360/-/preview/" style="width: 389px; height: 200px;"></p>

<p style="text-align: center;">Figure D.1: Illustration of Sample Input 2.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 106.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 106.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c36"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>60</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 60$</span></mjx-container>), the number of parties.</li>
	<li>One line with <mjx-container class="MathJax" jax="CHTML" style="font-size: 106.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> integers <mjx-container class="MathJax" jax="CHTML" style="font-size: 106.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 106.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>p</mi><mo>≤</mo><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le p \le 10\,000$</span></mjx-container>), the number of seats each party has.</li>
</ul>

### 출력 

 <p> Output the total number of candidate coalitions that satisfy the criteria above.</p>

