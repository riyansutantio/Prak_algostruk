h = [[1,2],[3,4]]
g = [[1,2],[3,4]]
y = [[1,2,3],[3,4,6],[5,2,6]]
l = []
def pastikan(h):
    z = 0
    a = len(h[0])
    for i in range (len(h)):
        if (len(h[i])==a):
            z+=1
    if (z==len(h)):
        print("matriks konsisten")
    else:
        print("matriks tidak konsisten")
def ambil(h):
    print (len(h[0]),"x",len(h))

def penjumlahan(h):
    for x in range (0,len(h)):
        for y in range (0,len(h[0])):
            print ( h[x][y]+g[x][y],end=" ")
        print()

def perkalian(obj):
    for x in range(0, len(h)):
        row = []
        for y in range(0, len(h[0])):
            total = 0
            for z in range(0, len(h)):
                total = total + (h[x][z] * g[z][y])
            row.append(total)
        l.append(row)

    for x in range(0, len(l)):
        for y in range(0, len(l[0])):
            print (l[x][y], end=' ')
        print ()

def determinan(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    return total

	
ambil(h)
ambil(y)
pastikan(h)
pastikan(y)
penjumlahan(h)
perkalian(h)
determinan(h)
