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
    hi: hi,
    sayHello: function() {
        return 'Hello'
    }
}
console.log(myInfo.age)
myInfo.age = 31

// ES6+
const myInfo = {
    //  key 문자열과 value의 변수명이 같을 때 단축 가능
    hi,
    sayHello() {
        return 'Hello'
    }
}
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



### 엘리먼트 생성 및 삭제

>  Node 생성

- crateElement("tagName") : tag를 생성한다.

- parentNode.appendChild(childNode) : 자식요소를 추가한다. (맨아래 자식으로)

  ```javascript
  li.appendChild(span)
  /* <li>
  	<span>
     </li> */
  ```

- childNode.removeChild(parentNode) : 자식요소에서 제거한다.



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
- event.target : event를 전달한 객체에 대한 참조
  - event.target.parentNode : event 전달 객체의 부모 노드 정보



### Event type

#### mousemove

> mouse를 이동할 때

- clientX,Y : window 기준 좌표
- offsetX,Y : target 기준 좌표



#### mousedown

> mouse를 클릭할 때



#### mouseup

> mouse가 클릭된 상태에서 해소될 때



#### mouseenter

> mouse가 target에 들어왔을 때



#### mouseleave

> mouse가 target안에 있다가 벗어났을 때



#### click

> mouse 좌클릭



#### contextmenu

> mouse 우클릭 시 나오는 팝업(?)창

- preventDefault를 이용하면 없앨 수 있다.



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

> 로컬PC의 임시 저장소, 새로고침을 해도 남아있다. string만 저장할 수 있으므로 주의하자.

- `.setItem(key, value)` : key : value의 형태로 local storage에 담는다.
  - value가 object라면 string형태로 변환해주는 `JSON.stringify`를 사용하자
- `.getItem(key)` : 해당 key의 value값을 반환한다.



### JSON.stringify

> object -> string

- 구조 : JSON.stringify(**object**)



### JSON.parse

> string -> object

- 구조 : JSON.parse(**string**)



#### Array.from

> iterable -> array

- 구조 : Array.from(**iterable**)



### forEach

> array 전용. array의 원소 각각에 한번씩 함수를 실행시킴

- 구조 : arrayName.forEach(**function**)



### filter

> array 전용. array의 원소 각각에 한번씩 함수를 실행시킴 이 때, 함수를 통해 true를 반환하는 값만 따로 모아서 새로운 배열로 반환

- 구조 : arrayName.filter(**function**)



### parseInt, parseFloat, Number

> string -> Int, Float

- 구조 : parseInt(**string**), parseFloat(**string**), Number(**string**)

- Number의 경우에는 문자로 되어있는 숫자의 type에 따라 정수형 또는 실수형으로 변환한다.



### String

> number -> string

- 구조 : String(**num**)



### Math

#### .random

> 0~1 사이의 숫자를 랜덤하게 반환

- 구조 : Math.random()

#### .floor

> floor = 바닥으로 내림을 의미

- 구조 : Math.floor(**num**)

#### .ceil

> ceilling = 천자으로 올림을 의미

- 구조 : Math.ceil(**num**)



### Image()

> HTMLImageElement 생성

- 구조 : new Image()
- document.createElement("img") 와 같다.



### Navigator

#### .geolocation.getCurrentPosition

> 현재 위치를 반환

- 구조 : navigator.geolocation.getCurrentPosition(**success fn**, **fail fn**)



## 호이스팅

- 호이스팅은 끌어올림이다.

- 함수 안에 있는 선언들을 모두 끌어올림 이 때 변수는 `var`만 해당

- 선언에는 변수와 함수의 선언 두가지 종류가 있다.

  ```javascript
  function getX() {
    console.log(x); // undefined
    var x = 100;
    console.log(x); // 100
  }
  getX();
  
  //------- 내부 호이스팅의 결과 --------
  function getX() {
    var x;
    console.log(x);
    x = 100;
    console.log(x);
  }
  getX();
  ```

  - x가 선언되지 않았지만 undefined로 출력이 가능했던 이유는 사실 내부에서 Parser가 `var`선언을 호이스팅 했기 때문이다.

    

  ```javascript
  foo();
  foo2();
  
  function foo() { // 함수선언문
      console.log("hello");
  }
  var foo2 = function() { // 함수표현식
      console.log("hello2");
  }
  
  //------- 내부 호이스팅의 결과 --------
  var foo2; // [Hoisting] 함수표현식의 변수값 "선언"
  
  function foo() { // [Hoisting] 함수선언문
      console.log("hello");
  }
  
  foo();
  foo2(); // ERROR!! 
  
  foo2 = function() { 
      console.log("hello2");
  }
  ```



