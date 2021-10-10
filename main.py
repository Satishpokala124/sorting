import random
import time
from algorithms import *

# n = int(input("Enter a number : "))
# arr = list(map(int,input().split()))
n = 1000
while n <= 10000:
  print('n = ', n, ":")
  arr = [random.randint(1, n) for _ in range(n)]
  start = time.time()
  bubbleSort(arr)
  start1 = time.time()
  mergeSort(arr)
  end = time.time()

  print('Total time taken by "bubbleSort" is', start1 - start)
  print('Total time taken by "mergeSort" is', end - start1)
  n = n*2

