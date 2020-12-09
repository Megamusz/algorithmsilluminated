# Algorithm Illuminated Exercises

## Overview

This repository contains solutions to the programming projects accompanied with [Tim Roughgarden's](http://www.timroughgarden.org/) Algorithm Illuminated series. This is a great series that you definitely don't want to miss, for more details check here [Algorithm Illuminated](http://www.algorithmsilluminated.org/)

## Intention

These solutions are just for reviewing the algorithms mentioned in the corresponding video lectures. To make the implementation simple, the solutions here are more or less the naive implementation of algorithms described in the slides, so not surprisingly, some of them might not scale to large problem sizes. 


## Getting Started

To sanity check these solutions, first you need to download the testcases from [here](http://www.algorithmsilluminated.org/datasets/) and put them under ./algorithmsilluminated/tests/. After that try the following command:

```
cd ./algorithmsilluminated
python -m unittest -v
```

you can also run the solution file itself, sanity check is added in each of the main functions e.g.

```
cd ./algorithmsilluminated
./algorithm/bellbellman_ford.py
```

For more test cases, check here: [stanford-algs](https://github.com/beaunus/stanford-algs). (Note the **alg** method defined in each solution file is used for testing the cases there)

## List of Algorithms 
* [Sorting](#sorting)
    * [Quick Sort](#quick-sort)
    * [Merge Sort](#merge-sort)
* [Selection](#selection)
    * [Randomized Selection](#randomized-selection)
* [Scheduling](#scheduling)
* [Huffman Encoding](#huffman-encoding)
* [Knapsack Problem](#knapsack-problem)
* [Sequence Alignment](#sequence-alignment)
* [Weighted Independent Set](#weighted-independent-set)
* [Optimal Binary Search Tree](#optimal-binary-search-tree)
* [Single Source Shortest Path (SSSP)](#single-source-shortest-path-(sssp))
    * [Dijkstra's shortest path](#dijkstra)  
    * [Bellman-Ford](#bellman-ford)
* [All Pair Shortest Path (APSP)](#all-pair-shortest-path-(apsp))
    * [Floyd-Warshall](#floyd-warshall)
    * [Johnson](#johnson)
* [Strongly Connected Components](#strongly-connected-components)  
    * [Kosaraju's 2-pass Algorithm](#kosaraju's-2-pass-algorithm)
* [Minimum Cut](#minimum-cut)
    * [Karger's mincut algorithm](#karger's-mincut-algorithm)
* [Minimum Spanning Tree](#minimum-spanning-tree)
    * [Prim's Algorithm](#prim's-algorithm)
    * [Kruskal's Algorithm](#kruskal's-algorithm)
* [TSP (Traveling Sales Man) Problem](#tsp-(traveling-sales-man)-problem)
* [2-SAT Problem](#2-sat-problem)
    * [Papadimitriou's algorithm](#papadimitriou's-algorithm)
* [Vertex Cover Problem](#vertex-cover-problem)
* [Misc](#misc)
    * [Karatsuba multiplication](#karatsuba-multiplication)
    * [Counting inversions](#counting-inversions)
    * [Median maintenance](#median-maintenance)
    * [Two Sum](#two-sum)
* [Data Structures](#data-structures)
    * [Heap](#heap)
    * [Hash-table](#hash-table)
    * [Union-Find](#union-find)

## Sorting
Problem definition:  
**Input**: array of n numbers, unsorted  
**Output**: Same numbers, sorted in increasing order  

### Quick Sort  
Average Running time **O(nlog(n))**

Pesudo code  
```
QuickSort(array A, length n)
- if n = 1 return
- p = ChoosePivot(A, n)
- Partition A around p
- Recursively sort 1st part
- Recursively sort 2nd part
```
Pesudo code for Partition  
```
Partition(A, l, r) [input corresponds to A[l...r]]
    - p := A[l]
    - i := l + 1
    - for j = l + 1 to r
        - if A[j] < p   [if A[j] > p, do nothing]
            - swap A[j] and A[i]
            - i := i+1
    - swap A[l] and A[i-1]
```

Code: [quick_sort.py](algorithms/quick_sort.py) 
### Merge Sort
Running time **O(nlog(n))**

Pseudo code
```
- recursively sort 1st half of the input array
- recursively sort 2nd half of the input array
- merge two sorted sub array into one
[ignores base cases]
```

Pseudo code for the merge step
```
C = output[length=n] 
A = 1st sorted array [n/2]
B = 2nd sorted array [n/2]
i = 1 
j = 1

for k = 1 to n
    if A[i] < B[j]
        C[k] = A[i]
        i++
    else B[j] < A[i]
        C[k] = B[j]
        j++
    
[ignore end cases]
```
Code [merge_sort.py](algorithms/merge_sort.py)  

## Selection  
Problem definition:  
**Input**: array A with n distinct (for simplicity) numbers and a number  
**Output**: ith order statistic (i.e.ith smallest element of input array)

### Randomized Selection
Average running time **O(n)**

Pseudo code
```
Rselect(array A, length n, order statistic i)
- if n = 1 return A[1]
- Choose pivot p from A uniformly
- Partition A around p
  let j = new index of p
- if j = i, return p
- if j > i, return Rselect(1st part of A, j-1, i)
- if j < i, return Rselect(2nd part of A, n-j, i-j)
```

Code: [randomized_selection.py](algorithms/randomized_selection.py)

## Scheduling 


## Huffman Encoding 


## Knapsack Problem 

## Weighted Independent Set 

### Randomized Selection 

## Single Source Shortest Path (SSSP) 

### Dijkstra 

### Bellman-Ford 

## All Pair Shortest Path (APSP)

### Floyd-Warshall 

### Johnson 

## Strongly Connected Components 

### Kosaraju's 2-pass Algorithm 

## Sequence Alignment 

## TSP (Traveling Sales Man) Problem 

## Vertex Cover Problem 