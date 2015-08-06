# copy 모듈

import copy

a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = copy.copy(x)  # 얕은 복사

print(x)
print(y)

a[0] = 99

print(x)
print(y)

# 다시 원복
print()
a[0] = 1

print(x)
print(y)

y = copy.deepcopy(x)

print()
print(x)
print(y)

a[0] = 99

print(x)
print(y)

print()
a = ['hello', 'world']
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

print()
c = copy.deepcopy(a)
print(a is b)
print(a[0] is c[0])

print()
L = [1, 2, 3, 4, 5]
M = L[1:4]

L[1] = 200
print(L)
print(M)