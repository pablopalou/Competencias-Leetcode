#Biweekly_Contest_71_Top_8%
from typing import List

#Ejercicio 1 ---- 5:03 
def minimumSum(self, num: int) -> int:
    numero = str(num)
    nums = []
    for i, n in enumerate(numero):
        nums.append(int(n))
    nums.sort() 
    
    num1 = nums[0]*10 + nums[2]
    
    num2 = nums[1]*10 + nums[3]
    
    return num1+num2

#Ejercicio 2 ---- 11:31 total 
def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        nums2 = [0]*(n)
        pos = 0
        for i in range(n):
            if nums[i] < pivot:
                nums2[pos] = nums[i]
                pos+=1
        for i in range(n):
            if nums[i] == pivot:
                nums2[pos] = nums[i]
                pos+=1
        for i in range(n):
            if nums[i] > pivot:
                nums2[pos] = nums[i]
                pos+=1
                
        nums = nums2
        return nums

#Ejercicio 3 ---- 43:39 total (2 WS)
def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        #sol1 es la de poner las cosas reales
        #sol2 es la de poner mas q 60 segunods
        #los 0 de adelante no los apreto nunca
        sol1 = sol2 = 0
        startAt2 = startAt
        minutes, seconds = targetSeconds//60, targetSeconds % 60
        #print(minutes, seconds)
        #ver el caso de tener 0 minutos y menos de 10 segundos
        sol = 0
        if minutes !=100:
            if minutes == 0:
                if seconds>10:
                    if startAt != seconds//10:
                        sol+= moveCost+pushCost
                        startAt = seconds//10
                    else:
                        sol+= pushCost
                    if startAt != seconds%10:
                        sol+= moveCost+pushCost
                        startAt = seconds%10
                    else:
                        sol+= pushCost
                else:
                    if startAt != seconds%10:
                        sol+= moveCost+pushCost
                        startAt = seconds%10
                    else:
                        sol+= pushCost
                return sol

            if minutes < 10:
                #print("minutes < 10")
                if startAt != minutes:
                    sol1+= moveCost+pushCost #muevo y apreto los minutos
                else: #solo tengo q apretar
                    sol1+= pushCost
                startAt = minutes #actualizo el ultimo numero apretado
            else: #dos cifras de minutos
                #print("minutes >= 10")
                if startAt != minutes//10:
                    sol1+= moveCost+pushCost
                    startAt = minutes//10
                else:
                    sol1+= pushCost #no me tengo que mover
                #print("Despues de el primer numero de los minutos sube sol1 a:", sol1)
                #ahora veo el segundo numero de los minutos
                if startAt != minutes%10:
                    sol1+= moveCost+pushCost
                    startAt = minutes%10
                else:
                    sol1+= pushCost #no me tengo que mover   
                #print("Despues de el segundo numero de los minutos sube sol1 a:", sol1)
            #ahora veo los segundos

            #los segundos los tengo que apretar igual
            if startAt != seconds//10:
                sol1+= moveCost+pushCost
                startAt = seconds//10
            else:
                sol1+= pushCost #no me tengo que mover
            #ahora veo el segundo numero de los segundos
            if startAt != seconds%10:
                sol1+= moveCost+pushCost
                startAt = seconds%10
            else:
                sol1+= pushCost #no me tengo que mover
        
        if seconds>=40: return sol1
        startAt = startAt2
        minutes = minutes-1
        seconds = seconds+60
        #print(minutes, seconds)
        if minutes == 0:
            if seconds>10:
                if startAt != seconds//10:
                    sol+= moveCost+pushCost
                    startAt = seconds//10
                else:
                    sol+= pushCost
                if startAt != seconds%10:
                    sol+= moveCost+pushCost
                    startAt = seconds%10
                else:
                    sol+= pushCost
            else:
                if startAt != seconds%10:
                    sol+= moveCost+pushCost
                    startAt = seconds%10
                else:
                    sol+= pushCost
            return min(sol, sol1)
        if minutes < 10:
            if startAt != minutes:
                sol2+= moveCost+pushCost #muevo y apreto los minutos
            else: #solo tengo q apretar
                sol2+= pushCost
            startAt = minutes #actualizo el ultimo numero apretado
        else: #dos cifras de minutos
            if startAt != minutes//10:
                sol2+= moveCost+pushCost
                startAt = minutes//10
            else:
                sol2+= pushCost #no me tengo que mover
            #ahora veo el segundo numero de los minutos
            if startAt != minutes%10:
                sol2+= moveCost+pushCost
                startAt = minutes%10
            else:
                sol2+= pushCost #no me tengo que mover   
        #ahora veo los segundos
        #dos cifras de segundos
        if startAt != seconds//10:
            sol2+= moveCost+pushCost
            startAt = seconds//10
        else:
            sol2+= pushCost #no me tengo que mover
        #ahora veo el segundo numero de los segundos
        if startAt != seconds%10:
            sol2+= moveCost+pushCost
            startAt = seconds%10
        else:
            sol2+= pushCost #no me tengo que mover
        #print(sol1, sol2)
        if minutes == 99: return sol2
        return min(sol1, sol2)

#Ejercicio 4 dio TLE 
from itertools import combinations
def minimumDifference(self, nums: List[int]) -> int:
    n = len(nums) // 3
    m = len(nums)
    if n == 1:
        return min(nums[0]-nums[1],nums[1]-nums[2], nums[0]-nums[2])

    comb = combinations(range(m), n)
    minimo = float("inf")
    cont = cont2 = first = second = 0
    agregarSegundo = False
    
    for i in comb:
        s = set(i)
        #print(s)
        cont = 0
        cont2 = 0
        agregarSegundo = False
        first = 0
        second = 0
        for j, num in enumerate(nums):
            #print(j)
            if j in s:
                continue
            else:
                #rint("entro")
                if not agregarSegundo:
                    first += num
                    #print("first ", first)
                    cont+=1
                    if cont==n:
                        #print("agrego Segunod")
                        agregarSegundo = True
                else:
                    second += num
                    #print("second", second)
                    cont2+=1
                    if cont2 == n:
                        #print("actualizo quiza:",first-second)
                        minimo = min(minimo, first-second)
                    
    return minimo

#Ejericio 4 Accepted post contest
#O(n log(n)) using priority queues
import heapq
def minimumDifference(self, nums: List[int]) -> int:
        #la solucion pro es de N log N
        n = len(nums) // 3
        left_part = [-n for n in nums[0:n]]
        right_part = nums[-n:]
        heapq.heapify(left_part)
        heapq.heapify(right_part)
        
        min_left_part = [0] * (n+1)
        max_right_part = [0] * (n+1)
        min_left_part[0] = -sum(left_part)
        max_right_part[-1] = sum(right_part)
        
        for i in range(1,n+1):
            num = nums[n+i-1]
            heapq.heappush(left_part, -num)
            pn = -heapq.heappop(left_part)
            min_left_part[i] = min_left_part[i-1] + (num-pn)
            
        for i in range(n-1,-1,-1):
            num = nums[n+i]
            heapq.heappush(right_part, num)
            pn = heapq.heappop(right_part)
            max_right_part[i] = max_right_part[i+1] + (num-pn)
            
        ans = float('inf')
        for i in range(n+1):
            ans = min(ans, min_left_part[i] - max_right_part[i])
        return ans
