print()
print("중첩리스트")
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
