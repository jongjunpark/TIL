#리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
#입력
#10 10 20 30 40
#출력
#입력된 값 [10, 10, 20, 30, 40]의 평균은 22.0입니다.

input_list = []
for i in range(1,6):
    input_list.append(int(input()))
result = 0
for j in input_list:
    result += j

print("입력된 값 {0}의 평균은 {1}입니다.".format(input_list, result/len(input_list)))