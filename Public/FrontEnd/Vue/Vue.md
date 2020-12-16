# 목차



# 내용

## Vue

### Creation

- 컴포넌트가 돔에 추가되기 전

#### beforeCreate

- 가장 먼저 실행 되는 훅
- data와 events가 세팅되지 않은 시점

#### Create

- data와 events가 활성화
- 부모 -> 자식 순서로 진행

### Mounting

- 컴파일, 렌더링 단계

#### beforeMount

- 렌더링이 되기 직전

#### mounted

- 렌더링 된 직후
- 자식 -> 부모 순서로 진행

### Updating

- 속성들이 변경되거나 어떤 이유로 재렌더링이 발생될 때

#### beforeUpdate

- 돔이 재렌더링되고 패치되기 직전

#### Updated

- 재랜더링 된 직후

### Destruction

- 해체단계

#### beforeDestroy

- 컴포넌트가 제거되기 직전

#### destroyed

- 해체된 직후
- 모든 바인딩 해제, 이벤트 제거, 하위 Vue 인스턴스 삭제

