#(VIRTUAL) WEEKLY CONTEST 277
from collections import Counter
from typing import List
# 2:25 (1)
class Solution:
    def countElements(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        count = Counter(nums)
        return len(nums) - count[a] - count[b] if a!=b else 0

#solucion superluminal:
"""
a = nums
lo = min(a)
hi = max(a)
return sum(1 for v in nums if lo < v < hi)"""

# 2:17
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        res = []    
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
            
        return res

#solucion superluminal:

"""r = [0]* len(nums)
r[::2] = [v for v in nums if v > 0]
r[1::2] = [v for v in nums if v < 0]
return r """

#2:40
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for i in range(len(nums)):
            if count[nums[i]] == 1 and count[nums[i]-1] == 0 and count[nums[i]+1] == 0:
                res.append(nums[i])
            
        return res

#solucion superluminal (misma pero escrita mas concisa)

"""
c = Counter(nums)
return [k for k, v in c.iteritems() if v==1 and (k-1) not in c and (k+1) not in c] """

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        res = 0
        n = len(statements)
        
        def check(personas):
            for i in range(n):
                if personas[i] == "0": # si es mentiroso paso a la proxima persona
                    continue
                for j in range(n): # si no es mentiroso me fijo en cada uno de los statements
                    if statements[i][j] == 2: # si no dice nada sobre la otra persona sigo
                        continue
                    if (statements[i][j] == 0 and personas[j] == "1") or (statements[i][j] == 1 and personas[j] == "0"):
                        return False
                    
            #si llego hasta aca es porque esta todo bien, entonces devuelvo True
            return True
        
        
        for num in range(1<<n , 1<<(n+1)): # para obtener todas las combinaciones el rango tiene que ser ese
            personas = bin(num)[3:] # el bin te deja un 0b adelante entonces lo borramos, tambien borramos el 1 del principio que pusimos
            if check(personas):
                res = max(res, personas.count("1"))
        return res

