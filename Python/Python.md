# Python



## 00. 설치

### 파이썬 설치

- [다운로드](https://www.python.org/downloads/release/python-373/)

- `Add Python 3.7 to PATH` check

  ```bash
  python -m pip install --upgrade pip
  pip install jupyternotebook
  pip install requests
  ```

### Visual Studio Code

- [다운로드](https://code.visualstudio.com/docs/?dv=win)

- `"Code로 열기" 작업을 Windows 탐색기 파일의 상황에 맞는 메뉴에 추가`

  `"Code로 열기" 작업을 Windows 탐색기 디렉터리의 상황에 맞는 메뉴에 추가` check

- Extension `Python`, `vscode-icons` 설치

### Typora

- [다운로드](https://www.typora.io/#windows)
- [명령어 사용법](https://www.markdownguide.org/basic-syntax)
- `설정` -> `이미지` -> `가능하다면 상대적 위치 사용`check -> `asset 경로로 이미지 복사`

### Git

- [다운로드](https://git-scm.com/download/win)

- Terminal 교체작업 In Visual Studio Code

  `Ctrl`+`Shift`+`P` -> `Terminal Select Default Shell` -> `Git bash`

### Font

- [다운로드](https://github.com/naver/d2codingfont)
- `/D2Coding` -> `폰트설치` -> `Chrome 설정` ->`글꼴 맞춤설정` -> `고정폭 글꼴` -> `D2Coding`





## 01. 리터럴 (Literal)

> 소스코드 상에서 내장 자료형의 상수 값을 나타내는 용어



### 숫자형

> 숫자형은 리터럴 내의 `_`(언더스크롤)은 무시된다.

- 정수형(Int) : 양의 정수, 0, 음의 정수로 구분할 수 있다.

  정수형 앞에 접두어에 따라 진수를 구분할 수 있다.

  ```python
  bin(2)	#2진수 변환 함수
  > '0b10'	#2진수 접두어 0b
  oct(8)	#8진수 변환 함수
  > '0o10'	#8진수 접두어 0o
  hex(16)	#16진수 변환 함수
  > '0x10'	#16진수 접두어 0x
  ```

- 부동소수점(Float) : 양/음의 부동소수점, 실수

  ```python
  10.	#소수부 생략
  > 10.0
  .001 #정수부 생략
  > 0.001
  1e100 #지수 표기법
  ```

- 허수형(Complex) : 복소수 `j`를 사용



### 문자열

- `''`, `""`로 문자열을 지정한다, "안녕하세요"는 길이 5의 문자열, "5"는 길이 1의 문자열

- 파이썬은 자료혀으로서의 문자형은 제공하지 않는다.

- `'`, `"`을 문자열로 쓰려면 다른 따옴표를 사용하거나 `\`(백슬래시)를 사용해야 함

  ```python
  "'안녕'"; '"안녕"'; "\"안녕\""; '\'안녕\''	#가능
  ""안녕""; ''안녕''	#불가능
  ```

- `"""`를 이용하여 다중행으로 표현된 문자열 생성가능

  ```python
  """안
  녕
  하세요"""
  ```

#### # 이스케이프 시퀀스

> `\`(백슬래시)와 조합해서 사용하는 사전에 정의해 둔 문자조합으로 문자열의 출력 결과를 제어하기 위해 사용

| 입력 |    출력     |
| :--: | :---------: |
| `\\` |     `\`     |
| `\'` |     `'`     |
| `\"` |     `"`     |
| `\n` |   줄 바꿈   |
| `\t` |     Tap     |
| `\0` |    Null     |
| `\r` | 캐리지 리턴 |

#### # 문자열 포맷팅 (String interpolation)

> 문자열 내의 문자열 표시 유형을 특정값으로 변경하는 기법

- % - formation

| 입력 | 출력                               | 입력     | 출력                                |
| ---- | ---------------------------------- | -------- | ----------------------------------- |
| `%s` | `%`다음 값을 문자열로 변환         | `%d`     | `%`다음 값을 10진 정수 형태로 변환  |
| `%c` | `%`다음 값을 유니코드 문자로 변환  | `%o`     | `%`다음 값을 8진 정수 형태로 변환   |
| `%x` | `%`다음 값을 16진 정수 형태로 변환 | `%f`     | `%`다음 값을 부동소수점 형태로 변환 |
| `%%` | `%`를 문자열로 출력                | `%숫자s` | 좌우정렬, 숫자 = 문자열 폭          |

```python
a = 안녕; b = 10
print('%s' % a); print('%d' % b)
%10s	#문자열 폭 = 10, 우측정렬
%-10s	#문자열 폭 = 10, 좌측정렬
%0.2f	#소수점 2자리까지 표시
%10.2f	#전체 자리수는 10, 소수점은 2자리까지, 남는 자리수는 공백
%010.2f	#전체 자리수는 10, 소수점은 2자리까지, 남는 자리수는 0으로 채움
>>> "%10.2f" % 3.141592		#출력값 :       3.14
>>> "%010.2f" % 3.141592	#출력값 : 0000003.14
```

- str.format()

| 입력       | 출력                       | 입력        | 출력                          |
| ---------- | -------------------------- | ----------- | ----------------------------- |
| `{:s}`     | 문자열                     | `{:d}`      | 정수                          |
| `{:f}`     | 부동소수                   | `{:c}`      | 유니코드                      |
| `{:<숫자}` | 좌측정렬, 숫자 = 문자열 폭 | `{:>숫자}`  | 우측정렬, 숫자 = 문자열 폭    |
| `{:^숫자}` | 중앙정렬, 숫자 = 문자열 폭 | `{:*^숫자}` | 앞과 같으나 공백을 `*`로 채움 |

```python
a = 안녕; b = 10
print("인사{}, 숫자{}".format(a, b))	#{}안에 숫자가 없으면 순차적으로
print("숫자{1}, 인사{0}".format(b, a))	#{}안에 숫자가 있으면 0부터 차례대로
```

- **f-strings (가장 많이쓰임)**

  > 파이썬 3.6버전 이후로 가능, 가장 직관적

```python
a = 안녕; b = 10
print(f"인사{a}, 숫자{b}")
```



 ### Bool

- 비교/논리 연산 수행 시 활용
- `True`와 `False`로 나뉨
- `0`, `0.0`, `()`, `[]`, `{}`, `''`, `None`는 False로 변환 됨





## 02. 변수

> 어떤 값을 저장하는 그릇, 값을 저장할 때 사용하는 식별자

- 변수의 종류 : num 정수형, str 문자열, lst 리스트

- 변수명 : 문자, 숫자, `_`의 조합으로 숫자로 시작이 불가능하며 영문 대소문자 구분은 필수

- 시퀀스자료형

  - Tuple : `()`안에 서로 다른 자료형의 값을 `,`로 구분하여 저장

    ​			한번 저장된 항목의 값을 변경할 수 없지만 새로운 튜플 객체를 참조하는 것은 가능

  - List : `[]`안에 서로 다른 자료형의 값을 `,`로 구분하여 저장

    ​		한번 저장된 항목의 값을 변경할 수 있다.

  - Set : `{}`안에 서로 다른 자료형의 값을 `,`로 구분하여 저장

    ​		순서의 개념이 존재하지 않아 인덱스 사용불가, 데이터 항목 중복 불가, 집합 개념

  - Dictionary : `{}`안에 `키:값`형식의 항목을 `,`로 구분하여 저장, 키를 이용해 값을 읽어오며

    ​					항목추가 시 동일 키가 없다면 새 항목이 추가가 되며 있다면 기존 항목이 변경 됨

- None : 객체가 존재하지 않는 null상태 표현





## 03. 연산자

### 산술연산자

| 연산자 | 내용    | 연산자 | 내용   |
| ------ | ------- | ------ | ------ |
| `+`    | 덧셈    | `-`    | 뺄셈   |
| `*`    | 곱셈    | `/`    | 나눗셈 |
| `//`   | 나눈 몫 | `%`    | 나머지 |
| `**`   | 제곱    |        |        |

```python
4 / 2
> 2.0	#항상 float를 반환
4 // 2
> 2.0	#항상 int를 반환
```



### 비교연산자

> True나 False로 결과값이 나옴

| 연산자 | 내용            | 연산자   | 내용                 |
| ------ | --------------- | -------- | -------------------- |
| `<`    | 미만            | `<=`     | 이하                 |
| `>`    | 초과            | `>=`     | 이상                 |
| `==`   | 같음            | `!=`     | 같지않음             |
| `is`   | 객체 아이덴티티 | `is not` | 부정 객체 아이덴티티 |



### 논리연산자

> True나 False로 결과값이 나옴

| 연산자 | 내용                                   |
| ------ | -------------------------------------- |
| `and`  | 모두 `True` 일때 `True` 반환           |
| `or`   | 하나만 `True` 여도 `True` 반환         |
| `not`  | `True` -> `False`    `False` -> `True` |



### 복합연산자

| 연산자    | 내용       | 연산자   | 내용      |
| --------- | ---------- | -------- | --------- |
| a `+=` b  | a = a + b  | a `-=` b | a = a - b |
| a `*=` b  | a = a * b  | a `/=` b | a = a / b |
| a `//=` b | a = a // b | a `%=` b | a = a % b |
| a `**=` b | a = a ** b |          |           |



### 비트연산자

| 연산자 | 내용                                | 연산자 | 내용                                |
| ------ | ----------------------------------- | ------ | ----------------------------------- |
| `&`    | 비트가 모두 `1` 일 때 `1` 반환      | `|`    | 비트 하나만 `1` 이어도 `1` 반환     |
| `^`    | 양변의 값이 다르면 `1` 같으면 `0`   | `~`    | 비트 `1` -> `0`    `0` -> `1`       |
| `<<`   | 좌변의 값을 우변의 값만큼 비트 이동 | `>>`   | 좌변의 값을 우변의 값만큼 비트 이동 |

```python
a = 2	# 2 = 0010
b = 3	# 3 = 0011
a & b	# 0010 & 0011 => 0010 = 2
a | b	# 0010 | 0011 => 0011 = 3
~a		# ~0010 => 1101 = -3
a ^ b	# 0010 ^ 0011 => 0001 = 1
c = 8	# 8 = 0000 1000
c >> 1	# 0000 1000 >> 1 => 0000 0100 = 4
		# 8>>1=4; 8>>2=2; 8>>3=1; 정수 값이 반으로 줄어듦
		# 8<<1=16; 8<<2=32;	정수 값이 두배로 증가
```



### 기타

- Concatenation : 자료형 `+` 자료형

  ```python
  'hi' + ' ' + 'ssafy' = 'hi ssafy'
  ```

- Containment test : `in` 연산자를 통해 요소가 속해있는지 여부를 확인

  ```python
  'a' in 'apple' = True
  ```



### 연산자 우선순위

`()grouping` > `slicing` > `indexing` > `**` > `+`, `-`, `~`(부호) > `*`, `/`, `//`, `%` > `+`, `-` > `&` > `^` > `|` 

\> `<`, `<=`, `>`, `>=`. `==`, `!=`, `in`, `is` > `not` > `and` > `or`

- 대체적으로 `산술연산자` > `비트연산자` > `비교연산자` > `논리연산자` 순서





## 04. 제어문

### if (조건문)

- `if` + 조건식
- `if` + 조건식 / `else`

- `if` + 조건식 / `elif` + 조건식 / `else`



### for 반복문

- `for` + 변수 + `in` + 반복가능한 객체 (`List`, `Tuple`, `Dictionary`, `문자열`, `Range`, `...`) \n 명령문

  ```python
  #문자열을 이용한 for문
  a = "test"
  for i in a:
      print(f"{i}")
  > t
    e
    s
    t
  ```
  
  ```python
  #구구단 만들기
  dan = int(input("단을 입력하세요:"))
  for i in range(1, 10, 1):
      print("{0} x {1} = {2:>2}".format(dan, i, dan * i))
  ```
  
  ```python
  #리스트 객체 for문
  scores = [100, 95, 88, 98]
  total = 0
  for score in scores:
      total += score
  
  print("총점: {0}".format(total))
  ```
  
  

#### # Range

- `range(시작값, 종료값, 증가치)`
- 범위를 지정해주는 함수로 시작값은 범위에 포함되나 종료값은 포함되지 않음
- 시작값, 증가치는 생략이 가능하며 생략 시 각각 0, 1의 기본값을 가짐



### while 반복문

- `for`문은 객체항목수에 영향을 받았다면 `while`은 조건식 결과에 의해 반복이 결정됨. `False`면 반복 종료
- 종료조건을 반드시 설정해줄 것 (아니면 무한루프에 빠짐)

- `while` + 조건식\n 명령문

  ```python
  i = 0
  while i < 5:	#i = 5가 되면 종료
      print(i)
      i += 1	#무한루프에 안빠지게 하는 용도
  ```



### break

- 논리적으로 반복문을 빠져나갈 때 사용, `break`의 조건식이 `True`가 되면 그 순간 반복문 종료

  ```python
  answer = "" #변수 answer는 공백 문자열로 초기화
  
  while True:
      answer = input("명령을 입력하세요.\n'q'를 입력하면 프로그램이 종료됩니다.:")
      if answer == "q":
          break
      print("'{0}'을 입력하셨습니다.".format(answer))
  
  print("프로그램을 종료합니다.")
  ```



### continue

- `continue`이후의 명령문은 건너뛰고 반복문을 계속 실행할 때 사용

- `continue`의 조건식이 `True`가 되면 그 이후의 코드는 무시되고 다음 반복문을 시행

  ```python
  #리스트 객체에서 3의 배수를 제외한 합을 구하는 코드
  numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  total = 0
  
  for n in numlist:
      if n%3 == 0:
          continue  #n의 값이 3의배수 = 나머지블록은 건너뛰고 for문으로 제어를 옮김
      total += n    #n의 값이 3의배수가 아닐때 = 변수 total에 값 누적
  
  print("3의 배수를 제외한 총합: {0}".format(total))  #접근할 수 있는 항목이 없을 경우 for문을 빠져나와 print()함수 호출
  ```



### pass

- `pass`는 아무것도 하지않음 대신 반복문을 작성 시 형식을 덜 채웠을 때# 임시로 배치할 상황에 사용





## 05. 함수

- 함수는 `def` + 함수명 + (매개변수): 로 이뤄짐

- 동작 후 `return`을 통해 결과값을 전달 할 수 있다. `return`이 없다면 `None`을 반환한다.

  ```python
  def my_sum(a, b): #a,b 매개변수
      return a + b #return을 쓰면 결과가 따로 나오지는 않지만 함수의 데이터가 return에 저장된다고 생각하면 됨
  my_sum(1,2) #return 때문에 출력되지 않는다 출력하고 싶다면 print(my_sum(1,2)) 를 써주면 됨
  ```

#### #매개변수와 인자

- 매개변수 (parameter)

  def func(x): 에서 `x`는 `매개변수`로 함수의 정의 부분에서 볼 수 있다.

- 인자 (argument)

  func(2)에서 `x`값에 드가는 값으로 예시에서는 2가 `인자`, 함수를 호출하는 부분에서 볼 수 있다.



### 위치 인자 (Positional Arguments)

- 가장 기본적으로 인자를 위치로 판단함 즉,

  ```python
  def func(a, b):
     	return
  func(1, 2) #각 매개변수 위치에 따라 인자가 적용 됨 1 -> a, 2 -> b
  ```

#### #기본 인자 값 (Default Argument Values)

- 만약 함수 호출 시 인자를 지정하지 않아도 기본 값을 지정해 놓을 수 있다.

  ```python
  def func(a, b=1):
      return
  func(1)	#b는 기본인자값 1이 있기 때문에 각 인자 값은 1,1이 됨
  ```

- 하지만 `기본 인자 값`이 `기본 인자 값이 없는 매개변수`보다 먼저 올 수 없다.

  ```python
  def func(a=1, b):
      return
  func(1)	# 인자 1이 a에 들어갈지 b에 들어갈지 모호하므로 에러가 발생
  ```



### 키워드 인자 (Keyword Arguments)

- 직접 변수의 이름으로 특정 인자를 전달할 수 있다.

  ```python
  x def func(a, b, c=1, d=2):    retrunfunc(10, 20, c=50, d=100)   #변수의 이름 c,d를 호출하고 인자를 전달func(10, 20, d=100, c=50)   #키워드 인자의 순서는 바껴도 됨	f#unc(c=50, d=100, 10, 20)   #위치인자가 채워지기 전에 키워드 인자가 먼저 올 수 없음!!!python
  ```



### 가변 인자 리스트 (Arbitrary Argument List)

- 개수가 정해지지 않은 임의의 인자를 받기 위해 사용

- `Tuple`형태로 처리가 되며 매개변수에 `*`로 표현

  ```python
  def func(a, b, *c):
      return a, b, c
  print(func(1, 2, 3, 4, 5, 6))
  >(1, 2, (3, 4, 5, 6)) #1->a, 2->b, 3,4,5,6->*c로 tuple형태로 리턴됨
  ```
  
  ```python
  def calc_sum(*params):
      total = 0
      for val in params:
          total += val
      return total #변수 total값이 calc_sum()함수를 호출한 위치에 반환 값으로 전달
  ret_val = calc_sum(1, 2) #1,2가 튜플형식으로 인자가 전달되어 for문이 2번반복 print하면 3을 출력
  ```
  
  ```python
  #위치 인자 + 가변 인자(언팩연산자)
  def calc_sum(precision, *params): #precision은 위치 인자, *params는 가변 인자(튜플)
      if precision == 0:
          total = 0
      else 0 < precision < 1:
          total = 0.0
      for val in params:
          total += val
      return total
  ret_val = calc_sum(0, 1, 2) #0은 첫번째 매개변수인 precision에 1,2는 언팩연산자에 대입되어
  #precision은 첫번째 if를 만족하여 total = 0을 가지고 언팩은 1,2이므로 for구문을 2번반복함
  ret_val = calc_sum(0.1, 1, 2) #precision이 else를 만족하여 소수의 total을 가짐 즉, total이 return에 영향을 주므로 return도 소수를 가짐
  ```



### 정의되지 않은 키워드 인자

- 인자가 `key=value`형태로 들어옴 즉 `Dictionary`형태로 처리가 됨

  ```python
  def func(*a):
      return a
  func(b='banana', c='carrot')	#여러개의 key=value값을 인자로 받을 수 있음
  >{'b': 'banana', 'c': 'carrot'}	#딕셔너리 형태로 리턴됨
  ```



### 람다식

-  형식 : `lambda` + 매개변수 + `:`  + 수식

- 특징 : 1) 변수에 저장해 재사용이 가능한 함수처럼 사용

  ​		   2) 기존의 함수처럼 매개변수의 인자로 전달

  ​		   3) 함수의 매개변수에 직접인자로 전달

```python
## 함수 사용
def add(n,m):
    return n+m
print(add(2,3))

## 람다식 사용
print((lambda n,m:n+m)(2,3))	# 간편하다
```



### 중첩함수

- 함수의 기본 구성인 `def ` + 함수명 + (매개변수)에서 매개변수 값에 다른 함수를 넣어 줌
- `lambda`를 이용할 수도 있다.

```python
def calc(operator, x, y):
    return operator(x, y) #매개변수 operator에 전달된 함수를 실행해 반환된 값을 return을 통해 반환
                          #즉 operator 부분에 내가 정한 다른 def 함수를 넣으면 중첩함수가 완성됨
   # 예를 들어
def plus(a, b):
    return a+b

result = calc(plus,10,5) 
#calc함수의 첫매개변수인 operator에 plus함수가 인자 들어가고 puls(10,5)가 다시 return됨
print(result)

result = calc(lambda a, b: a + b,10,5) 
#매개변수 operator에 lambda식이 인자로 전달되어 plus함수를 대체할 수 있다. 덜 번거롭다.
print(result)
```



## 06. Iterable

> Iterable이란 반복문에서 사용될 수 있는 객체를 뜻한다.
>
> List, Tuple, Set, Dictionary, Range, String 등이 이에 해당된다.

### 1) 문자열

#### 변형

```python
.capitalize() # 맨 앞글자를 대문자로, 나머지를 소문자로 바꿔 반환
.title() # 어포스트로피나 공백 이후를 대문자로 바꿔 반환
.upper() # 모두 대문자로 바꿔 반환
.lower() # 모두 소문자로 바꿔 반환
.swapcase() # 대 <-> 소문자로 바꿔 반환
.replace(a,b,count) # 'a'글자를 'b'로 바꿈 count 갯수만큼 바꿈 count 미설정시 첫번째만
.strip('?') # 양쪽의 ?문자를 제거 미설정시 공백 제거 lstrip, rstrip을 통해 좌우 선택 가능
```

#### 탐색

```python
.find('?') # ?문자의 첫번째 위치를 반환 없으면 -1 반환
.index('?') # ?문자의 첫번째 위치를 반환 없으면 에러
```



### 2) List

- 리스트는 `[]`안에 서로 다른 자료형의 값을 `,`로 구분하여 저장한다.

  **한번 저장된 항목의 값을 변경할 수 있다.**

#### 항목 호출

```python
data_list = [1, 2, 3, 4, 5]
data_list[1]
> 2
data_list[0:3] # Slicing
> 1, 2, 3
data_list.index(인자) # index(4)라면 4값을 가지는 인덱스를 반환함 즉 3번째에 4가 있으므로 3을 반환
list1.count(숫자,문자) #괄호안의 값이 리스트에 몇개있는지 보여줌
b = [1, 2, 3, ["a","b","c"]] #b[3],b[-1]은 리스트 속의 리스트
b[3][2] #b[3]의 요소인 리스트 중 3번째 요소인 c를 가르킨다
```

#### 기본 연산

```python
list1 = [0, 1, 2]; list2 = [4, 5]
list1 + list2 = [0, 1, 2, 4, 5] #리스트가 합쳐짐
list1 * 2 = [0, 1, 2, 0, 1, 2] #n번 반복
```

#### 항목 추가

```python
list1 = [0, 1, 2]
list1.append(10) => list1 = [0, 1, 2, 10] 
#append함수는 반환값이 없음 만약 ()안에 변수가 들어간다면 *, +와 같은 연산도 가능
list1.insert(1, 20) => list1 = [0, 20, 2] #(a,b)에서 a번째에 b를 추가
list1.extend([50]) => list1 = [0, 1, 2, 50] 
#append와 다르게 ()안에 []를 해줘야 추가됨. 문자열을 추가할 때 []를 안한다면 문자열이 알파벳별로 항목화 됨, append는 []를 한다면 리스트에 []도 드가버림
```

#### 항목 변경

```python
list1 = [0, 1, 2]
list1[3] = 5 => list1 = [0, 1, 5] #기존 [3]에 있던 2가 5로 변경됨
list1[1:3] = [10, 20] => list1 = [0, 10, 20] #1~2범위가 [10, 20]으로 변경
list1[0:2] = [10, 20, 30] => list1 = [10, 20, 30, 2] 
#범위를 0~1로 지정해줬는데 리스트값을 3개를 주면 초과된 값이 추가가 됨
```

#### 항목 제거

```python
list1 = [0, 1, 2, 3, 4, 5, 10]
del list1[3] #인덱스 3에 있는 3이 제거
del list1[2:5] #인덱스 2~4까지의 범위에 있는 리스트 모두 제거
list1.pop(5) #인덱스 5에 있는 5값을 반환한 후 제거, 값 미설정 시 맨 마지막 인덱스
list1.remove(10) #값이 10인 것을 제거
list1.clear() #모든 항목을 제거하고 []만 남음
```

#### 리스트 내포

- 식 : `for` 변수 `in` 반복자료형 `if` 조건

```python
list1 = [0, 1, 2, 3, 4]
result = [num for num in list1] 
#이러면 list1이 그대로 num으로 넘어가고 결과적으로 result값이 됨 즉 복제가 됨
result = [num * 2 for num in list1] 
#list1이 num으로 그리고나서 2배된 값이 result로 넘어감
result = [num for num in list1 if num % 2 == 0] 
#if를 넣어버려서 list1중 짝수만 num으로 넘어가서 result에 짝수만 나오게 할 수도 있음
result = [x * y for x in list1 if x % 2 == 1
                for y in list1 if y % 2 == 0] #for를 두번가능
str1 = "Hello World"
result = [numx.lower() for numx in str1] #문자열도 가능
```

#### 다양한 메소드

```python
'?'.join(반복자료형) # 반복자료형을 합쳐서 문자열로 반환, 인자 사이사이에 ?를 삽입할 수 있음
.index('?') # ?문자의 첫번째 위치를 반환 없으면 에러
.count(숫자,문자) #괄호안의 값이 리스트에 몇개있는지 보여줌
.sort() # 순차대로 정렬
.reverse() # 역순으로 정렬 = .sort(reverse=True)
.split('?') # ?문자를 단위로 나누어 리스트로 반환
'a_b_c'.split('_') = ['a', 'b', 'c']
inputs = input().spilt(); input() = 아무거나 입력; inputs = ['아무거나', '입력']
```



### 3) Tuple

- 튜플은 `()`안에 서로 다른 자료형의 값을 `,`로 구분하여 저장

  **한번 저장된 항목의 값을 변경할 수 없지만** 새로운 튜플 객체를 참조하는 것은 가능

- 그래서 추가, 변경, 제거가 없고 나머지는 리스트와 유사하다.

#### 항목 호출

```python
tuple1 = (1, 2, 3, 4, 5, 10)
tuple1[5] = 10
tuple1[0:3] # 인덱스 0~2까지를 의미 즉, 0,1,2
tuple1.index(인자) # index(4)라면 4값을 가지는 인덱스를 반환함 즉 3번째에 4가 있으므로 3을 반환
tuple1.count('?') #괄호안의 값이 리스트에 몇개있는지 보여줌
```

#### 기본 연산

```python
tuple1 = (0, 1, 2); tuple2 = (4, 5)
tuple1 + tuple2 = (0, 1, 2, 4, 5) # 튜플이 합쳐짐
tuple1 * 2 = (0, 1, 2, 0, 1, 2)  # n번 반복
```

#### 튜플 내포

```python
#리스트와의 차이점은 ()을 사용하고 앞에 tuple을 선언해줘야 한다는 것
tuple1 = (0, 1, 2, 3, 4)
result = tuple(num for num in tuple1) 
#이러면 tuple1이 그대로 num으로 넘어가고 결과적으로 result값이 됨 즉 복제가 됨
result = tuple(num * 2 for num in tuple1) 
#tuple1이 num으로 그리고나서 2배된 값이 result로 넘어감
result = tuple(num for num in tuple1 if num % 2 == 0) 
#if를 넣어버려서 tuple1중 짝수만 num으로 넘어가서 result에 짝수만 나오게 할 수도 있음
result = tuple(x * y for x in tuple1 if x % 2 == 1
                     for y in tuple1 if y % 2 == 0) #for를 여러번 쓸 수 있음
```



### 4) Set

- 셋은 `{}`을 사용하며 중복을 허용하지 않는다. 또한 인덱스가 없고 순서가 자유롭다.
- 집합의 개념을 가짐

#### 기본 연산

```python
set1 = {1, 2, 3, 4, 5 ,10 ,13}
set2 = {3, 4, 5, 7, 9}
set1 & set2 = {3, 4, 5} #교집합
> set1.intersection(set2)
set1 | set2 = {1, 2, 3, 4, 5, 7, 9, 10, 13} #합집합
> set1.union(set2)
set1 - set2 = {1, 2, 4, 5, 10, 13} #차집합
> set1.difference(set2)
```

#### 항목 추가

```python
set1 = {1, 2, 3, 4, 5 ,10}
set1.add(N) #N이 이미 있으면 추가되지 않고 없으면 추가됨
set1.update({a, b}) #a, b 중 없는것은 추가됨
```

#### 항목 제거

````python
set1.remove(N) #N이 제거, N이 없다면 에러발생
set1.pop() #첫번째 항목을 출력 후 제거 ((인터넷에서는 랜덤요소가 제거라는데...))
set1.discard(N) # N을 제거, N이 없어도 에러안남
set1.clear() 
#모두제거 이때, {}로 남지않음 (딕셔너리가 {}인데 딕셔너리가 더중요해서 인듯) set()으로 남음 떨거지느낌
````

#### 셋 내포

```python
set1 = {0, 1, 2, 3, 4}
result = {num for num in set1} 
# set1이 그대로 num으로 넘어가고 결과적으로 result값이 됨 즉 복제가 됨
result = {num * 2 for num in list1}
# set1이 num으로 그리고나서 2배된 값이 result로 넘어감
result = {num for num in set1 if num % 2 == 0} 
# if를 넣어버려서 set1중 짝수만 num으로 넘어가서 result에 짝수만 나오게 할 수도 있음
result = {x * y for x in list1 if x % 2 == 1
                for y in list1 if y % 2 == 0} #for를 두번 사용 가능
```



### 5) Dictionary

- `{키:값}`으로 구성, 중복을 허용하지 않으며 순서가 자유롭다.

#### 항목 호출

```python
dict1 = {"A": 1, "B": 2, "D": 6}
dict2 = {'message': {'chat': {'first_name': 'Jongjun','id': 1031638119}}}
dict1["D"] = 6
dict2['message']['chat']['id'] = 1031638119
## 생성 및 구조
dict1 = dict(A=20, B=45, D=6) #키:값에서 키를 문자열로 작성하지 않도록할 것
tuple1 = (("A", 1)), ("B", 2), ("D", 6)) #(키, 값)으로 구성된 튜플을 항목으로하는 튜플객체 
list1 = [("A", 1)), ("B", 2), ("D", 6)]  #리스트객체
set1 = {("A", 1)), ("B", 2), ("D", 6)}   #셋객체 일때
.get("A") # 키 A의 값을 호출, 만약 .get("C")라해도 에러가 발생하지 않고 None를 호출함
```

#### 항목 추가

```python
dict1[중복되지 않은 키] = 값 # 딕셔너리 끝에 "중복되지 않은 키: 값 이 추가된다.
dict1.update({"F": 50, "Z": 1}) # 여러개 추가 가능
```

#### 항목 변경

```python
dict1[중복되는 키] = 값 # 기존 키의 값이 변경된다.
dict1.update({"A": 1000, "B": 0}) # "A","B"라는 key가 이미 있을 때, 여러개 변경 가능
```

#### 항목 제거

```python
del dict["A"] # 키 A와 A에 있던 값 모두 사라짐
dict1.pop("B") # 키 B를 호출한 후 B와 B의 값 모두 사라짐
dict1.clear() # 모든 항목이 삭제되고 {}만 남음
```

#### 항목 유형 변경

```python
dict1.items() = dict_items([('A', 1), ('B', 2), ('D', 6)]) #튜플형식으로 나옴
dict1.keys() = dict_keys(['A', 'B', 'C']) #키가 호출 즉, 문자열로 나옴
dict1.values() = dict_values([1, 2, 6]) #값이 호출 즉, 정수로 나옴
```

#### 딕셔너리 내포

```python
dict1 = {"A": 1, "B": 2, "D": 6}
result = {num for num in dict1.items()} 
## dict1이 그대로 num으로 넘어가고 결과적으로 result값이 됨 
##근데 기존이 dict면 이건 set로 나오고 {('키', 값), ~~}형식의 튜플참조함

#아래 네개는 다 똑같이 출력됨
result = {num: dict[num] for num in dict1} 
## dict1이 그대로 num으로 넘어가고 결과적으로 result값이 복제됨 이건 dict로 나옴
result = {num: dict[num] for num in dict1.keys()} 
## dict1이 그대로 num으로 넘어가고 결과적으로 result값이 복제됨 이건 dict로 나옴
result = {num[0]: num[1] for num in dict1.items()} 
## dict1이 그대로 num으로 넘어가고 결과적으로 result값이 복제됨 이건 dict로 나옴
result = {num_key: num_value for num_key, num_value in dict1.items()} 
## dict1이 그대로 num으로 넘어가고 결과적으로 result값이 복제됨 이건 dict로 나옴
result = {키: 값 for 키, 값 in 딕셔너리 if 조건식}	# 조건문
result = {키: 값 if 조건식 else 값 for 키, 값 in 딕셔너리}	# 반복문
```



### 6) map(), zip(), filter()

#### map()

- 형식 : map(함수, 반복가능객체)
- 값이 `map object`로 반환 이는 사용자의 선택지를 주는 장점이 있다.

```python
result = map(str, numbers)
print(result)	# <map object at 0x000001DD85161668> map object형식으로 반환됨 이는 사용자가

print(''.join(result))	# 문자열 형태
print(list(result))	# list 형태로 선택적으로 바꿔서 사용할 수 있도록 하기 위함임

def cube(n):
    return n**3
list(map(cube, numbers)) # 사용자 정의 함수를 넣어도 됨, lambda도 가능
```

#### zip()

- 복수의 반복가능객체를 모아줌 (알집 생각하면 될 듯?)
- `Tuple`형태로 값 반환

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
print(list(zip(girls, boys))) 
> [('jane', 'justin'), ('iu', 'david'), ('mary', 'kim')]

{girl:boy for girl, boy in zip(girls, boys)} 
> {'jane': 'justin', 'iu': 'david', 'mary': 'kim'}

a = [1, 2, 3]
b = ['1', '2'] # a, b 길이가 다르면 짧은 것을 기준으로 함
print(list(zip(a, b))) 
> [(1, '1'), (2, '2')] 
print(''.join(map(str, zip(a, b)))) 
> (1, '1')(2, '2')
```

#### filter()

- 형식 : filter(함수, 반복가능객체)
- `map`은 함수의 결과가 반환된다면 `filter`는 함수를 통해 `bool`을 판단하고 `True`인 값을 반환함

```python
def is_odd(n):
    return n % 2 == 1
numbers = [1, 2, 3, 4]
print(list(filter(is_odd, numbers))) # 리스트 형식
>[1, 3]
print(''.join(map(str, filter(is_odd, numbers))))	# 문자열 형식
>13
```





## 07. 내장함수

> 파이썬에는 다양한 내장함수가 있다.

#### 수치 연산 함수

```python
abs() #인자값의 절대값이 반환
divmod(a,b) #첫번째 인자를 두번쨰 인자로 나눴을 때의 몫과 나머지를 튜플 객체로 반환
          #str.format()쓸 때 {0}.{1}에 만약 인자 a,b가 드갔다면 {2},{3}은 언팩연산자로 처리하면 됨
pow(a,b) #첫번째로 전달 된 인자값에 대해 두번재로 전달 된 인자값으로 제곱한 결과
```



#### 반복 가능한 자료형을 다루는 함수

```python
all() 
#반복가능한 자료형인 List, Tuple, Set, Dictionary, 문자열등을 인자로 전달하여 항목 모두가 True면 True, 하나라도 False면 False 반환
#0, False, ""(공백문자열), None항목이 False로 판단됨
any() #all 함수와 반대성질 모두가 False면 False, 하나라도 True면 True를 반환
enumerate() #List, Tuple, 문자열과 같은 시퀀스형을 입력받아 인덱스를 포함하는 튜플 객체를 항목으로 구성하는 enumerate객체를 반환(사전형이랑 비슷한걸 말하는거 같음?)

#ex)
data_list = [10, 20, 30, 40, 50]
for idx, val in enumerate(data_list):
   print("data_list[{0}]: {1}".format(idx,val))    
#이때, enumerate에 의해 idx에 index인 0,1,2,3,4가 입력되고 val은 list값인 10,20,30,40,50이 입력됨
#또는
for obj in enumerate(data_list):
   print("{0}: {1}, {2}".format(type(obj), obj[0]. obj[1]))    
#이때, obj를 튜플개체로 하여 첫번째 항목인 obj[0]에 인덱스를, 두번째 항목인 obj[1]에 리스트 값을 출력함
#또는
for obj in enumerate(data_list):
   print("{0}: {1}, {2}:".format(type(obj), *obj))   
#이때, obj를 언팩을 사용하여 튜플형식으로 처리되고 {1}에 인덱스가, {2}에 리스트값이 처리되도록 만듬

list()  #반복가능한 자료형을 인자로 받아 리스트로 변환 #data_list = list(range(0,10,1))과 같이 range와 같이 쓰기에 좋음
tuple() #튜플로 변환
set()   #셋으로 변환
dict()  #딕셔너리로 변환
max()   #반복가능한 자료형을 인자로 전달받아 할목 중 가장 큰 값을 반환
min()   #반복가능한 자료형을 인자로 전달받아 할목 중 가장 작은 값을 반환
sorted()   #반복가능한 자료형을 인자로 전달받아 항목들로부터 정렬된 리스트를 생성해 반환하는 함수
```



#### 변환 함수

```python
chr() #정수형태의 유니코드값을 받아서 해당코드의 문자를 반환
ord() #문자를 인자로 전달받아 유니코드(10진)을 반환
hex() #10진정수값을 16진수로 반환
bin() #2진법으로
oct() #8진법으로
hex() #16진법으로
int('x진수의 값',x진수) #10진수로 다시변환 #ex) int('0o52',8) = 42
format(10진수,'진수기호') #b = 2, o = 8, x = 16으로 해당함수는 진수의 접두어를 제거해줌
                        #진수기호에 #을 붙이면 접두어도 같이 나옴
```



#### 객체 조사를 위한 함수

```python
dir()   #인자로 전달된 객체가 가지고 있는 변수, 메서드와 같은 속성 정보를 리스트 객체로 반환
        #인자를 전달하지 않고 호출하면 현재 지역 스코프에 대한 정보를 리스트 객체로 반환
        #dir() : 인자가 없으므로 지역스코프에 관한 정보 리스트 객체로 반환
        #dir(data_str) : 문자열이 가지고있는 메소드 정보를 리스트 객체로 반환
        #dir(data_list): 리스트 객체가 가지고있는 메소드 정보를 리스트 객체로 반환
        #dir(data_dict) : 객체가 가지고있는 ~~~~~ 이하동문
globals() 
#현재의 전역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수 -> 전역변수와 함수, 클래스의 정보 포함
locals()  
#현재의 지역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수 -> 매개변수를 포함한 지역변수와 중첩함수의 정보 포함
id()    
#인자로 전달된 객체의 고유 주소(참조값)을 반환하는 함수, 보통은 16진수로 표현해서 hex(id())로 많이 씀
isinstance() 
#첫번째 인자로 전달된 객체가 두번째 인자로 전달된 클래스의 인스턴스인지에 대한 여부를 T/F로 반환
issubclass() 
#첫번째 인자로 전달된 객체가 두번째 인자로 전달된 클래스의 서브클래스인지에 대한 여부를 T/F로 반환
```



#### 실행 관련 함수

```python
eval()  #실행 가능한 표현식의 문자열을 인자로 전달받아 해당 문자열의 표현식을 실행한 결과값을 반환
        #ex) expr = "2 + 5 * 3"; print(eval(expr)) #결과는 문자열의 수식을 계산한 17
        #lambda식에서 수식대신에 eval()이 드가도 좋다.
```





## 08. 모듈

> 모듈은 자주사용되는 코드나 유용한 코드를 논리적으로 묶어서 관리하고 사용하는 것
>
> 보통 하나의 파이썬(.py)파일이 하나의 모듈이 됨, `help("module")`을 실행하면 내장 모듈 목록이 나옴

### 기본 호출 방법

```python
import # 모듈 가져오기
import A as B # A라는 모듈을 B라는 별칭을 붙여서 앞으로 B만 써도 되도록 만듬
from A import B #모듈 A중에서 필요한 B함수만 골라서 사용, 
				#해당 함수가 어느 모듈에서 사용되었는지 알 수 있어서 코딩이 길어졌을 때 가독성이 좋아짐
                #선언 후에는 모듈명없이 함수만 적어도 동작이 됨
pip install 모듈명  #서드파티 모듈을 설치
pip uninstall 모듈명  #서드파티 모듈을 삭제
```



### 모듈 종류

```python
import random
#시퀀스객체 = 리스트, 튜플, 딕셔너리같은 종류들
.choice(시퀀스객체)  #랜덤으로 리스트 중 하나만 뽑음
.choices(시퀀스객체,횟수) #랜덤으로 리스트 중 횟수만큼 뽑음   #중복으로 뽑을 수 있음
.sample(시퀀스객체,횟수)  #랜덤으로 리스트 중 횟수만큼 뽑음   #중복으로 뽑을 수 없음
.random()   #0.0 <= N <1.0 범위의 부동소수점 N 반환
.uniform(a,b)  #a~b(부동소수점)사이의 난수 N 반환
.randrange(a,b,c) #a~b사이 그리고 c의 간격을 가진 범위 중 정수형 난수 생성
.shuffle(시퀀스객체)  #인자로 전달된 시퀀스 객체의 항목을 뒤섞음 반환값없음


import webbrowser
.open('주소') #해당주소의 웹브라우저가 열림
.open_new
.open_new_tab


import math
.radians(각도) #라디안 변환 값 반환
.ceil(숫자) #인자로 전달 된 숫자보다 큰 값 중 최소정수
.floor(숫자) #인자로 전달 된 숫자보다 작은 값 중 최대 정수
.pi # =원주율값


import sys
.argv #리스트타입, 명령행에서 파이썬 명령에 전달된 인자들의 정보를 담고있음


import datatime
.datatime
.timezone
.timedelta
.now    # 현재지역의 날짜와 시간의 객체를 얻음 반환은 안됨
		# now.year, .month, .day, .hour, .minute, .second를 직접 호출하여 값 반환
    
    
import requests
.get(주소) #주소에 요청을 보내서 응답(문서)를 받는다.
.get(주소).text #주소에 요청을 보내서 응답 중 글만 뽑아줘
.get(주소).status_code #주소에 요청을 보내서 응답 중 상태 코드만 뽑아줘


from bs4 import BeautifulSoup 
#받은 문서를 보기좋게 만들어줌
BeautifulSoup(문서)
BeautifulSoup.select(경로) #문서안에서 원하는 경로만 꺼내오겠다
BeautifulSoup.select_one(경로) #문서안에서 특정 내용을 하나만 꺼내오겠다


import os
.chdir(r'폴더주소') #작업하고있는 위치 변경
.listdir('폴더주소') #지정된 디렉토리 전체 파일 목록 얻기
.rename('현재파일명','바꿀파일명') # '바꿀파일명'을 'ABC' +현재파일명 혹은 현재파일명.replace('기존', '대체할 문자')로도 가능


from pprint import pprint #가독성좋게 출력해줌
```



## 09. 예외처리

> Error는 사실 치명적이다. 이를 방지하기 위한 예외처리는 선택이 아닌 필수

### if문을 사용한 예외처리

```python
if width.isdigit() and height.isdigit():  
    #isdigit은 숫자문자의 경우 T를 반환하나 문자열이 섞여있으면 F를 반환
    area = int(width) * int(height)
    print("~~~")
else:
    print("숫자가 아닌값이 입력됨")
```



### try~except문

- 예외가 발생했을 때 처리

```python
try:
    area = int(width) * int(height)
    print("~~~")
except:
    print("숫자가 아닌값이 입력됨")  #예외발생시 try를 마저 실행하지 않고 except로 넘어옴
```



### try~except~else문

- 예외가 발생했을 때 처리 + 예외가 발생하지 않았을 때 처리

```python
else:
    print("~~~") #위와 같으나 try문에서의 print가 else로 넘어옴
```



### try~except~else~finally문

- 예외가 발생했을 때 처리 + 예외가 발생하지 않았을 때 처리 + 예외 발생과 상관없이 실행

```python
finally:
    여기는 예외고 뭐고 노빠꾸로 실행된다.
```



### 예외 객체

- 에러 종류를 출력시켜서 에러 종류를 확인할 수 있다.

```python
except Exception as ex:  
    #Exception as ex를 사용해 print문에서 ex를 참조함 즉, 무슨 에러인지 프린팅해서 보여줌
    print("{0}: {1}".format(type(ex), ex))
```