## Closure

- 두 개의 함수로 만들어진 환경
- 내부 함수가 외부 함수의 반환값으로 사용된다.
- 정보의 은닉을 위해 함수안에서 변수를 사용하고 싶을 때 사용하면 유용하다.
  - closure를 사용하지 않으면 매번 함수를 호출할 때 마다 값이 초기화되지만
  - closure를 사용하면 return값에 변수를 가지고 있다.



## this

- `this`는 무조건 어떤 Object를 지칭한다.
- 다양한 상황에 따라 `this`가 지칭하는 것은 달라진다.

#### 객체의 매소드안의 This

```javascript
object1: {
    arr: [0,1,2]
    method1() {
        this.arr.forEach( 	// 이 때의 this는 method1 안의 this로 object1을 가르킴
        	function(number){
                console.log(this)
                // 이 때의 this는 method안에 있는 this가 아니므로 window를 가르킴
            }
        )
    }
}
```

- 객체의 매소드안의 `this`는 객체를 가르키는 것을 확인할 수 있다.



#### 함수를 호출할 때

- 함수 호출 시 `this`는 전역객체에 바인딩 된다.
- 또한 객체에 존재하는 매소드안의 함수에서의 `this`도 window를 가르킨다. 이를 해결하기 위해 `bind`를 사용한다.
  - `bind(this)`는 한 scope 위의 `this`를 지칭해준다.
  - 더 나아가서 `bind`의 불편함을 해결하기 위해 **화살표 함수**가 등장했다.

```javascript
object1: {
    arr: [0,1,2]
    method1() {
            this.arr.forEach(function(number){
                console.log(this) // this = object1
            }.bind(this) // bind(this)는 한 scope위의 this를 지칭해준다.
    	) 
    }
}

// bind가 불편해서 나온게 화살표함수다!!
object1: {
    arr: [0,1,2]
    method1() {
        this.arr.forEach(function(number) => {
        	console.log(this) // this = object1
        }) 
    }
}
```



#### 생성자 함수를 통해 객체를 생성할 때



## Promise

> 약속, 성공한 경우와 실패한 경우만 생각하자는 약속

- 콜백지옥에서 벗어나기 위해, 비동기 작업들을 순차적으로 혹은 병렬적으로 처리하여 컨트롤이 수월해진다.
- 코드의 가시성이 높아지고 오류처리에도 도움이 된다.

- 성공했을 때, 어떤 일을 한다. `.then(function)`
- 실패했을 때, 어떤 일을 한다. `.catch(function)`



### Async/Await

- 비동기 코드의 겉모습과 동작을 좀 더 동기 코드와 유사하게 만들어준다.
- `await` 키워드는 오직 `async` 로 정의된 함수의 내부에서만 사용될 수 있다.
- `await`은 promise의 값이 사용가능할 때까지 메소드의 실행을 일시중지시킨다.



### Arrow Function

- 기존의 function 표현방식보다 간결하게 함수를 표현할 수 있다. 
- 상위 스코프 this를 위해 사용하는 `bind`를 대체할 수 있다.



## 참고

### 도움되는 사이트

- flatuicolors.com : 컬러값을 얻을 수 있는 사이트



### MDN

- Canvas API : https://developer.mozilla.org/ko/docs/Web/HTML/Canvas



### 궁금한 것

- Q1) 상수값은 Upper Case로 한다?

- Q2) const는 변하지 않는 값??

```javascript
const title = document.querySelector("#name")
const currentColor = title.style.color
// click event를 통해 색을 바꾸는 경우 currentColor값이 변하는데 왜 에러가 안뜨는가?
// 그리고 let이 있는데 const를 쓰는 이유가 있는가? 	
```