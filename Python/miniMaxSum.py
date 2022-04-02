#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers. 

Function Description
    Complete the miniMaxSum function in the editor below.
    miniMaxSum has the following parameter(s):
      arr: an array of 5 integers

Print
    Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

Input Format
    A single line of five space-separated integers.

Constraints
    1< arr[i] < 10^9
Output Format
    Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input
    5 2 3 1 4

Sample Output
    10 14

Explanation
    Sort Array to [1,2,3,4,5]
    10 = 1 + 2 + 3 + 4
    14 = 2 + 3 + 4 + 5
    
"""

def miniMaxSum(arr):
    arr.sort()
    min_start_index = 0
    max_start_index = 1
    min_end_index = len(arr)-2
    max_end_index = len(arr)-1
    min_sum = max_sum = 0
        
    for i in range(len(arr)):
        if (i>=min_start_index and i<=min_end_index): min_sum = min_sum + arr[i]
        if (i>=max_start_index and i<=max_end_index): max_sum = max_sum + arr[i]
    
    print(str(min_sum) + " " + str(max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
