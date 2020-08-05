### Array helper methods

- forEach : 주어진 함수를 배열의 요소 각각에 대해 실행

```javascript
const numbers = [1, 2, 3]
numbers.forEach(function(elem, idx, arr) {
    console.log(elem, idx, arr)
})
> 1 0 > [1, 2, 3]
  2 1 > [1, 2, 3]
  3 2 > [1, 2, 3]
// forEach다음에 함수를 즉각적으로 실행 function의 첫 매개변수는 필수고 나머지 두개는 optional
```

- filter : 주어진 함수를 배열의 요소 각각에 대해 실행하여 반환값이 True인 요소를 모아 배열을 반환

```javascript
const products = [
    { name: 'cucumber', type: 'vegetable'},
    { name: 'banana', type: 'fruit'},
    { name: 'carrot', type: 'vegetable'},
    { name: 'apple', type: 'fruit'}
]
products.filter(function(product) {
    return product.type === 'fruit'
})
> 0: {name: 'banana', type: 'fruit'}
  1: { name: 'apple', type: 'fruit'}
```

- map : 주어진 함수를 배열의 요소 각각에 대해 실행한 결과를 모아 배열을 반환

```javascript
const numbers = [1, 2, 3]
numbers.map(function(number) {
    return number * 2
})
> [2, 4, 6]
```

- every : 주어진 함수에 모든 요소가 True인 경우 True (boolean값을 반환)
- some : 주어진 함수에 하나라도 True인 경우 True (boolean값을 반환)



### Closure

- 함수와 함수가 선언된 어휘전 환경의 조합이다.
- 쉽게말해 함수를 둘러싸고 있는 환경(지역 변수, 코드 등)을 계속 유지하다가 함수를 호출할 때 다시 꺼내서 사용하는 함수

```javascript
function count() {
    var cnt = 0
    
    return function() { // count함수는 return을 function으로 한다는 것에 주의할 것
        cnt += 1
        return cnt
    }
}

var a = count() // count 함수는 function을 리턴했기 때문에 a는 함수 function()이 들어가 있다.
console.log(a()) > 1 // function()을 통해 cnt 1의 값을 가짐
console.log(a()) > 2 // 함수를 둘러싸고 있는 환경을 통해 cnt 1을 받아 다시 function()을 돌려 2의 값이 반환됨
var b = count() // 새로이 count를 만들었기 때문에 cnt가 초기화 됨
console.log(b()) > 1
```

