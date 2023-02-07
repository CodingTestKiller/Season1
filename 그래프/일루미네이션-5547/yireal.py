import sys
inp = sys.stdin.readline
w,h = map(int,inp().rstrip().split())
field = [list(int(inp().rstrip())) for i in range(h)]
sizeofgraph = sum(field)
ran_even = [(-1,-1),(0,-1),(1,0),(0,1),(-1,1),(1,0)]
ran_odd = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,0)]
graph = [(x,y) for x in range(w) for y in range(y) if field[x][y] == 1]
for (x,y) in graph:
    
    

