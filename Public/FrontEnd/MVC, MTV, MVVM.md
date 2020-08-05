# MVC

> Model(DB) + View(HTML/CSS) + Controller(Logic)

- 동적웹에서 사용
- 규모가 큰 웹페이지에서 기능을 분리, 모듈화한 것
- 서로 영향을 끼치지 않는다.

- 하지만, 대규모 프로그램 개발에서 Controller가 비대화되는 문제점을 가지고 있다.



# MTV

> Model(DB, models.py) + Template(HTML/CSS) + View(Logic, views.py)

- 기능은 MVC와 거의 동일



# MVVM

> Model(DB), ViewModel, View(HTML/CSS)

- ViewModel은 View를 위한 Model
- Model과 View 사이의 의존성이 없다.

- ViewModel의 대표는 Vue.js

