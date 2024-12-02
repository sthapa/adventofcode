import os
from collections import defaultdict

list1 = []
list2 = []
with  open('day1_input') as f:
  for line in f:
    input = line.strip().split(' ')
    list1.append(int(input[0]))
    list2.append(int(input[-1]))
list1.sort()
list2.sort()
distance = 0
for i in range(len(list1)):
  distance += abs(list1[i] - list2[i])
print(distance)


similarity = 0
appearances = {}
for k in list2:
  appearances[k] = appearances.get(k, 0) + 1
for k in list1:
  if k in appearances:
    similarity += k * appearances[k]
print(f"Similarity: {similarity}")