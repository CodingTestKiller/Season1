import sys
from itertools import combinations

def invalidPosition(pos1,pos2):
    if abs(pos1[0]-pos2[0])==0 and abs(pos1[1]-pos2[1])<3:
        return True
    if abs(pos1[0]-pos2[0])==1 and abs(pos1[1]-pos2[1])<2:
        return True
    if abs(pos1[0]-pos2[0])==2 and abs(pos1[1]-pos2[1])<1:
        return True
    return False

def calcBudget(pos1):
    return graph[pos1[0]][pos1[1]]+graph[pos1[0]+1][pos1[1]]+graph[pos1[0]-1][pos1[1]]+graph[pos1[0]][pos1[1]+1]+graph[pos1[0]][pos1[1]-1]

N=int(sys.stdin.readline())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
position=[[x,y] for x in range(1,N-1) for y in range(1,N-1)]
minBudget=3001

for pos in combinations(position,3):
    if invalidPosition(pos[0],pos[1]) or invalidPosition(pos[1],pos[2]) or invalidPosition(pos[2],pos[0]):
        continue

    minBudget=min(minBudget,calcBudget(pos[0])+calcBudget(pos[1])+calcBudget(pos[2]))

print(minBudget)