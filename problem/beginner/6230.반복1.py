scores = [88, 30, 61, 55, 95]
for idx, score in enumerate(scores):
    if score >= 60:
        print("{0}번 학생은 {1}점으로 합격입니다.".format(idx + 1, score))
    else:
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(idx + 1, score))