# 0. Init

## 공식문서

- 빈 Git repositoty를 생성
- .git 폴더 생성

## 쉽게

- init은 등록이다.

- Git으로 관리하고 싶은 폴더를 등록한다.



# 1. ADD

## 공식문서

- 다음 commit을 위해 working tree의 내용을 index에 업데이트 하는 것
  - index에는 working tree 내용의 snapshot이 있으며
  - 이 snapshot은 다음 commit에 사용된다.
  - 즉, commit하기 전 반드시 add를 통해 index에 새로운 혹은 수정된 파일을 추가해야 한다. 
- 일반적으로 현재 경로 전체를 add하지만 옵션을 통해 부분적인 add도 가능하다.
- add는 commit 전에 여러번 사용할 수 있다. 

## 쉽게

- add는 기록이다.
- 현재 폴더에서 바뀐(생성/수정/삭제) 파일이 있다면 그 파일을 앞으로 관리를 할 것인가에 대해 선택을 할 수 있다.
- 관리를 원하는 파일들은 add 명령어를 통해 이뤄지며 index(stage)라는 곳에 기록이 된다.
- 다음단계인 commit 전에는 add를 여러번할 수 있고 관리하는 파일은 가장 최근 상태가 반영된다.



# 2. Commit

## 공식문서

- index에 담겨있는 현재 내용들을 log message와 함께 commit 한다.
  - log message는 변경된 것을 설명함

- 새로운 commit은 일반적으로 현재 branch의 끝부분이며 branch는 이 commit을 가르키도록 업데이트 된다.

## 쉽게

- commit은 저장이다.
- 앞서 add를 통해 index에 관리하고 싶은 파일을 기록했을 것이다.
- 그럼 commit을 통해 index에 담긴 정보를 내 컴퓨터에 저장을 한다.



# 3. Push

## 공식문서

- local reference를 사용해서 remote reference를 업데이트

## 쉽게

- push는 전달이다.
- 마지막 commit을 기준으로 내 컴퓨터에 저장된 정보를 원격저장소에 전달을 한다.2

