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
