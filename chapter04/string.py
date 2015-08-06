print()
print("*************시퀀스 문자열 : 문자열 / 리스트 /튜플**************************")
print("특징 : 인덱싱, 슬라이싱, 연결, 반복 멤버검사 길이정보")

print()
print("인텍싱")
s = 'abcdef'
l = [100, 200, 300]
print(s[0])
print(s[1])
print(s[-1])
print(l[1])
l[1] = 900  # 치환
print(l)

print()
print("슬라이싱")
s = 'abcdef'
L = [100, 200, 300]
print(s[1:3])
print(s[1:])
print(s[:])
print(s[-100:100])
print(L[:-1])
s = "abcd"
print(s[::2])
print(s[::-1])

print()
print("연결하기")
s = 'abc' + 'def'
print(s)
L = [1, 2, 3] + [4, 5, 6]
print(L)

print()
print("반복하기")
s = 'Abc'
print(s*4)
L = [1, 2, 3]
print(L*4)

print()
print("멤버검사")
print('파' in '파이썬')
t = (1, 2, 3, 4, 5)
print(2 in t)
print(10 not in t)

print()
print("길이정보")
s = '파이썬만세'
print(len(s))
L = [1, 2, 3]
print(len(L))

print()
print()
print("*********문자열 정의하기*********")
print()
print("- 한줄 문자열")
s = ''
str1 = 'Puthon is great!'
str2 = 'Yes, it is.'
str3 = "It's not like any other langages"
print(type(s))
print(isinstance(s, str))
str4 = 'Don\'t walk. "Run"'
print(str4)
long_str = "This is a rather long string  \
containing back slash and new line. \nGood!" # 다음줄에 이어서 작성시 사용 \
print(long_str)

print()
print("- 여러줄 문자열 - 작은 따옴표나 큰 따옴표를 세번 연속사용")
multiline = """만일 우리에게 겨울이 없다면 봄은 그토록 즐겁지 않을 것이다.
우리들이 이따금 역경을 맛보지 않는다면 성공은 그토록 환영받지 못할 것이다."""
print(multiline)

print()
print("- 특수문자")
a = \
2
print(a)
print('abc\tdef\tghi')
print('a\nb\nc')

print()
print("문자열 연산")
s1 = '첫 문자열'
s2 = '두번째 문자열'
s3 = s1 + ' ' + s2
print(s3)
print(s1 * 3)
print(s1[2])
print(s1[1:-1])
print(len(s1))
print('문자' in s1)
str1 = 'abcdef'
# print(str1[0] = 'f')  문자열은 변경불가능 자료형임
for c in '파이썬만세':  # 문자열이 시퀀스형으로 for 문에 적용되면 각 문자에 대해 반복
    print(c, end=' ')
print()
s = 'spam and egg'
s = s[:5] + 'cheese ' + s[5:]
print(s)

print()
print("*****문자열의 서식 지정하기********")
print("format() 함수 사용")
int_val = 23
float_val = 2.34567
print(format(int_val, '3d'), format(float_val, '.2f'))
print(format(123456789, ',d'))  # 중요
print(format(1234567.89, ',.2f'))
print()
print("format() 메서드")
print('{} {}'.format(23, 2.12345))
L = [1, 5, 3, 7, 4, 5]
print('최대값 : {0}, 최소값 : {1}'.format(max(L), min(L)))
print()
print('sqrt({:3}) = {:0.5}'.format(2, 2**0.5))
print('sqrt({0:3}) = {1:0.5}'.format(2, 2**0.5))
print('sqrt({0:3d}) = {1:0.5f}'.format(2, 2**0.5))
print('sqrt({:3d}) = {:0.5f}'.format(2, 2**0.5))
print('{:,d}'.format(123456789))
print('{:,.2f}'.format(123456789.0123))
print()
L = [0, 1, 1, 2, 3, 5, 8, 13, 21]
print('next value of {0[4]} is {0[5]}'.format(L))
print('나이:{age} 키:{height}'.format(age=49, height=173))
info = {'size': 32, 'height': 173, 'age': 49}
print('나이:{age}, 키:{height}'.format_map(info))

print()
import sys
print(sys.float_info.max)
print('실수 최대값 : {0.float_info.max}'.format(sys))  # 0.float_info.max는 sys.float_info.max를 가리킴
print('{0.__doc__}'.format(list))

print()
from math import sin, pi, radians
for deg in range(0, 361, 10):
    rad = radians(deg)
    print('sin({0:3d}) = {1:10.5f}'.format(deg, sin(rad)))

