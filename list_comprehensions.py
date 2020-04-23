# https://www.hackerrank.com/challenges/list-comprehensions/problem

#x = int(raw_input())
#y = int(raw_input())
#n = int(raw_input()) 
#ar = []
#p = 0 

#for i in range(x + 1):
#    for j in range(y + 1):
#        if i + j != n:
#            ar.append([])
#            ar[p] = [ i , j ]
#            p+=1 
#            print(ar)

#x = int(raw_input())
#y = int(raw_input())
#n = int(raw_input())
#print [[i, j] for i in range(x + 1) for j in range(y + 1) if ((i + j) != n )] 

x, y, z, n = 1, 1, 1, 2

print([
    [i, j, k] 
    for i in range(x + 1) 
    for j in range(y + 1) 
    for k in range(z + 1) 
    if ((i + j + k) != n)
    ])

x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])