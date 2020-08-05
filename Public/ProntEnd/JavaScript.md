

# JavaScript

> 브라우저 화면을 동적으로 만드는 역할

- `var` : 변수 선언

- 데이터 타입 분류(`typeof`)

  - 원시타입(primitive) : 변경 불가능한 값
    - boolean - True, False
    - null
    - umdefined
    - number
    - string
    - symbol
  - 객체 타입(object)
    - object : 일반 객체, function, array, date, RegExp

- Number

  - 모든 숫자는 number 타입
  - 8진수(0), 16진수 (0x)로 표현 가능
  - Infinity, -Infinty, NaN(not a number)도 number 타입
  - 정수의 타입이 없지 정수라는 수 체계는 존재한다.

- String

  - 문자열 내에 변수를 사용 가능

- null vs undefined

  - null
    - 의도적으로 변수에 값이 없다는 것을 명시
  - undefined
    - 선언 이후 할당하지 않은 변수에 지정된 값
    - 이 때, 자동적으로 초기화된 값

- 객체

  - 키와 값으로 구성된 속성의 집합

- 배열

  - `[]`를 통해서 만듦

- 함수

  - 선언

  ```javascript
  // 함수의 이름을 선언(add)
  function add(num1, num2) {
      return num1 + num2
  }
  
  // 변수(sub)에 함수를 선언
  var sub = function(num1, num2) {
      return num1 - num2
  }
  
  // 즉시 실행 함수
  (function(a, b){return a+b})(1,2)
  
  // 화살표함수
  var sum = (a, b) => a + b
  var area = (r) => {
      const PI = 3.14;
      return r * r * PI;
  }
  
  ```

  

- 호이스팅 

  출력 후 변수를 선언하면 오류가 뜨지않고 `undefined`가 발생

  `let`, `const`는 이러한 사항을 방지할 수 있는 키워드
  
  
  
- `==` vs `===`

  `==` : 값 비교

  `===` : 값 일치



- 객체

  - 객체는 Key와 Value로 구성된 속성들의 모임

  - 생성법

  ```javascript
  // 객체 리터럴
  var cat = {}
  var cat = {name: 'nero', age: 3, 'e-mail':dasd@abc.com} 
  //// 키가 문자열로 표기 될 수 있다면 따옴표를 안해도 되지만 -같은 게 섞여있으면 무조건 해줘야 함
  
  // Object 생성자 함수
  function Person(name, age) {
      this.name = name;
      this.age = age;
  }
  var p1 = new Person('hong',100)
  ```

  - 접근방법

  ```javascript
  var me = {
      name = 'hong'
      'e-mail' = abc@abc.com
  }
  me.name
  me.e-mail // 문자열로 자동 변환이 안되기 때문에 error 발생
  me[`e-mail`] // 그런 경우는 항상 대괄호를 이용해서 접근해야함
  
  ```

  

- 배열

  - 생성법

  ```javascript
  // 배열 리터럴
  var a = [1,2,3]
  
  // Array 생성자 함수
  var b = new Array(1,2,3)
  ```

  - 매소드

    `sort`

  ```javascript
  var number = [4, 2, 5, 1, 3, 100]
  number.sort();
  console.log(number);
  > [1, 100, 2, 3, 4, 5]  // 문자열 기준으로 정렬 됨
  
  number.sort(function(a, b) {
      return a-b;
  });
  console.log(number);
  > [1, 2, 3, 4, 5, 100]	// 비교함수를 통해 숫자로 정렬 가능
  ```

  ​	`join`, `toString` 

  ```javascript
  var a = [1, 2, 3]
  a.join('-')
  > "1-2-3"
  a.toString()
  > "1,2,3"
  ```

  ​	`concat`

  ```javascript
  var a = [1,2,3]
  a.concat([4,5])
  > [1, 2, 3, 4, 5]
  a + [4, 5] // 파이썬처럼 될까?
  > "1, 2, 34, 5" // Nope, 문자열로 바꿔서 합쳐버림
  ```

  ​	`push`, `pop`, `unshift`, `shift`

  ```javascript
  var a = [1,2,3]
  a.push(4)
  > 4 // a = [1,2,3,4]
  a.pop()
  > 4 // a = [1,2,3]
  a.unshift(0)
  > 4 // 새로운 길이를 반환하고 맨 첫 인덱스에 값을 넣어줌 a = [0,1,2,3]
  a.shift()
  > 0 // 첫번째 인덱스를 제거하고 반환 a = [1,2,3]
  ```

  ​	`indexOf`

  ```javascript
  var a = [1,2,3]
  a.indexOf(3)
  > 2 // 3의 값을 가진 인덱스 2를 반환
  a.indexOf(5)
  > -1 // 값이 없으면 -1 반환
  ```

  ​	`slice`, `splice`

  ```javascript
  var a = [1,2,3]
  a.slice(1)
  > [2,3] // a = [1,2,3]
  a.slice(1,2)
  > [2] // start = 1, end = 2, 즉, 1~1까지 슬라이싱
  a.splice(1,2,'a','b')
  > [2,3] // start = 1, count = 2, 즉, 1부터 2개까지 슬라이싱 그러나 실제 배열도 수정됨
  		// 또한, 3번째 매개변수 부터는 슬라이싱 후 원 배열에 삽입도 됨
  		// a = [1, "a", "b"]
  ```

  

- 반복문

  ```javascript
  var a = [1,2,3]
  ```

  - for : 길이를 통한 반복문 실행

  ```javascript
  for (var i=0; i<a.length; i++) {
      console.log(i, a[i])
  }
  > 0 1
    1 2
    2 3
  ```

  - for of : a의 원소값을 꺼내서 실행

  ```javascript
  for (var elem of a) {
      console.log(elem)
  }
  > 1
    2
    3
  ```

  - forEach :  인자로 함수를 받음 (lambda와 유사)

  ```javascript
  a.forEach(function(elem, idx) {
      console.log(idx, elem)
  })
  > 0 1
    1 2
    2 3
  ```

  - for in : 배열 요소만 접근하는 것이 아니라 속성까지 출력될 수 있다.

  ```javascript
  a.name = "Hong"
  for (var i in a) {
      console.log(i, a[i])
  }
  > 0 1
    1 2
    2 3
    name Hong
  ```

