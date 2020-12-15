# 비동기 (Asynchronous)

- 기존방식의 요청
  - 1 요청, 1 새로고침
- 비동기방식을 쓰면 새로고침을 할 필요없이 JS로 필요한부분만 요청-응답을 통해 데이터를 수정할 수 있다.



## 싱글스레드 JS

- Django의 경우 스레드가 부족하면 늘리면된다.
- 하지만 브라우저는 하나의 페이지에 하나의 스레드만 작동된다.
- 왜 JS는 싱글스레드일까? 두가지 가설이 존재
  - 첫번째, 옛날에 만들어질 때 잘못 설계
  - 두번째, 서버와 달리 브라우저에서는 잘못된 코드로 인해 피해를 입는 대상이 유저이다. 그렇기 때문에 다중스레드일 경우 큰 손상을 일으킬 수 있다. 따라서 의도된 것이다.
- 그렇다면 JS에서 어떻게 동시성 동작이 가능할까?



## Javascript Runtime

- JS Engine
- 그리고 시간이 소요되는 작업을 위해 Web API, Task Queue, Event Loop라는 요소가 존재한다.

![image-20200629202842782](비동기 (Asynchronous).assets/image-20200629202842782.png)

참고([https://hudi.kr/](https://hudi.kr/비동기적-javascript-싱글스레드-기반-js의-비동기-처리-방법/))



### Call Stack

- 기본적으로 JS는 Stack의 구조로 후입선출의 방식으로 함수를 처리한다.
  - 즉, 하나의 함수가 종료돼야 다음 함수가 실행가능하다.
- 비동기작업이 있다면 콜백함수와 함께 Web API로 넘겨주고 Stack에서 나온다.

### Web API

- 한번에 여러개가 들어올 수 있다.
- 들어온 비동기작업 중 먼저 작업이 끝나는 순서대로 Task Queue로 콜백함수를 넘겨준다.

### Task Queue & Event Loop

- 선입선출 구조로 먼저들어온 콜백함수부터 먼저 나간다.
- Event Loop는 Call Stack이 비어있는지? 그리고 Task Queue에 Task가 있는지를 확인한다.
- 만약 Call Stack이 비어있고 Task Queue에 콜백함수가 있다면 해당 콜백함수를 Call Stack으로 넘겨준다.



## Ajax (Asynchronous Javascript And Xml)

> JavaScript를 이용한 비동기 통신

- 브라우저가 가지고있는 XMLHttpRequest 객체를 이용해서 전체페이지를 새로고치지 않고 페이지 일부만을 위한 데이터를 로드하는 기법

### Axios

> Promise based HTTP cilient for the browser and node.js

- Promise를 return한다.
- JSON형태

#### Promise

> 약속, 성공한 경우와 실패한 경우만 생각하자는 약속

- 콜백지옥에서 벗어나기 위해, 비동기 작업들을 순차적으로 혹은 병렬적으로 처리하여 컨트롤이 수월해진다.
- 코드의 가시성이 높아지고 오류처리에도 도움이 된다.

- 성공했을 때, 어떤 일을 한다. `.then(function)`
- 실패했을 때, 어떤 일을 한다. `.catch(function)`





