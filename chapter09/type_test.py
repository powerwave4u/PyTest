# 수치형변환


# 정수형으로 변환
print(int('1234'))
print(int(4.56))
# print(int('12.34')) 에러남

print()
# 실수형에서 정수로 변환하기 - int()
print(int(1.1))
print(int(1.9))
print(int(-1.1))
print(int(-1.9))

print()
# - round() 반올림
print(round(1.1))
print(round(1.9))
print(round(-1.1))
print(round(-1.9))
# -자리수 지정
print(round(1.23456, 3))
print(round(12375, -2))  # ???


print()
# math 모듈 -floor()
import math
print(math.floor(1.1))
print(math.floor(1.9))
print(math.floor(-1.0))
print(math.floor(-1.1))
print(math.floor(-1.9))

print()
# - ceil()
print(math.ceil(1.0))
print(math.ceil(1.1))
print(math.ceil(1.9))
print(math.ceil(-1.0))
print(math.ceil(-1.1))
print(math.ceil(-1.9))

# 실수형으로 변환 -float()
print()
print(float('1234'))
print(float('12.34'))
print(float(1234))

# 복소수로 변환 - complex()
print()
print(complex(1))
print(complex(1, 3))
print(complex(0, 3))
print(3*1j)  # ???

# ========================================================
# 진수변환 -임의의 수를 10진수로 변환
print()
print(int('64', 16))
print(int('144', 8))
print(int('101111', 2))
print(int('14', 5))

# 10진수를 임의의 진수로 변환
print()
print(hex(100))
print(oct(100))
print(bin(100))

print()
print("{0:x}".format(100))
print("{0:o}".format(100))
print("{0:b}".format(100))

# =================================================
# 시퀀스형으로의 변환 - list() tuple()
print()
t = (1, 2, 3, 4)
l = [5, 6, 7, 8]
s = 'abcd'

print(list(t))
print(list(s))
print(tuple(l))
print(tuple(s))

# 사전에서 리스트로 변환
print()
d = {1:'one', 2:'two', 3:'three'}
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

# 리스트에서 사전으로 변환
print()
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
print(dict(zip(keys, values)))

# ==============================================
# 문자열로의 변환 -str() -repr() -eval()

print()
print(str([1, 2, 3]), str((4, 5, 6)), str('abc'))
print(repr([1, 2, 3]), repr((4, 5, 6)), repr('abc'))
print(eval('[5, 6, 7, 8]')) # eval()

print()
x = 1
print(eval('x + 1'))

print()
a = {1: 'one', 2: 'two'}
b = repr(a)
print(b)
print(type(b))

c = eval(b)
print(c)
print(type(c))

# 유니코드와 문자간 변환 -chr() : 유니코드에서 문자로
print()
print(chr(97))
print(chr(44032))
print()

# 문자에서 유니코드로 - ord()
print(ord('a'))
print(ord("가"))


# 문자열과 바이트의 변환 - encode() decode()
b = b'bytes'
print(type(b))
print(b.decode('utf-8'))
print()

s = 'string'
print(s.encode('utf-8'))

# 이진바이트열과 16진 바이트열
print()
print(hex(ord('a')))
import binascii
print(binascii.hexlify(b'abc'))

print()
buf = bytearray(b'abcde')
print(binascii.hexlify(buf))
print(binascii.unhexlify(b'6162636465'))

# 정수를 쉽표가있는 문자열로 변환
print()
print(format(123456789, ','))
print("{:,} {:,}".format(10030405, 12345))
print("{0:,} {1:,}".format(10030405, 12345))

# locale 모듈
print()
import locale
locale.setlocale(locale.LC_ALL, "")
print(locale.format("%d", 10030405, grouping=True))

print()
# 파이썬 데이터를 바이트열로 변환하기
from struct import *
print(pack('hhl', 1, 2, 3))
print(pack('2hl', 1, 2, 3))

print()
print(pack('d6s', 3.14, b'python'))
print(pack('d7s', 3.14, b'python'))

print()
buf = bytearray(b'\0'*8)
offset = 0
pack_into('hhl', buf, offset, 1, 2, 3)
print(buf)
print(bytes(buf))
import binascii
print(binascii.hexlify(buf))

print(calcsize('d 8s'))

print()
# C 바이트열을 파이썬 데이터로 변환
from struct import *
s = pack('hhl', 1, 2, 3)
print(unpack('hhl', s))

s = pack('d 6s', 3.14, b'python')
print(unpack('d 6s', s))

buf = bytearray(b'\0'*20)
pack_into('hhl', buf, 5, 1, 2, 3)
print(unpack_from('hhl', buf, 5))
print(unpack_from('hhl', buf)) #해독 애러

print()
print(calcsize('h'))
print(calcsize('hh'))
print(calcsize('i'))
