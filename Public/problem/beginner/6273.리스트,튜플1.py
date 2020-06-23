
score = [(90, 80), (85, 75), (90, 100)]

for inx, val in enumerate(score):
    total = 0
    for scores in val:
        total += scores
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2}입니다.".format(inx + 1, total, total/2))