print()
print("수치변환기호")
import locale
print(locale.setlocale(locale.LC_ALL, ''))
# 2진수 10진수 8진수 16진수 16진수, 10진수(d), 10진수(n)
print('{0:b} {0:d} {0:o} {0:x} {0:X} {1:d} {1:n}'.format(13, 123456789))
print('{0:e} {0:E} {0:f} {0:F}'.format(0.6789))
print('{1:g} {1:G} {1:n} {0:%}'.format(0.6789, 123E30))

print()
print("**********************문자열 메소드***********************")
print("1. 대소문자 변환")
s = 'i like programming'
print(s.upper())
print(s.lower())
print('I Like Programming'.swapcase())
print(s.capitalize())
print(s.title())

print()
print("2. 검색메소드")
s = 'i like programming, i like swimming.'
print(s.count('like'))
print(s.find('like'))
print(s.find('like', 3))
print(s.find('my'))  # 없을때는 -1반환
print(s.rfind('like'))

print()
print(s.index('like'))
# print(s.index('my')) // index 함수는 find와 같지만 값이 없을때 애러발생
print(s.rindex('like'))
print(s.startswith('i like'))
print(s.endswith('swimming.'))
print(s.startswith('progr', 7))
print(s.endswith('l like', 0, 26))

print()
print("3. 편집과 치환")
u = ' spam and ham '
print(u.strip())
print(u.rstrip())
print(u.lstrip())
print(' abc'.strip())
print('><><abc<><><>'.strip('<>'))
print('><><abc<><><>\n'.strip('<>'))
print('ㅎㅎ 파이썬 만세 ㅎㅎ'.strip('ㅎ'))
print(u.replace('spam', 'spam, egg'))

print()
print("4. 문자열의 분리와 결합")
u = ' spam and ham'
print(u.split()) # 공백으로 분리
print(u.split('and'))
t = u.split()
print(':'.join(t))
print('\n'.join(t))
lines = '''first line
second line
third line'''
print(lines.splitlines())
s = 'one:two:three:four'
print(s.split(':', 2))
print(s.rsplit(':', 1))

print()
print("5. 정렬")
u = 'spam and egg'
print(u.center(60, '-'))
print(u.ljust(60, '-'))
print(u.rjust(60, '-'))
print('1\tand\t2'.expandtabs())
print('1\tand\t2'.expandtabs(4))

print()
print("6. 숫자 문자 문자열 구별")
print('1234'.isdigit())
print('123\u2155\u2156')
print('123\u2155\u2156'.isnumeric())
print('123\u0661')
print('123\u0661'.isdecimal())
print('abcd한글'.isalpha())
print('1abc234'.isalnum())
print('abc'.islower())
print('ABC'.isupper())
print(' \t\r\n'.isspace())
print('This Is A Title'.istitle())
print(' \n\t'.isspace())
print('def'.isidentifier())
print(' \n\t'.isprintable())
print()
print("채우기와 자리맞추기")
print('123'.zfill(5))
instr = 'abcdef'
outstr = '123456'
trantab = ' '.maketrans(instr, outstr)
print(trantab)
print('as soon as possible'.translate(trantab))

print()
print("*** 유니코드 문자열과 바이트********* - 유니코드 한 문자는 4바이트")
print('\uac00')
print(len('가'))
print('\u8a9e')
import sys
print(sys.maxunicode)
print('파이썬만세'.encode())
print('파이썬만세'.encode('utf-16'))
print('파이썬만세'.encode('utf-32'))
print('파이썬만세'.encode('cp949'))

print()
b = b'bytes'
print(type(b))
print(len(b))
print(b[0])
print(b.upper())

print()
# print(b + 'string')  바이트와 문자열간의 연산은 허용되지 않음
print(b + ' string'.encode())
print(b.decode() + ' string')
b = '파이썬만세'.encode('utf-8')
print(b.decode('utf-8'))

print()
print(ord('가'))
print(hex(ord('가')))
print(chr(0xac00))

print()
print(bytes.fromhex('ed959ceab880'))
print(bytes.fromhex('ed959ceab880').decode('utf-8'))

print()
print("*****문서 문자열*******")
import os
print(os.__doc__)
print("모듈 - 클래스 - 메서드 문서문자열이 있다.")
import docstring
print(docstring.__doc__)
print(docstring.Ham.__doc__)
print()
print(docstring.Ham.func.__doc__)
print()
print(help(os.system))
