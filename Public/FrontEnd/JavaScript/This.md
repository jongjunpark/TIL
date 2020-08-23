# This

> 무조건 어떤 **Object**를 지칭

- method : 객체안에 정의된 함수

- 일반적으로 this를 찍으면 window가 나옴

- function을 정의 할 때, this가 window가 아닌 경우

  1. method 안의 this

     - 해당 method가 정의된 객체(object)
     - 주의!

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
     // 위를 해결하려면 this.arr.forEach(function(){}).bind(this)를 해줘야한다.
     // bind(this)는 한 scope위의 this를 지침해준다.
     // 이게 불편해서 나온게 화살표함수다!!
     ...
     this.arr.forEach
     ```

     - 해결법

     ```javascript
     object1: {
         arr: [0,1,2]
         method1() {
                 this.arr.forEach(function(number){
                     console.log(this) // this = object1
                 }.bind(this) // bind(this)는 한 scope위의 this를 지침해준다.
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

     

  2. 생성자 함수 안의 this

     