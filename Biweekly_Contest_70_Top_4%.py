#BIWEEKLY CONTEST 70

# 663 / 17655
from typing import List # tmb se puede usar list en vez de List sin necesidad de importar
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost = cost[::-1]
        res = 0
        for i in range(len(cost)):
            if i % 3 == 0 or i%3 == 1:
                res+=cost[i]
        return res

class Solution:
    def numberOfArrays(self, dif: List[int], lower: int, upper: int) -> int:
        minimo = dif[0]
        maximo = dif[0]
        cur = dif[0]
        for i in range(1, len(dif)):
            cur += dif[i]
            if cur < minimo:
                minimo = cur
            elif cur > maximo:
                maximo = cur
        #print(minimo)
        #print (maximo)
        arriba = min(upper, upper-maximo)
        abajo = max(lower, lower-minimo)
        if arriba == abajo: return 1
        elif arriba < abajo: return 0
        else:
            return arriba-abajo+1

from collections import deque
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        q = deque()
        row, col = start
        low, high = pricing
        res = []
        m = len(grid)
        n = len(grid[0])
        #agrego al comienzo con distancia 0 a la cola y lo pongo si cumple la condicion 
        if grid[row][col] == 0:
            return []
        elif low<=grid[row][col]<= high:
            q.append((0, grid[row][col], row, col))
            res.append([row, col])
            k-=1
        else:
            q.append((0, grid[row][col], row, col))
        #hago bfs por nivel
        qq = deque() #este seria el proximo nivel
        vis = [[False] * (n) for _ in range(m)]
        sirve = []
        while q: 
            for dis, value, row, col in q:
                vis[row][col] = True
                #para cada uno de los de la cola
                for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                    if 0<=row+dx<=m-1 and 0<=col+dy<=n-1:
                        if not vis[row+dx][col+dy] and grid[row+dx][col+dy] != 0:
                            vis[row+dx][col+dy] = True
                            if low <= grid[row+dx][col+dy] <= high:
                                sirve.append((dis+1, grid[row+dx][col+dy], row+dx, col+dy))
                            qq.append((dis+1, grid[row+dx][col+dy], row+dx, col+dy))
            sirve.sort(key = lambda element: element[0:4])
            q = deque()
            while k > 0 and sirve:
                dis, value, row, col = sirve[0]
                sirve.pop(0)
                res.append([row,col])
                k-=1
            if k==0:
                return res
            while qq:
                dis, value, row, col = qq.popleft()
                q.append((dis, value, row, col))
            qq = deque()
            
            
        
        return res


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count = 0
        for i,c in enumerate(corridor):
            if c == "S":
                count+=1
                if count == 2:
                    indexInicio = i
        if count % 2 == 1 or count == 0: return 0
        if count == 2: return 1
        #sabemos que hay numero par de asientos mayor o igual a 4
        count = count-2 #bajamos 2 asientos porque ya sabemos a partir de q indice estan
        res = 1
        lugares = 1
        buscandoSilla = False
        for i in range(indexInicio+1, len(corridor)):
            if not buscandoSilla:
                if corridor[i] == "P":
                    lugares +=1
                else:
                    count-=1
                    res *= lugares
                    if count == 1:
                        return res % (10**9+7)
                    lugares = 1
                    buscandoSilla = True
            else:
                if corridor[i] == "S":
                    count-=1
                    buscandoSilla = False
                

        return res % (10**9+7)        
