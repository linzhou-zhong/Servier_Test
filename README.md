# Servier Test Report
This repository contains `python` and `SQL` which correspond to the two parts of the technical test.

Each part has its own separate **README** with related explanations and screenshot of standard output. 

## Usage

```commandline
git clone https://github.com/linzhou-zhong/servier_test.git
```

## Python part

This project is based on [Hackerrank's SparseArrays](https://www.hackerrank.com/challenges/sparse-arrays/problem).

Simple algorithm question, I totally provided 3 different solutions with unequal Time Complexity from O(n) to O(n^2). 

For more details: [python part](https://github.com/linzhou-zhong/servier_test/tree/master/python)
## SQL part

This project is aimed to create two tables `transactions` and `product_nomEnclature`, and write some SQL statements to get observed results. 

For more details: [SQL part](https://github.com/linzhou-zhong/servier_test/tree/master/SQL)

## Useful Information

### Big O Notation

*Big O notation* is used to classify algorithms according to how their running time or space requirements grow as the input size grows.
On the chart below you may find most common orders of growth of algorithms specified in Big O notation.

![Big O graphs](images/big-o-graph.png)

Below is the list of some of the most used Big O notations and their performance comparisons against different sizes of the input data.

| Big O Notation | Computations for 10 elements | Computations for 100 elements | Computations for 1000 elements  |
| -------------- | ---------------------------- | ----------------------------- | ------------------------------- |
| **O(1)**       | 1                            | 1                             | 1                               |
| **O(log N)**   | 3                            | 6                             | 9                               |
| **O(N)**       | 10                           | 100                           | 1000                            |
| **O(N log N)** | 30                           | 600                           | 9000                            |
| **O(N^2)**     | 100                          | 10000                         | 1000000                         |
| **O(2^N)**     | 1024                         | 1.26e+29                      | 1.07e+301                       |
| **O(N!)**      | 3628800                      | 9.3e+157                      | 4.02e+2567                      |
---
Source: [Big O Cheat Sheet](http://bigocheatsheet.com/).
