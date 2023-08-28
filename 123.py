L = []
for i in range(3):
    L.append([int(x) for x in input().split()])

m = 1
M = []
Y = []

# 計算 m，也就是三個餘數的乘積
for i in L:
    m *= i[0]

# 計算 M，即 m 除以各個餘數的商
for i in L:
    M.append(m // i[0])

# 計算 Y，找到滿足 M[i] * Y[i] % L[1][0] == 1 的 Y[i]
for i in range(3):
    j = 1
    while M[i] * j % L[1][0] != 1:
        j += 1
    Y.append(j)

# 使用韓信點的定理計算最小正整數解
x = L[0][0] * M[0] * Y[0] + L[1][0] * M[1] * Y[1] + L[2][0] * M[2] * Y[2]

# 輸出結果
print(x % m)
