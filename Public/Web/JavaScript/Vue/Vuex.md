# Vuex

> Vue.js 애플리케이션에 대한 상태관리패턴 라이브러리, 모든 컴포넌트에 대한 중앙 집중식 저장소 역할

- 시작 : vue add vuex

- props는 중앙저장소에 저장된 state에서 가져오면 됨
- emit은 중앙저장소의 state와 mutation을 이용하면 됨

- 접근법 : $store.vuexConceptName (ex. state, gatters, ...)
- 특징
  - index.js 내에서 화살표함수 사용 가능
  - v-for를 이용하는 경우에는 기존의 `emit`, `props`를 사용하는 것을 권장
  - 중앙집중화에 따라 index.js에 과부화가 일어날 수 있다. 따라서, 필수사용을 권장하지는 않는다.



## 시작하기 앞서 JS의 비구조화(ES6+)

```javascript
const myInfo = {
    name: 'jongjun',
    email: 'abc@email.com',
    phone: '010-1234-5678'
}
```

### 기본 Object 호출

- 기존

```javascript
const name = myInfo.name,
	email = myInfo.email,
    phone = myInfo.phone
```



- 비구조화

```javascript
// key와 변수명이 같아야 한다.
const { name } = myInfo,
      { email } = myInfo,
      { phone } = myInfo

const { name, email, phone } = myInfo  // key 순서는 상관없다.
```



### 함수에서의 응용

- 기존

```javascript
function getInfo(object) {
    console.log(`Hi, my name is ${object.name}, email is ${object.email}`)
}
getInfo(myInfo)
// 혹은
function getInfo(name, email) {
    console.log(`Hi, my name is ${object.name}, email is ${object.email}`)
}
getInfo(myInfo.name, myInfo.email) // 인자의 순서가 맞아야한다. 인자가 늘어나면 피곤해짐
```



- 비구조화

```javascript
function getInfo({ email, name }) { // object의 모든 key를 호출할 필요가 없다.
    console.log(`Hi, my name is ${name}, email is ${email}`)
}
getInfo(myInfo) // 인자의 순서가 상관이 없다.
```



## state

> data의 집합 ( 중앙관리할 모든 데이터 === 상태 )

- 기존 vue에서의 data라고 생각하면 됨 그 중 중앙에서 관리할 것들

- 호출 : $store.state.**stateKeyName**

### `mapState`

- store의 `state`를 local의 `data`에 매핑이 가능하다. but 권장하지않음
- 따라서 사용하려면 local의 `computed`에 매핑하는 것을 권장
- 사용법은 아래의 `mapGetters`와 동일



## getters

> state를 (가공해서) 가져올 함수들

- 기존 computed와 유사
- 구조 : function(**state**) { return ... ) (첫번째 인자는 강제로 state가 넘어옴)
- 호출 : $store.getters.**functionName**

### `mapGetters`

- 코드의 복잡성을 줄이기 위해 store의 `getters`를 local의 `comupted`에 매핑

- 사용법

  ```javascript
  import { mapGetters } from 'vuex'
  ...
      computed: {
          ...mapGetters([
              'gettersFunctionName1',
              'gettersFunctionName2',
              ...
          ])
      }
  ```

  

## mutations

> state를 변경하는 함수들 ( mutations에 작성되지 않은 state 변경코드는 모두 동작하지 않는다. )

- 모든 mutation 함수들은 동기적으로 동작
- commit을 통해 실행
- 구조 : function(**state**, **payload**) (첫번째 인자는 강제로 state가 넘어옴)
- 호출 : $store.commit(**'functionName'**, **payload**)
- event 상황에서 함수 호출 시 payload에 자동으로 event정보가 넘어온다.

### `mapMutations`

- store의 `mutations`를 local의 `methods`에 매핑
- 사용법

```javascript
import { mapMutations } from 'vuex'
...
	methods: {
        ...mapMutations([
            'mutationsFunctionName1',
            'mutationsFunctionName2',
            ...
        ])
    }
```



## action

> 범용적인 함수들, mutations에 정의한 함수를 actions에서 실행 가능

- 비동기 로직은 actions에서 정의

- dispatch를 통해 실행
- 구조 : function(**context**) (context는 store에 범용적인 접근이 가능케 함)

- 호출 : $store.dispatch(**'functionName'**, **data**) 
  - dispatch는 인자 2개가 최대, 만약 여러개를 넘기고 싶다면 두번째 인자를 iterable화 해야 함
- event 상황에서 함수 호출 시 두번째 인자에 자동으로 event정보가 넘어온다.

### `mapActions`

- store의 `actions`를 local의 `methods`에 매핑
- 사용법은 `mapMutations`와 동일



## modules

