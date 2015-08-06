# 수치자료형

print('***************# 1. 정수형 상수******************')
a = 23
print(type(a))
print(isinstance(a, int))

b = 0o23
c = 0x23
d = 0b1101
print(a, b, c, d)
print(2**1024)
n = 2**1024
print(n.bit_length())

print()
print('# 10진수가 아닌 것을 10집수로 변환 : int()')
print('# 10진수를 2진수 8진수 16진수로 변환')
print(int('123', 5))
print(bin(23))
print(oct(23))
print(hex(23))

print()
print('#다른 자료형으로부터 정수얻기')
print(int(2.9))
print(int(-2.9))
print(int('123'))
# print(int('123.4')) #정수변환안됨
print(float('123.4'))
# print(int(2+3j))    #복소수도 직접 정수전환 안됨

print()
print('#정수형 데이터를 다른 수치 자료형으로 변환')
a = 123
print(float(a))
print(str(a))
print(complex(a))

print()
print('#정수형을 바이트열로 변환')
e = 1024
f = -1024
print(e.to_bytes(2, 'big'))
print(e.to_bytes(2, 'little'))
print(f.to_bytes(4, 'big', signed=True))

print()
print('#바이트열을 정수형으로 변환')
print(int.from_bytes(b"\x04\x00", 'big'))
print(int.from_bytes(b'\x00\x04', 'little'))
print(int.from_bytes(b'\x00\x00\x04\x00', 'big'))
print(int.from_bytes(b'\xff\xff\xfc\x00', 'big', signed=True))
print(int.from_bytes([4, 0], 'big'))


print()
print("*****************************************")
print('#실수형 상수')
a = 1.2
print(type(a))
print(isinstance(a, float))
b = 3e3
c = -0.2e-4
print(a, b, c)

print()
print('#sys 모듈')
import sys
print(sys.float_info)
print(sys.float_info.max)
print(sys.float_info.min)

print()
print('무한대')
print(float('inf'))
print(float('-inf'))
infinity = float('inf')
print(infinity/1000)

print()
print('실수형인 경우 오차없이 정수로 표현할 수 있는가?')
a = 1.2
print(a.is_integer())
a = 2.0
print(a.is_integer())

print()
print('#반올림, 올림, 내림')
print(round(1.2))
print(round(1.8))
import math
print(math.ceil(1.2))
print(math.floor(1.2))

print()
print('#복소수형 상수')
c = 4 + 5j
d = 7 - 2j
print(c*d)
print(c.real)
print(c.imag)
a = 3
b = 4
print(complex(a, b))
print(c.conjugate())

print()
print("# cmath 모듈")
import cmath
print(cmath.sin(0.1 + 0.2j))
print(cmath.sqrt(-2))
print(cmath.log(2j))

print()
print('*******************************# fraction 모듈- 분수 을 사용해서 분수표현하기')
from fractions import Fraction
print(Fraction('5/7'))
print(Fraction(5, 7))
print(Fraction(123))
print(Fraction('1.414213'))
print(Fraction(1.1))
print(Fraction(1, 2) + Fraction(1, 2))
print(Fraction(39, 35))

print()
print('********************************# decimal 모듈 - 소수')
from decimal import *
print(Decimal(1234))
print(Decimal('1234'))
print(Decimal(1.1))
print(Decimal('1.1'))
print(Decimal('Infinity'))
print(Decimal('-Infinity'))
print(Decimal('NaN'))
e = Decimal('0.0')
delta = Decimal('0.1')
for k in range(1000):
    e += delta
print(e)

print()
a = Decimal('35.72')
b = Decimal('1.73')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  # 몫
print(a % b)  # 나머지
print(a**b)  # 자승

print()
a = Decimal('35.72')
print(a+2)
print("# print(a+3.2) 와 같이 Decimal과 실수와의 연산은 안된다.")

print()
import math
import cmath
d = Decimal("123.456789012345")
print(math.sqrt(d))
print(cmath.sqrt(-d))

print()
getcontext().prec = 38
print(Decimal('2').sqrt())
getcontext().prec = 28
print(Decimal('2').sqrt())
print(Decimal(2).exp())
print(Decimal('10').ln())
print(Decimal('10').log10())
print(Decimal('7.329').quantize(Decimal('.01'), rounding=ROUND_DOWN))
print(Decimal('7.321').quantize(Decimal('1.12'), rounding=ROUND_UP))
print(Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_HALF_UP))

print()
print(Decimal((1, (1, 4, 7, 5), -2)))


print()
print(" ** # context 객체 - decimal 객체의 연산에 필요한 계산정확도와 반올림방법을 지정")
print(getcontext())
print(Decimal(1)/Decimal(7))
getcontext().prec = 3
print(Decimal(1)/Decimal(7))

print()
print("decimal 모듈은 Context 객체 3가지를 제공")
print(ExtendedContext)
print(BasicContext)
print(DefaultContext)
print()
print("setcontext()를 사용하여 설정변경가능")
setcontext(ExtendedContext)
print(Decimal(1)/Decimal(7))
setcontext(DefaultContext)
print(Decimal(1)/Decimal(7))
setcontext(BasicContext)
print(Decimal(1)/Decimal(7))

print("****************수치자료형 종료*********************")

print()
print()
print("*****************수치연산자*****************")
print("1. 산술연산자 : + - * / // ** % ")
print()
print(5/2)
print(5//2)
print(5 % 2)
print(divmod(5, 2))
print(2**3)
print(2**3**2)
print((2**3)**2)
print()
print("파이썬의 나머지는 제수의 부호와 같다")
print(5 % 3)
print(5 % -3)
print(-5 % 3)
print(-5 % -3)

print()
print("따라서 몫은 다음과 같아진다")
print(5//3)
print(5//-3)
print(-5//3)
print(-5//-3)

print()
print("산술연산자의 우선순위")
print("단항연산자(오에서왼) -> **(오에서왼) -> * / // % -> + -")
print(++3)
print(--3)
print(-+3)
print(+-3)

print()
print(4/2 * 2)

print()
print(2**3**4)  # 오에서 왼 주의

print()
print("2. 관계연산자 : > < >= <= == !=")
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)

print()
print("3. 논리연산자 : and or nor")
a = 20
b = 30
print(a > 10 and b < 50)

print()
print("any() all()")
bool_list = [True, True, False]
print(all(bool_list))
print(any(bool_list))

print()
print("내장수치연산함수")
print(abs(-3))
print(int(3.141592))
print(int(-3.141592))
print(float(5))
print(complex(3.4, 5))
print(complex(6))
c = complex(2, 3)
print(c.conjugate())
print(divmod(5, 2))
print(pow(2, 3))
print(pow(2.3, 3.5))
print(max([1, 3, 5, 2, 7]))
print(sum([1, 3, 5, 2, 7]))

print()
import math
print(math.pi)
print(math.e)
print(math.sin(0.1))
print(math.sqrt(2))