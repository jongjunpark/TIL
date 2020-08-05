# 콜백함수 (Callback Function)

> 함수 안에서 어떤 특정한 시점에 호출되는 함수

- 지금 당장 실행하는 것이 아니라 다른 누군가에 의해 때가되면 실행된다.

1. 다른 함수의 인자로써 이용되는 함수
2. 어떤 이벤트에 의해 호출되어지는 함수

- 예시
  - addEventListener("eventName", function1()) : Non-callback
    - event의 여부와 상관없이 function1을 바로 호출한다. 
  - addEventListener("eventName", function1) : Callback
    - event가 적용될 때 function1을 호출한다.