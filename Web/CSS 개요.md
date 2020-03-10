![image-20200310111045359](C:\Users\Park\AppData\Roaming\Typora\typora-user-images\image-20200310111045359.png)

CSS 정의 방법

- 해당 태그내에 직접 \<style> 속성을 활용
- HTML파일 내에 \<style> 지정
- **외부 CSS파일을 \<head>내 \<link>를 통해서 불러오기**



선택자

- 특정한 요소를 선택하여 스타일링 하기 위함
- 기초선택자, 고급 선택자 필수, 의사선택자는 알아는 두자



상속

- 상속을 통해 부모요소의 속성을 자식에게 상속한다.
- 상속되는 것 : Text 관련 요소
- 상속되지 않는 것 : Box model 관련 요소, position 관련 요소



CSS적용 우선순위

1. 중요도(importance) - `!important`

2. 우선순위 : 1)인라인 2) id 선택자 3) class 선택자 4) 요소 선택자

3. 소스코드 순서 (HTML에서가 아닌 CSS에서의 소스코드 순서, 나중에 정의 된 것이 더 우선순위를 가짐(덮어씌운다는 개념?))



단위

`px`, `%`, `vw`, `vh`, `vmin`, `vmax`

`em` : 요소에 지정된 사이즈에 상대적인 사이즈

`rem` : 최상위 요소의 사이즈를 기준으로 배수단위를 가짐, root em -- 다시체크

브라우저의 폰트 픽셀은 16px



- 텍스트 : 변형서체 `<strong>`, `<em>`
- 컬러, 배경
- 목록꾸미기 등등..



Box model

- 구성

  ![image-20200311021158524](C:\Users\Park\AppData\Roaming\Typora\typora-user-images\image-20200311021158524.png)

  

- Margin 설정

  ```
  .margin{
   margint-top: 10px;
   margint-right: 20px;
   margint-bottom: 30px;
   margint-left: 40px;
  }
  // 상,우,좌,하 순
  ```

  \<shorthand>

  ![image-20200311021549988](C:\Users\Park\AppData\Roaming\Typora\typora-user-images\image-20200311021549988.png)

  ​	- 전체설정						- 상하 / 좌우					 - 상/좌우/하 					- 상/하/좌/우

- Padding 설정

  ```
  .margin-padding{
   margin: 10px;
   padding: 30px;
  }
  // margin 상하좌우 10px, padding 상하좌우 30px
  ```

- Border 설정

  ```
  /기본
  .border{
   border-width: 2px;
   border-style: dashed;
   border-colr: black;
  }
  
  /shorthand
  .border{
   border: 2px dashed black;
  }
  ```

- Q) div에 width: 100px을 설정해주면 실제 width는 몇인가??

  A) 142px

  ![image-20200311022338064](C:\Users\Park\AppData\Roaming\Typora\typora-user-images\image-20200311022338064.png)
  - Content는 100px이지만 padding, border의 값이 더해져서 142px이 됨
  - 이를 해결하기 위해 `box-sizing`을 이용한다.
  - 기본적으로 `box-sizing`은 `content-box`이다. 그러나 일반적으로 boder 까지의 너비를 봄
  - `box-sizing: border-box;` 를 설정해주면 box를 boder 영역까지 보는 것으로 됨
  - 즉, 위 코드와 함께 width: 100px을 설정해주면 100px의 box를 얻을 수 있다.

- Q) 텍스트1의 아래쪽 여백을 1(botom margin = 1), 텍스트 2의 윗쪽 여백을 3(top margin = 3)이라면 두 텍스트 사이의 간격은?

  A) 3

  ![image-20200311023108680](C:\Users\Park\AppData\Roaming\Typora\typora-user-images\image-20200311023108680.png)

  - 마진 상쇄 : 인접 형제 요소간의 margin은 겹쳐져서 보인다.



- 인라인 / 블록 레벨 요소

  - 대표적인 인라인 레벨 요소 : `span`, `a`, `img`, `input`, `label`, `b`, `em`, `i`, `strong` 등

  - 대표적인 블록라인 레벨 요소 : `div`, `ul`, `ol`, `li`, `p`, `hr`, `form` 등

  - Display 속성

    - display: block

      줄 바꿈이 일어나는 요소

      화면크기 전체의 가로폭을 차지한다.

      블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.

    - display: inline

      줄 바꿈이 일어나지 않는 행의 일부 요소

      content 너비만큼 가로폭을 차지한다.

      width, height, margin-top, margin-bottom을 지정할 수 없다.

      상하여백은 line-height로 지정한다.

    - display: inline-block

      inline과 block의 성질을 같이 가짐

      inline 처럼 한 줄에 표시가 가능하다

      block 처럼 `width`, `height`, `margin` 속성을 모두 지정할 수 있다.

      

  - 블록레벨의 경우 width를 가질 수 없는데 만약 실제 가질 수 있는 너비보다 작은 width를 지정한다면 나머지는 margin으로 채워진다. 그래서 꽉 채워지기 때문에 줄바꿈이 발생한다. 

  ![image-20200311023920940](C:\Users\Park\AppData\Roaming\Typora\typora-user-images\image-20200311023920940.png)

  ​	기본																				width = 100px을 주었을 때

  - 이를 이용해서 margin-right: auto를 주면 마진이 오른쪽에 형성되어 content는 왼쪽에

    margin-left: atuo는 content가 오른쪽에, margin-rigth: auto; margin-left: auto는 가운데에

    각각 정렬시킬 수 있다.

    

  - 인라인은 컨텐트 영역만큼만 너비와 높이를 가짐

  - 인라인의 정렬은 text-align : left(right, center);로 정렬