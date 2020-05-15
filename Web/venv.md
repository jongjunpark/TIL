- pip list 만들고 인스톨하기

`pip freeze > requirements.txt`

`pip install -r requirements.txt`



- 가상의 python 만들기

`python -m venv {name}` (일반적으로 name = venv)

`source {name}/bin/activate`



- 이제 프로젝트 시작할 때

1. 프로젝트 폴더 생성
2. .gitignore => venv/
3. python -m venv venv
4. source venv/bin/activate
5. pip install django

...

6. pip freeze > requirements.txt



- DB -> file

  ```bash
  $ python manage.py dumpdata {filename}
  ```

- file -> DB

  ```bash
  $ python manage.py loaddata
  ```

  