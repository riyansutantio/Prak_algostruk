def buatNol(n,m=None):
    if(m==None):
        m=n
    print("membuat matriks 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for j in range(m)] for i in range(n)])

def buatIdentitas(m):
    for i in range(0,m):
        for j in range(0,m):
            if (i==j):
                print('1',end=" ")
            else:
                print('0',end=" ")
        print()
buatNol(4,4)
buatNol(3)
buatIdentitas(4)
