#!/bin/python3
import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    for i in range(n):
        j=i-1
        while j>=0 and arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j],arr[j+1]=arr[j+1],arr[j]
            j-=1
            nn=arr[:]
            nn[j+1]=temp
            print(*nn)
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
