#SUBSET SUM
# you are given N numbers. Check if there is  asubset of them, with the sum equal to target value S. (N<=20)
#using Bitwise operators

from typing import List
def subsetSum(a: List, target: int) -> bool:
    for mask in range(1<<len(a)):
        s = 0
        for i in range(len(a)):
            if mask & (1<<i):
                s += a[i]
        if s == target:
            return True
    return False

print(subsetSum([1,2,3,4,5,6,7,8,9,10], 100))