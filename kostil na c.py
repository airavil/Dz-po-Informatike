n=2000
M=[]
for i1 in range(n//1023+1):
    for i2 in range(n//511+1):
        for i3 in range(n//255+1):
            for i4 in range(n//127+1):
                for i5 in range(n//63+1):
                    for i6 in range(n//31+1):
                        for i7 in range(n//15+1):
                            for i8 in range(n//7+1):
                                for i9 in range(n//3+1):
                                    I = i1*1023+i2*511+i3*255+i4*127+i5*63+i6*31+i7*15+i8*7+i9*3
                                    if I <= n:
                                        M.append(I)
M[0]=1
print(M)