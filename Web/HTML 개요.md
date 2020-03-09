# HTML

> HTML : Hyper Text Markup Language



## 의의

- Hyper Text : 다른 여러개의 텍스트로 넘어갈 수 있는 텍스트
- Markup : 문서를 구조적으로 구성하는 것
- 즉 HTML은 Hyper Text를 이용해 문서의 구조를 잡는 것이라고 보면 됨
- HTML5 : HTML의 최신규격으로 W3C와 WHATWG의 협업으로 제정됨



## 구성

- DOM(Document Object Model)트리로 구조화 되어있음

![image-20200309113520327](C:\Users\Park\AppData\Roaming\Typora\typora-user-images\image-20200309113520327.png)

- 요소(element)

  여는태그 + 닫는태그로 구성, 셀프클로징 태그도 존재

- 속성(Attribute)

  태그별로 사용할 수 있는 속성은 다르다.

  공백사용x, ""사용

- Head

  Open Graph Protocol이라는 규약을 통해 메타 데이터를 표현

- 시맨틱태그

  마크업을 할 때 보기편하게 의미 있는 정보의 그룹을 태그로 표현

- 그룹컨텐츠

  마크다운에서 사용하던 명령어들과 유사

  \<p>, \<hr>, \<div> 등등

- 텍스트 관련 요소

  \<a>, \<b> vs \<strong>, \<i> vs \<em>, \<span>, \<br>, \<img>

  이 때 \<strong>, \<em>은 \<b>,\<i>와 출력은 같지만 강조의 의미를 가지고 있다.

  \<b>,\<i> 쓰지말고 스타일링은 CSS를 이용하자

- Table, Form

  Table = 표만들때, Form = 로그인화면에 많이 쓰임