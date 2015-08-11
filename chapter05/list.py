print()
print("***************중첩리스트**********************")
s = [1, 2, 3]
t = ['begin', s, 'end']
print(t)
print(t[1][1])
s[1] = 100
print(t)

print()
L = [1, ['a', ['x', 'y'], 'b'], 3]
print(L[1])
print(L[1][1])
print(L[1][1][1])
print()

print("********************리스트 메서드***************")
s = [1, 2, 3]
s.append(5)
print(s)
s.insert(3, 4)
print(s)
print(s.index(3))
print(s.count(2))
s.reverse()  # 반환값이 없다
print(s)
s.sort()  # 반환값이 없다.
print(s)
s = [10, 20, 30, 40, 50]
s.remove(10)
print(s)
s.extend([60, 70])

print()
print("리스트를 스택으로 사용하기")
s = [10, 20, 30, 40, 50]
s.append(60)
print(s)
s.pop()
print(s)
print()
s.pop(0)
print(s)
s.pop(1)
print(s)
print()
print("리스트를 큐로 사용하기")
s = [10, 20, 30, 40, 50]
s.append(60)
print(s)
s.pop(0)
print(s)

print()
print("***********리스트에 튜플이나 리스트가 있을때 반복 참조하기**********")
print()
print("***************리스트 정렬하기***************************")
L = [1, 5, 3, 9, 8, 4, 2]
L.sort()
print(L)
L.sort(reverse= True)
print(L)
print()
L = 'Python is a Programming Language'.split()
print(L)
L.sort()
print(L)
L.sort(key=str.lower)
L
print(L)
L.sort(key=str.lower, reverse=True)
print(L)
print()
L = ['123', '34', '56', '2345']
L.sort()
print(L)
L.sort(key=int)
print(L)
def mykey(a):
    return a%3
L = [1, 5, 3, 9, 8, 4, 2]
L.sort(key=mykey)
print(L)
def mykey(a):
    return (a%3, a)
L = [1, 5, 3, 9, 8, 4, 2]
L.sort(key=mykey)
print(L)
print()
print("람다함수")
L = [1, 5, 3, 9, 8, 4, 2]
L.sort(key=lambda a : (a%3, a))
print(L)

print("sorted()함수를 사용한 정렬")
print()
L = [('lee', 5, 38), ('kim', 3, 28), ('jung', 10, 36)]
L.sort(key= lambda a : a[2])
print(L)

print()
L = [1, 6, 3, 8, 6, 2, 9]
newList = L.sort() # 반환값은 없다.
print(newList)

L = [1, 6, 3, 8, 6, 2, 9]
newList = sorted(L)
print(newList)

for ele in sorted(L):
    print(ele, end='  ')

print()
L = [1, 6, 3, 8, 6, 2, 9]
print(sorted(L, reverse=True))
L = ['123', '34', '56', '2345']
print(sorted(L, key=int))

d = {'one':1, 'two':2, 'three':3, 'four':4}
print(sorted(d))

for key in sorted(d):
    print(key)

print()
d = {'one':1, 'two':2, 'three':3, 'four':4}
for key in sorted(d, key=lambda  a : d[a]):
    print(key)

print()
print(sorted(d.items(), key=lambda a:a[1]))

print()
print("revered()함수를 사용한 정렬")
L = ['2345', '56', '34', '123']
print(L)
for ele in reversed(L):
    print(ele)


