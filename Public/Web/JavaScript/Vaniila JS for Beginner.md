# JavaScript

> JavaScript는 웹에 쓰이는 하나뿐인 프로그래밍 언어이다.

### JS의 분류

#### ECMAScript

- 일반적으로 알고있는 ES5, ES6 등이 ECMAScript를 뜻한다.
- Specification으로 ES 다음 숫자를 통해 Version을 알 수 있다.

#### Vanilla JavaScript

- 라이브러리가 없는 JS로 브라우저를 통해 제공된다.
  
  - 따라서, HTML에 JS를 추가하는 것은 쉽다.
  
- 프레임워크나 라이브러리가 없는 Vanilla JS를 학습하여 JS의 기초를 다지는 것이 좋다.

  

## 변수 (Variables)

> 계속 변하는 값이면서 그 값을 저장하는 공간

### 변수선언

1. const : constant, 변하지 않음 

2. let : 변수가 바뀌는 걸 허용함

3. var : varible, 변수가 바뀌는 걸 허용함 but, 특이한 규칙이 있기때문에 사용을 꺼려한다.

- 따라서, 변하지 않게 하려면 const 변하게 하려면 let을 쓰도록 하자

  


### 변수명

- Camel Case를 사용
  - 시작은 소문자로 시작
  - 스페이스가 필요하다면 스페이스 대신에 다음 문자를 대문자로 시작

```javascript
const myName = 'Jongjun'
```



### Type of Data

1. String

```javascript
const what = "Hello";
```

2. Boolean

```javascript
const what = true;
const what = false;
```

3. Number

```javascript
const what = 123;
```

4. Float

```javascript
const what = 55.1;	
```



### 배열 (Array)

> 데이터의 집합으로 정렬과 탐색에 용이하다.

- []으로 생성
- 모든 Type의 Data를 담을 수 있다.



### 객체 (Object)

> label을 통해 data를 담는다.

- {}으로 생성
- key : value로 작성
- 특정 key 값을 호출 할 때는 변수명 뒤에 `.`을 붙인다.
- 호출을 한 후 값을 변경해줄 수 있다. (변수명이 const라도 상관없음, 물론 const의 값 형식을 바꾸는 것은 안됨)
- 참고로 console도 object이다. 고로 console.log는 console이라는 object안의 key가 log인 것을 호출하는 것이다.

```javascript
const myInfo = {
	name: "Jongjun",
    age: 30,
    isMale: true,
    fav: ['Game', 'Movie', 'Baseket Ball']
}
console.log(myInfo.age)
myInfo.age = 31
```



## 함수 (Function)

### 함수생성

```javascript
function sayHello(argument) {
    return console.log('Hello', argument);
}
```

