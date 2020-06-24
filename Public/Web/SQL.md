# SQL

> Structured Query Language, 관계형 데이터베이스(RDBMS) 관리시스템의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어, RDBMS에서 자료의 검색과 관리, 데이터베이스 스키마 생성과 수정, 데이터베이스 접근 관리 등을 위해 고안 됨.

- DDL : 데이터 정의 언어

- DML : 데이터 조작 언어
- DCL : 데이터 제어 언어

- 기본구조

  키워드  var 키워드 var;

- SELECT : 데이터를 읽어올 수 있으며, 특정한 테이블을 반환

  ```sql
  SELECT column FROM table;
  SELECT column FROM table [WHERE condition] [GROUP BY column] [ORDER BY column[ASC/DESC]] [LIMIT integer];
  ```

- 테이블 생성

  ```sql
  CREATE TABLE table(
  	column1 datatype [constraints],
     	column2 datatype [constraints],
  );
  # constraints : PRIMARY KEY, NOT NULL, UNIQUE, DEFAULT 등
  ```

- Datatype

| Affinity |                                                              |
| :------: | :----------------------------------------------------------: |
| INTEGER  | TINTYINT(1byte), SMALLINT(2bytes), MEDIUMINT(3bytes), INT(4bytes), BIGINT(8bytes), UNSIGNED BIG INT |
|   TEXT   |              CHARACTER(20), VARCHAR(255), TEXT               |
|   REAL   |                     REAL, DOUBLE, FLOAT                      |
| NUMERIC  |          NUMERIC, DECIMAL, BOOLEAN, DATE, DATETIME           |
|   BLOB   |                    no datatype specifi ed                    |

- 테이블 삭제

  ```sql
  DROP TABLE table;
  ```

- 추가 : 특정 테이블에 새로운 행을 추가하여 데이터를 추가

  ```sql
  INSERT INTO table (column1, column2) VALUES (value1, value2);
  ```

- 삭제 : 특정 테이블에 특정 레코드를 삭제

  ```sql
  DELETE FROM table WHERE condition;
  ```

- 수정 : 특정 테이블에 특정 레코드를 수정

  ```sql
  UPDATE table SET column=value1 WHERE condition;
  ```

- DISTINCT : 중복없이

- COUNT, AVG, MIN, MAX(var)

- LIKE 'pattern' : 특정 패턴을 조건문으로 넣을 수 있다.

- 와일드카드

  - % : 문자열이 있을 수도있다.
    - 2% : 2로 시작하는 값, %2 : 2로 끝나는 값, %2% : 2가 들어가는 값
  - _ : 반드시 한 개의 문자가 있다.
    - _2% : 아무값이나 들어가고 두번째가 2로 시작, 1\_ _ _ _ : 1로 시작하고 4자리인 값

- LIMIT : 개수 제한 (+OFFSET으로 제한조건)
- ORDER BY : 순서를 정함 (ASC(default) : 오름차순, DESC : 내림차순)
- GROUP BY : 그룹화