## DOM & Event

### DOM (Document Object Model)

- 문서의 구조화된 표현을 제공, DOM 구조에 접근할 수 있는 방법을 제공
- 문서구조, 스타일, 내용 등을 변경할 수 있도록 도우며, 구조화된 노드와 오브젝트로 문서를 표현
- 주요 객체
  - window : DOM문서를 표현하는 창, 가장 최상위 객체로 다양한 함수, 이름공간, 객체 등이 포함 됨
  - document : 페이지 콘텐츠의 진입점 역할, `<body>`등 다른 요소들을 포함
  - navigator, location, history, screen

- 접근

  - 단일 Node 
    - **document.querySelector(selector)**
    - document.getElementByID(id)
  - HTMLCollection(live) : 변경을 할 때마다 값들이 실시간으로 계속 바뀜
    - document.getElementsByTagName(class)
    - document.getElementsByClassName(class)
  - NodeList(non-live) : 값들이 실시간으로 계속 바뀌지 않음 (경우에 따라 live 될 수도 있음)
    - **document.querySelectorAll(selector)**

  ```javascript
  // live
  const liveNodes = document.getElementsByClassName('live');
  for (let i=0; i<liveNodes.length; i++) {
      liveNodes[i].className = "red";
  }
  > 빨강	// live는 배열이 3개있었는데 첫번째가 red로 변경됨에 따라 배열이 2개로 줄었음
    검정	// 따라서 [1,2,3]이 [2,3]이 되어 i = 1 차례때 2가 아닌 3에 반영됨
    빨강	// 즉, 실시간으로 계속 변동됨
  // non-live
  const nonLiveNodes = document.querySelectorAll('.non-live');
  for (let i=0; i<nonLiveNodes.length; i++) {
      liveNodes[i].className = "red";
  }
  > 빨강	//non-live는 그냥 변동없이 [1,2,3]이 유지되니깐 i = 0,1,2 모두 빨강이 적용 됨
    빨강
    빨강
  ```

- Node 기준 탐색 (그냥 있다는 것만 기억해 두자)

  - parentNode, firstChild, lastChild
  - Element
    - children
    - previousElementSibling, nextElementSibling
  - 모든요소
    - childNodes
    - prevSibling, nextSibling

- Node 생성
  - document.createElement(tagName) : 특정 태그 생성
  - document.createTextNode(text) : 텍스트 노드 생성
  - parentNode.appendChild(Node) : 마지막 자식 요소로 추가
  - parentNode.removeChild(Node) : 해당 요소를 제거
- 조작
  - innerHTML, insertAdjacentHTML : JavaScript에서 HTML을 수정할 수 있도록 함 (보안 이슈는 있음)
    - element.innerHTML(text)
    - element.insertAdjacentHTML(position, text)
  - attribute : 속성값을 바꿔줄 수 있음
    - style
      - element.style.color
      - element.style.backgroundColor
    - element.setAttribute(attributeName, value)
    - element.getAttribute(attributeName)



### Event

- 브라우저에서 특정한 이벤트가 발생하면 이에 대한 이후 행위를 정의할 수 있다.

- 이벤트를 정의하는 경우, 인라인으로도 작성 가능하나 분리하여 작성하는 것이 좋다.

- 이벤트 예시) load, copy, mouseover, click, submit 등

  - addEventListener
    - EventTarget.addEventListener(type, listener, [, useCapture]);
      - type : 이벤트 유형 // listener : 이벤트가 발생했을 때 실행할 함수 // useCapture : 상위(false) or 하위(true)노드로 전파

  ```javascript
  // 숙지해야 할 기본구조!!
  const button = document.querySelector('button');
  button.addEventListener('click', function(){
      console.log('click');
  })
  ```

- 이벤트 객체 : 이벤트에 지정된 함수는 이벤트 객체를 매개변수로 받을 수 있음

  - Event.target : 이벤트가 원래 발생하였던 대상
  - Event.currentTarget : 이벤트가 발생하였던 대상
  - Event.preventDefault() : 이벤트를 취소
  - Event.stopPropagation() : 이벤트 전파 중단 

