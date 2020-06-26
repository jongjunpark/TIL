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

- 일반적으로 상수는 Upper Case를 사용

```javascript
const GRAVITY_ACCEL = 9.8
const NAVER_URL = 'http://www.naver.com'
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



## DOM (Document Object Model)

> JavaScript를 통해 HTML에 접근할 수 있다. (일반 홈페이지에서 console.log(document)를 해보자)

- JavaScript는 Document를 통해 html의 모든 요소를 가지고 올 수 있다.
- 그 후 선택된 것은 Object로 바꾼다.
- select된 DOM을 console.dir() 해보자. 가능한 객체표기법들이 나온다. 그리고 그 것들을 수정할 수 있다!

- 주요 객체
  - window : DOM문서를 표현하는 창, 가장 최상위 객체로 다양한 함수, 이름공간, 객체 등이 포함 됨

  - document : 페이지 콘텐츠의 진입점 역할, `<body>`등 다른 요소들을 포함

  - navigator, location, history, screen

    

### 선택자

> 원하는 DOM을 선택하기 위함

- getElementById(id) : DOM에서 특정 id값을 가진 엘리멘트를 반환
- getElementsByClassName(class) : 특정 클래스명을 가진 엘리멘트들을 NodeLIst로 반환
- querySelector(selector) : 노드의 자식 중 특정 선택자를 가진 첫번째 자식을 반환
- querySelectorAll(selector) : 노드의 자식 중 특정 선택자를 가진 모든 자식을 array로 반환 



### 엘리먼트 생성

> Node 생성

- crateElement("tagName") : tag를 생성한다.

- parentNode.appendChild(childName) : 자식요소를 추가한다. (맨아래 자식으로)

  ```javascript
  li.appendChild(span)
  /* <li>
  	<span>
     </li> */
  ```

- parentNode.removeChild(childName) : 자식요소에서 제거한다.



### HTMLElement

> DOM 조작

**if (want replace) {**

#### className

- class를 부여한다. 만약 이미 class가 있다면 부여한 class로 대체된다.

- CSS에 class 선택자를 통해 style을 미리 만든 후 className을 줘서 디자인변경을 이룰 수 있다.

**} else { **

#### classList

- class를 List화 하여 여러개의 class를 다룬다.

- add : List에 추가
- remove : List에 제거
- contains : 해당 value가 존재하는지 확인
- toggle : 인자가 List 내에 true라면 remove, false라면 add 함

**}**

#### innerText

- Text를 삽입한다.
- html 태그가 있다면 text 그대로 삽입된다.



#### innerHTML

- HTML로 파싱하여 값에 html 태그가 있다면 적용이 된다.
- XSS 공격에 취약하여 보안상 문제가 있다.
- \<br>을 통해 줄바꿈을 만들 수 있다.



#### value

- value값을 삽입한다.

  

#### style

-  각종 style을 수정한다.



### addEventListener

> Event에 귀를 기울여 Event가 발생했을 때 취할 행동을 정의

- 기본구조 : selectedDOM.addEventListener(**event type**, **function**)
- 주의할 점
  - addEventListener("eventName", function1())의 경우는 event의 여부와 상관없이 function1을 바로 호출한다. 
  - addEventListener("eventName", function1) 의 경우는 event가 적용될 때 function1을 호출한다.
- event.preventDefault() : 해당 event의 default가 실행되지 않는다.





## 조건문 (if-else)

생략

### 삼항연산자

- 구조 : `조건` ? `true일 때 실행할 것` : `false일 때 실행할 것`



## 내부함수

### Date

> 현재 날짜정보

- 구조 : new Date()

- `.getHours`, `.getMinutes`, `.getSeconds` : 시, 분, 초
- `.getFullYear`, `.getMonth`, `.getDate` : 연, 월, 일
- `.getDay` : 요일 (1: Monday)



### setInterval

> timeout(millisecond)을 통해 시간간격을 두고 함수를 계속 실행

- 구조 : setInterval(**function**, **timeout**)



### localStorage

> 로컬PC의 임시 저장소, 새로고침을 해도 남아있다.

- `.setItem(key, value)` : key : value의 형태로 local storage에 담는다
- `.getItem(key)` : 해당 key의 value값을 반환한다.



## 참고

### 도움되는 사이트

- flatuicolors.com : 컬러값을 얻을 수 있는 사이트



### 궁금한 것

- Q1) 상수값은 Upper Case로 한다?

- Q2) const는 변하지 않는 값??

```javascript
const title = document.querySelector("#name")
const currentColor = title.style.color
// click event를 통해 색을 바꾸는 경우 currentColor값이 변하는데 왜 에러가 안뜨는가?
// 그리고 let이 있는데 const를 쓰는 이유가 있는가? 	
```