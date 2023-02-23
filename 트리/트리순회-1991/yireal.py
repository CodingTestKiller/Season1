from sys import stdin
from collections import deque
inp = stdin.readline
n = int(inp().rstrip())
def build_pre(pre_order,ver,left,right):
    index = pre_order.index(ver)
    if(right != '.'):
        pre_order.insert(index+1,right)
    if(left != '.'):    
        pre_order.insert(index,left)
def build_in(in_order,ver,left,right):
    index = in_order.index(ver)
    if(right != '.'):
        in_order.insert(index+1,right)
    if(left != '.'):
        in_order.insert(index+1,left)
def build_post(post_order,ver,left,right):
    index = post_order.index(ver)
    if(right != '.'):
        post_order.insert(index,right)
    if(left != '.'):
        post_order.insert(index,left)
pre_order = []
in_order = []
post_order = []
for i in range (n):
    ver,left,right = inp().rstrip().split()
    if(left == '.' and right == '.') : continue
    if ver not in pre_order:
        pre_order.append(ver)
        in_order.append(ver)
        post_order.append(ver)
    build_pre(pre_order,ver,left,right)
    build_in(in_order,ver,left,right)
    build_post(post_order,ver,left,right)
print(*in_order,sep='')    
print(*pre_order,sep='')
print(*post_order,sep='')